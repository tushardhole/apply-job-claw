"""Skills model."""

from typing import Optional, List
from pydantic import BaseModel


class Skills(BaseModel):
    """Skills and certifications model."""

    technical_skills: List[str] = []
    programming_languages: List[str] = []
    frameworks: List[str] = []
    tools: List[str] = []
    languages: List[str] = []  # Human languages
    certifications: List[str] = []

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "technical_skills": [
                    "Software Development",
                    "System Design",
                    "Cloud Architecture",
                ],
                "programming_languages": ["Python", "JavaScript", "Go"],
                "frameworks": ["Django", "React", "FastAPI"],
                "tools": ["Docker", "Kubernetes", "AWS", "Git"],
                "languages": ["English", "Spanish"],
                "certifications": [
                    "AWS Certified Solutions Architect",
                    "Kubernetes Administrator",
                ],
            }
        }
