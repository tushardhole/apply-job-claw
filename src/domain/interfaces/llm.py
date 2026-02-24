"""LLM client interface."""

from abc import abstractmethod
from typing import Any, Protocol


class ILLMClient(Protocol):
    """Interface for LLM API operations."""

    @abstractmethod
    async def chat_completion(
        self,
        messages: list[dict[str, str]],
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        tools: list[dict[str, Any]] | None = None,
        tool_choice: str | None = None,
    ) -> dict[str, Any]:
        """
        Create a chat completion.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Optional model name override
            temperature: Optional temperature setting
            max_tokens: Optional maximum tokens
            tools: Optional list of tool definitions for function calling
            tool_choice: Optional tool choice mode ('auto', 'none', or tool dict)

        Returns:
            Completion response dictionary
        """
        ...

    @abstractmethod
    async def extract_structured_data(
        self,
        text: str,
        schema: dict[str, Any],
        model: str | None = None,
    ) -> dict[str, Any]:
        """
        Extract structured data from text using LLM.

        Args:
            text: Input text to extract data from
            schema: JSON schema describing the desired output structure
            model: Optional model name override

        Returns:
            Extracted structured data dictionary
        """
        ...

    @abstractmethod
    async def generate_text(
        self,
        prompt: str,
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        """
        Generate text from a prompt.

        Args:
            prompt: Input prompt
            model: Optional model name override
            temperature: Optional temperature setting
            max_tokens: Optional maximum tokens

        Returns:
            Generated text
        """
        ...
