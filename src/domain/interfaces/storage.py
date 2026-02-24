"""Storage interface."""

from abc import abstractmethod
from typing import Any, Protocol


class IStorage(Protocol):
    """Interface for data storage operations."""

    @abstractmethod
    async def create_user(self, telegram_chat_id: int) -> int:
        """
        Create a new user.

        Args:
            telegram_chat_id: Telegram chat ID

        Returns:
            User ID
        """
        ...

    @abstractmethod
    async def get_user_by_telegram_id(self, telegram_chat_id: int) -> dict[str, Any] | None:
        """
        Get user by Telegram chat ID.

        Args:
            telegram_chat_id: Telegram chat ID

        Returns:
            User dictionary or None if not found
        """
        ...

    @abstractmethod
    async def save_user_config(
        self,
        user_id: int,
        telegram_bot_token: str,
        openai_key: str,
        model_name: str,
        model_base_url: str,
    ) -> None:
        """
        Save user configuration.

        Args:
            user_id: User ID
            telegram_bot_token: Telegram bot token
            openai_key: OpenAI API key
            model_name: LLM model name
            model_base_url: Model base URL
        """
        ...

    @abstractmethod
    async def get_user_config(self, user_id: int) -> dict[str, Any] | None:
        """
        Get user configuration.

        Args:
            user_id: User ID

        Returns:
            User config dictionary or None if not found
        """
        ...

    @abstractmethod
    async def save_user_profile(
        self,
        user_id: int,
        profile_data: dict[str, Any],
    ) -> None:
        """
        Save user profile.

        Args:
            user_id: User ID
            profile_data: Profile data dictionary
        """
        ...

    @abstractmethod
    async def get_user_profile(self, user_id: int) -> dict[str, Any] | None:
        """
        Get user profile.

        Args:
            user_id: User ID

        Returns:
            User profile dictionary or None if not found
        """
        ...

    @abstractmethod
    async def save_resume(
        self,
        user_id: int,
        file_path: str,
        file_type: str,
    ) -> int:
        """
        Save resume file information.

        Args:
            user_id: User ID
            file_path: Path to resume file
            file_type: File type (pdf, docx, etc.)

        Returns:
            Resume ID
        """
        ...

    @abstractmethod
    async def get_resume(self, user_id: int) -> dict[str, Any] | None:
        """
        Get user's resume.

        Args:
            user_id: User ID

        Returns:
            Resume dictionary or None if not found
        """
        ...

    @abstractmethod
    async def save_cover_letter(
        self,
        user_id: int,
        content: str,
        file_path: str | None = None,
    ) -> int:
        """
        Save cover letter.

        Args:
            user_id: User ID
            content: Cover letter content
            file_path: Optional path to cover letter file

        Returns:
            Cover letter ID
        """
        ...

    @abstractmethod
    async def get_cover_letter(self, user_id: int) -> dict[str, Any] | None:
        """
        Get user's cover letter.

        Args:
            user_id: User ID

        Returns:
            Cover letter dictionary or None if not found
        """
        ...

    @abstractmethod
    async def create_job_application(
        self,
        user_id: int,
        job_url: str,
    ) -> int:
        """
        Create a new job application record.

        Args:
            user_id: User ID
            job_url: Job application URL

        Returns:
            Application ID
        """
        ...

    @abstractmethod
    async def update_job_application(
        self,
        application_id: int,
        status: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Update job application status.

        Args:
            application_id: Application ID
            status: Application status
            metadata: Optional metadata dictionary
        """
        ...

    @abstractmethod
    async def get_job_application(self, application_id: int) -> dict[str, Any] | None:
        """
        Get job application by ID.

        Args:
            application_id: Application ID

        Returns:
            Application dictionary or None if not found
        """
        ...

    @abstractmethod
    async def get_user_applications(
        self,
        user_id: int,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Get user's job applications.

        Args:
            user_id: User ID
            limit: Optional limit on number of results

        Returns:
            List of application dictionaries
        """
        ...

    @abstractmethod
    async def add_application_history(
        self,
        application_id: int,
        event_type: str,
        event_data: dict[str, Any],
    ) -> None:
        """
        Add an event to application history.

        Args:
            application_id: Application ID
            event_type: Event type
            event_data: Event data dictionary
        """
        ...

    @abstractmethod
    async def get_application_history(
        self,
        application_id: int,
    ) -> list[dict[str, Any]]:
        """
        Get application history.

        Args:
            application_id: Application ID

        Returns:
            List of history event dictionaries
        """
        ...
