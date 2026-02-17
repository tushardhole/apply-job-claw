"""LLM client interface."""

from typing import Protocol, Optional, List, Dict, Any
from abc import abstractmethod


class ILLMClient(Protocol):
    """Interface for LLM API operations."""

    @abstractmethod
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[str] = None,
    ) -> Dict[str, Any]:
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
        schema: Dict[str, Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
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
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
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
