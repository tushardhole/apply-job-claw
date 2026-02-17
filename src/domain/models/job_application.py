"""Job application model."""

from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, HttpUrl


class ApplicationStatus(str, Enum):
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

    application_id: Optional[int] = None
    user_id: int
    job_url: HttpUrl
    status: ApplicationStatus = ApplicationStatus.PENDING
    started_at: datetime
    completed_at: Optional[datetime] = None
    metadata: Dict[str, Any] = {}

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
