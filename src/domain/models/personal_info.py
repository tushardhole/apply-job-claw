"""Personal information model."""

from typing import Optional
from pydantic import BaseModel, EmailStr, HttpUrl


class PersonalInfo(BaseModel):
    """Personal information model."""

    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    address_street: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_zip: Optional[str] = None
    address_country: Optional[str] = None
    linkedin_url: Optional[HttpUrl] = None
    portfolio_url: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "+1234567890",
                "address_street": "123 Main St",
                "address_city": "San Francisco",
                "address_state": "CA",
                "address_zip": "94102",
                "address_country": "USA",
                "linkedin_url": "https://linkedin.com/in/johndoe",
                "portfolio_url": "https://johndoe.dev",
                "github_url": "https://github.com/johndoe",
            }
        }
