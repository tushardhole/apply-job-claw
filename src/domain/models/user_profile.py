"""User profile model."""


from pydantic import BaseModel

from .education import Education
from .personal_info import PersonalInfo
from .skills import Skills
from .work_authorization import WorkAuthorization
from .work_experience import WorkExperience


class UserProfile(BaseModel):
    """Complete user profile model."""

    personal_info: PersonalInfo
    work_authorization: WorkAuthorization
    education: list[Education] = []
    work_experience: list[WorkExperience] = []
    skills: Skills
    additional_questions: dict[str, str] = {}
    resume_path: str | None = None
    cover_letter_path: str | None = None

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "personal_info": {
                    "full_name": "John Doe",
                    "email": "john.doe@example.com",
                },
                "work_authorization": {
                    "status": "Authorized to work in US",
                },
                "education": [],
                "work_experience": [],
                "skills": {
                    "technical_skills": [],
                },
                "additional_questions": {},
                "resume_path": "/path/to/resume.pdf",
                "cover_letter_path": "/path/to/cover_letter.txt",
            }
        }
