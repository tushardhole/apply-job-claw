"""Domain models."""

from .education import Education
from .form_field import FieldType, FormField
from .job_application import ApplicationStatus, JobApplication
from .personal_info import PersonalInfo
from .skills import Skills
from .user_config import UserConfig
from .user_profile import UserProfile
from .work_authorization import WorkAuthorization
from .work_experience import WorkExperience

__all__ = [
    "PersonalInfo",
    "WorkAuthorization",
    "Education",
    "WorkExperience",
    "Skills",
    "UserConfig",
    "UserProfile",
    "JobApplication",
    "ApplicationStatus",
    "FormField",
    "FieldType",
]
