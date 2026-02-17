"""User configuration model."""

from pydantic import BaseModel, SecretStr


class UserConfig(BaseModel):
    """User configuration model for API keys and LLM settings."""

    telegram_bot_token: SecretStr
    openai_key: SecretStr
    model_name: str
    model_base_url: str

    class Config:
        """Pydantic config."""

        json_schema_extra = {
            "example": {
                "telegram_bot_token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
                "openai_key": "sk-...",
                "model_name": "gpt-4",
                "model_base_url": "https://api.openai.com/v1",
            }
        }
