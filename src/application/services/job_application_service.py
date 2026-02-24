"""Job application orchestration service."""

from __future__ import annotations

from typing import Any

from src.domain.interfaces.browser import IBrowserAutomation
from src.domain.interfaces.handlers import (
    IAuthenticationHandler,
    IFormFiller,
    IJobApplicationHandler,
)
from src.domain.interfaces.storage import IStorage
from src.domain.interfaces.telegram import ITelegramBot


class JobApplicationService(IJobApplicationHandler):
    """Coordinates browser automation, user input, and persistence."""

    def __init__(
        self,
        storage: IStorage,
        browser: IBrowserAutomation,
        form_filler: IFormFiller,
        auth_handler: IAuthenticationHandler,
        telegram_bot: ITelegramBot,
    ) -> None:
        self.storage = storage
        self.browser = browser
        self.form_filler = form_filler
        self.auth_handler = auth_handler
        self.telegram_bot = telegram_bot

    async def start_application(self, user_id: int, job_url: str) -> int:
        application_id = await self.storage.create_job_application(user_id, job_url)
        await self.storage.update_job_application(application_id, "in_progress")
        return application_id

    async def process_application(self, application_id: int) -> dict[str, str]:
        application = await self.storage.get_job_application(application_id)
        if application is None:
            return {"status": "failed", "message": "Application not found"}
        await self.browser.navigate(application["job_url"])

        if await self.auth_handler.detect_login_required():
            await self.storage.update_job_application(application_id, "awaiting_user_input", {"reason": "login_required"})
            return {"status": "awaiting_user_input", "message": "Login required"}

        profile = await self.storage.get_user_profile(application["user_id"]) or {}
        form_data = self._flatten_profile(profile)
        unmatched = await self.form_filler.fill_form(form_data)
        await self.storage.add_application_history(application_id, "form_filled", {"unmatched": unmatched})
        submitted = await self.form_filler.submit_form()
        if submitted:
            await self.storage.update_job_application(application_id, "completed")
            return {"status": "completed", "message": "Application submitted"}
        await self.storage.update_job_application(application_id, "failed", {"reason": "submit_button_not_found"})
        return {"status": "failed", "message": "Unable to submit"}

    async def handle_user_response(self, application_id: int, response: str) -> dict[str, str]:
        await self.storage.add_application_history(application_id, "user_response", {"response": response})
        await self.storage.update_job_application(application_id, "in_progress")
        return {"status": "in_progress", "message": "Response recorded"}

    async def handle_otp(self, application_id: int, otp_code: str) -> dict[str, str]:
        accepted = await self.auth_handler.submit_otp(otp_code)
        status = "in_progress" if accepted else "awaiting_otp"
        await self.storage.update_job_application(application_id, status)
        await self.storage.add_application_history(application_id, "otp_submitted", {"accepted": accepted})
        return {"status": status}

    async def cancel_application(self, application_id: int) -> None:
        await self.storage.update_job_application(application_id, "cancelled")
        await self.storage.add_application_history(application_id, "cancelled", {})

    def _flatten_profile(self, profile: dict[str, Any]) -> dict[str, Any]:
        flattened: dict[str, Any] = {}
        for section in ("personal_info", "work_authorization"):
            section_data = profile.get(section)
            if isinstance(section_data, dict):
                flattened.update(section_data)
        skills = profile.get("skills")
        if isinstance(skills, dict):
            technical = skills.get("technical_skills") or []
            if isinstance(technical, list):
                flattened["skills"] = ", ".join(str(item) for item in technical)
        return flattened
