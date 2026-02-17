"""Unit tests for UserConfig model."""

import pytest
from pydantic import ValidationError

from src.domain.models.user_config import UserConfig


def test_user_config_creation():
    """Test creating a UserConfig instance."""
    config = UserConfig(
        telegram_bot_token="123456:ABC-DEF1234ghIkl",
        openai_key="sk-test123",
        model_name="gpt-4",
        model_base_url="https://api.openai.com/v1",
    )
    assert config.model_name == "gpt-4"
    assert config.model_base_url == "https://api.openai.com/v1"
    # SecretStr values are accessed via .get_secret_value()
    assert config.telegram_bot_token.get_secret_value() == "123456:ABC-DEF1234ghIkl"
    assert config.openai_key.get_secret_value() == "sk-test123"


def test_user_config_missing_fields():
    """Test that missing required fields raise ValidationError."""
    with pytest.raises(ValidationError):
        UserConfig(
            telegram_bot_token="123456:ABC-DEF1234ghIkl",
            # Missing other required fields
        )


def test_user_config_secret_str():
    """Test that sensitive fields are stored as SecretStr."""
    config = UserConfig(
        telegram_bot_token="secret-token",
        openai_key="secret-key",
        model_name="gpt-4",
        model_base_url="https://api.openai.com/v1",
    )
    # SecretStr doesn't expose value in repr
    assert "secret-token" not in str(config)
    assert "secret-key" not in str(config)
    # But we can get the value explicitly
    assert config.telegram_bot_token.get_secret_value() == "secret-token"
