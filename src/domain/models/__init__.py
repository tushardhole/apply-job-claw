"""Domain models."""

from .personal_info import PersonalInfo
from .work_authorization import WorkAuthorization
from .education import Education
from .work_experience import WorkExperience
from .skills import Skills
from .user_config import UserConfig
from .user_profile import UserProfile
from .job_application import JobApplication, ApplicationStatus
from .form_field import FormField, FieldType

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
