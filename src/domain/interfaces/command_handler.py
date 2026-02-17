"""Command handler interfaces."""

from typing import Protocol, Dict, Any, Callable, Awaitable
from abc import abstractmethod


class ICommandHandler(Protocol):
    """Interface for Telegram command handlers."""

    @abstractmethod
    async def handle(
        self,
        update: Any,
        context: Any,
    ) -> None:
        """
        Handle a command.
        
        Args:
            update: Telegram update object
            context: Telegram context object
        """
        ...

    @property
    @abstractmethod
    def command_name(self) -> str:
        """Get the command name (without leading slash)."""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """Get the command description."""
        ...


class ICommandRegistry(Protocol):
    """Interface for command registration and routing."""

    @abstractmethod
    async def register_command(
        self,
        command: str,
        handler: ICommandHandler,
    ) -> None:
        """
        Register a command handler.
        
        Args:
            command: Command name (without leading slash)
            handler: Command handler instance
        """
        ...

    @abstractmethod
    async def get_handler(self, command: str) -> Optional[ICommandHandler]:
        """
        Get handler for a command.
        
        Args:
            command: Command name (without leading slash)
            
        Returns:
            Command handler or None if not found
        """
        ...

    @abstractmethod
    async def register_all_commands(self, bot: Any) -> None:
        """
        Register all commands with Telegram Bot API.
        
        Args:
            bot: Telegram bot instance
        """
        ...

    @abstractmethod
    def get_all_commands(self) -> list[Dict[str, str]]:
        """
        Get all registered commands for Telegram.
        
        Returns:
            List of command dictionaries with 'command' and 'description' keys
        """
        ...
