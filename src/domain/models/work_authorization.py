"""Work authorization model."""

from datetime import date

from pydantic import BaseModel


class WorkAuthorization(BaseModel):
    """Work authorization model."""

    status: str  # e.g., "Authorized to work in US", "Require sponsorship", etc.
    visa_type: str | None = None  # e.g., "H1B", "Green Card", "Citizen", etc.
    start_date_availability: date | None = None
    requires_sponsorship: bool = False

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "status": "Authorized to work in US",
                "visa_type": "Green Card",
                "start_date_availability": "2024-03-01",
                "requires_sponsorship": False,
            }
        }
