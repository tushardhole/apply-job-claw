"""Personal information model."""


from pydantic import BaseModel, EmailStr, HttpUrl


class PersonalInfo(BaseModel):
    """Personal information model."""

    full_name: str
    email: EmailStr
    phone: str | None = None
    address_street: str | None = None
    address_city: str | None = None
    address_state: str | None = None
    address_zip: str | None = None
    address_country: str | None = None
    linkedin_url: HttpUrl | None = None
    portfolio_url: HttpUrl | None = None
    github_url: HttpUrl | None = None

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
