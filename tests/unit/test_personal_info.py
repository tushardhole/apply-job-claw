"""Unit tests for PersonalInfo model."""

import pytest
from pydantic import ValidationError

from src.domain.models.personal_info import PersonalInfo


def test_personal_info_creation():
    """Test creating a PersonalInfo instance with required fields."""
    info = PersonalInfo(
        full_name="John Doe",
        email="john.doe@example.com",
    )
    assert info.full_name == "John Doe"
    assert info.email == "john.doe@example.com"


def test_personal_info_with_all_fields():
    """Test creating a PersonalInfo instance with all fields."""
    info = PersonalInfo(
        full_name="John Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        address_street="123 Main St",
        address_city="San Francisco",
        address_state="CA",
        address_zip="94102",
        address_country="USA",
        linkedin_url="https://linkedin.com/in/johndoe",
        portfolio_url="https://johndoe.dev",
        github_url="https://github.com/johndoe",
    )
    assert info.full_name == "John Doe"
    assert info.phone == "+1234567890"
    assert info.address_city == "San Francisco"


def test_personal_info_invalid_email():
    """Test that invalid email raises ValidationError."""
    with pytest.raises(ValidationError):
        PersonalInfo(
            full_name="John Doe",
            email="invalid-email",
        )


def test_personal_info_invalid_url():
    """Test that invalid URL raises ValidationError."""
    with pytest.raises(ValidationError):
        PersonalInfo(
            full_name="John Doe",
            email="john.doe@example.com",
            linkedin_url="not-a-url",
        )
