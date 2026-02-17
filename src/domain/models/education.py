"""Education model."""

from typing import Optional
from datetime import date
from pydantic import BaseModel


class Education(BaseModel):
    """Education entry model."""

    degree: str  # e.g., "Bachelor of Science", "Master of Science", etc.
    field_of_study: Optional[str] = None
    institution: str
    location: Optional[str] = None
    graduation_date: Optional[date] = None
    gpa: Optional[float] = None
    honors: Optional[str] = None

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "degree": "Bachelor of Science",
                "field_of_study": "Computer Science",
                "institution": "University of California",
                "location": "Berkeley, CA",
                "graduation_date": "2020-05-15",
                "gpa": 3.8,
                "honors": "Magna Cum Laude",
            }
        }
