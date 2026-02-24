"""Education model."""

from datetime import date

from pydantic import BaseModel


class Education(BaseModel):
    """Education entry model."""

    degree: str  # e.g., "Bachelor of Science", "Master of Science", etc.
    field_of_study: str | None = None
    institution: str
    location: str | None = None
    graduation_date: date | None = None
    gpa: float | None = None
    honors: str | None = None

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
