"""Skills model."""

from pydantic import BaseModel


class Skills(BaseModel):
    """Skills and certifications model."""

    technical_skills: list[str] = []
    programming_languages: list[str] = []
    frameworks: list[str] = []
    tools: list[str] = []
    languages: list[str] = []  # Human languages
    certifications: list[str] = []

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
