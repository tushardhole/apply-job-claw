"""Form field model."""

from typing import Optional, List, Dict, Any, ClassVar
from enum import Enum
from pydantic import BaseModel


class FieldType(str, Enum):
    """Form field type enum."""

    TEXT = "text"
    EMAIL = "email"
    PHONE = "tel"
    NUMBER = "number"
    TEXTAREA = "textarea"
    SELECT = "select"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    FILE = "file"
    DATE = "date"
    URL = "url"
    PASSWORD = "password"
    HIDDEN = "hidden"


class FormField(BaseModel):
    """Form field model."""

    field_id: Optional[str] = None
    name: str
    field_type: FieldType
    label: Optional[str] = None
    selector: str  # CSS selector or XPath
    value: Optional[str] = None
    required: bool = False
    options: Optional[List[str]] = None  # For select/radio fields
    placeholder: Optional[str] = None
    validation_pattern: Optional[str] = None
    metadata: Dict[str, Any] = {}

    class Config:
        """Pydantic config."""

        json_schema_extra: ClassVar[Dict[str, Any]] = {
            "example": {
                "name": "email",
                "field_type": "email",
                "label": "Email Address",
                "selector": "#email",
                "value": None,
                "required": True,
                "options": None,
                "placeholder": "Enter your email",
                "validation_pattern": None,
                "metadata": {},
            }
        }
