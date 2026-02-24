"""CLI entrypoint for onboarding and run modes."""

from __future__ import annotations

import argparse
import asyncio

from src.application.services.onboarding_service import OnboardingInput, OnboardingService
from src.application.services.resume_parser_service import ResumeParserService
from src.domain.models.user_config import UserConfig
from src.infrastructure.storage.sqlite_storage import SQLiteStorage  # type: ignore[import-not-found]


async def run_onboarding(args: argparse.Namespace) -> None:
    storage = SQLiteStorage(args.db_path)
    await storage.initialize()
    service = OnboardingService(storage=storage, resume_parser=ResumeParserService())

    config = UserConfig(
        telegram_bot_token=args.telegram_bot_token,
        openai_key=args.openai_key,
        model_name=args.model_name,
        model_base_url=args.model_base_url,
    )
    payload = OnboardingInput(
        telegram_chat_id=args.telegram_chat_id,
        config=config,
        resume_path=args.resume_path,
        cover_letter_text=args.cover_letter,
    )
    user_id = await service.run(payload)
    print(f"Onboarding completed for user_id={user_id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apply Job Claw CLI")
    parser.add_argument("--db-path", default="apply_job_claw.db")

    subparsers = parser.add_subparsers(dest="command", required=True)
    onboard = subparsers.add_parser("onboard", help="Run onboarding flow")
    onboard.add_argument("--telegram-chat-id", type=int, required=True)
    onboard.add_argument("--telegram-bot-token", required=True)
    onboard.add_argument("--openai-key", required=True)
    onboard.add_argument("--model-name", default="gpt-4o-mini")
    onboard.add_argument("--model-base-url", default="https://api.openai.com/v1")
    onboard.add_argument("--resume-path")
    onboard.add_argument("--cover-letter")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "onboard":
        asyncio.run(run_onboarding(args))


if __name__ == "__main__":
    main()
