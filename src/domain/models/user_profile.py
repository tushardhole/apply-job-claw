"""User profile model."""

from typing import Optional, List, Dict
from pydantic import BaseModel

from .personal_info import PersonalInfo
from .work_authorization import WorkAuthorization
from .education import Education
from .work_experience import WorkExperience
from .skills import Skills


class UserProfile(BaseModel):
    """Complete user profile model."""

    personal_info: PersonalInfo
    work_authorization: WorkAuthorization
    education: List[Education] = []
    work_experience: List[WorkExperience] = []
    skills: Skills
    additional_questions: Dict[str, str] = {}
    resume_path: Optional[str] = None
    cover_letter_path: Optional[str] = None

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
