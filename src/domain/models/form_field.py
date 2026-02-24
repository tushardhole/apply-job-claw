"""Form field model."""

from enum import StrEnum
from typing import Any, ClassVar

from pydantic import BaseModel


class FieldType(StrEnum):
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

    field_id: str | None = None
    name: str
    field_type: FieldType
    label: str | None = None
    selector: str  # CSS selector or XPath
    value: str | None = None
    required: bool = False
    options: list[str] | None = None  # For select/radio fields
    placeholder: str | None = None
    validation_pattern: str | None = None
    metadata: dict[str, Any] = {}

    class Config:
        """Pydantic config."""

        json_schema_extra: ClassVar[dict[str, Any]] = {
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
