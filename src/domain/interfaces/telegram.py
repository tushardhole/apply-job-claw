"""Telegram bot interface."""

from typing import Protocol, Optional, List, Dict, Any, Callable, Awaitable
from abc import abstractmethod


class ITelegramBot(Protocol):
    """Interface for Telegram bot operations."""

    @abstractmethod
    async def send_message(
        self,
        chat_id: int,
        text: str,
        reply_to_message_id: Optional[int] = None,
        parse_mode: Optional[str] = None,
    ) -> None:
        """
        Send a text message to a chat.
        
        Args:
            chat_id: Chat ID to send message to
            text: Message text
            reply_to_message_id: Optional message ID to reply to
            parse_mode: Optional parse mode (HTML, Markdown, etc.)
        """
        ...

    @abstractmethod
    async def send_document(
        self,
        chat_id: int,
        document_path: str,
        caption: Optional[str] = None,
    ) -> None:
        """
        Send a document/file to a chat.
        
        Args:
            chat_id: Chat ID to send document to
            document_path: Path to the document file
            caption: Optional caption for the document
        """
        ...

    @abstractmethod
    async def send_photo(
        self,
        chat_id: int,
        photo_path: str,
        caption: Optional[str] = None,
    ) -> None:
        """
        Send a photo to a chat.
        
        Args:
            chat_id: Chat ID to send photo to
            photo_path: Path to the photo file
            caption: Optional caption for the photo
        """
        ...

    @abstractmethod
    async def register_command(
        self,
        command: str,
        description: str,
        handler: Callable[[Any, Any], Awaitable[None]],
    ) -> None:
        """
        Register a bot command.
        
        Args:
            command: Command name (without leading slash)
            description: Command description
            handler: Async handler function for the command
        """
        ...

    @abstractmethod
    async def set_commands(self, commands: List[Dict[str, str]]) -> None:
        """
        Set bot commands list for Telegram.
        
        Args:
            commands: List of command dictionaries with 'command' and 'description' keys
        """
        ...

    @abstractmethod
    async def wait_for_message(
        self,
        chat_id: int,
        timeout: Optional[float] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Wait for a message from a specific chat.
        
        Args:
            chat_id: Chat ID to wait for message from
            timeout: Optional timeout in seconds
            
        Returns:
            Message dictionary or None if timeout
        """
        ...

    @abstractmethod
    async def start_polling(self) -> None:
        """Start the bot polling loop."""
        ...

    @abstractmethod
    async def stop_polling(self) -> None:
        """Stop the bot polling loop."""
        ...

    @abstractmethod
    async def get_chat_id(self, user_id: int) -> Optional[int]:
        """
        Get chat ID for a user.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            Chat ID or None if not found
        """
        ...
