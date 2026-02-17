"""Work experience model."""

from typing import Optional, List
from datetime import date
from pydantic import BaseModel


class WorkExperience(BaseModel):
    """Work experience entry model."""

    title: str
    company: str
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    current: bool = False
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    technologies: Optional[List[str]] = None

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "title": "Senior Software Engineer",
                "company": "Tech Corp",
                "location": "San Francisco, CA",
                "start_date": "2020-06-01",
                "end_date": None,
                "current": True,
                "description": "Led development of microservices architecture",
                "achievements": [
                    "Reduced API response time by 50%",
                    "Mentored 3 junior engineers",
                ],
                "technologies": ["Python", "Docker", "Kubernetes"],
            }
        }
