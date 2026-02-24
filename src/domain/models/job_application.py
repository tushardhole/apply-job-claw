"""Job application model."""

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, HttpUrl


class ApplicationStatus(StrEnum):
    """Job application status enum."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    AWAITING_USER_INPUT = "awaiting_user_input"
    AWAITING_OTP = "awaiting_otp"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobApplication(BaseModel):
    """Job application model."""

    application_id: int | None = None
    user_id: int
    job_url: HttpUrl
    status: ApplicationStatus = ApplicationStatus.PENDING
    started_at: datetime
    completed_at: datetime | None = None
    metadata: dict[str, Any] = {}

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "user_id": 1,
                "job_url": "https://company.com/careers/job/123",
                "status": "pending",
                "started_at": "2024-01-15T10:00:00Z",
                "completed_at": None,
                "metadata": {},
            }
        }
