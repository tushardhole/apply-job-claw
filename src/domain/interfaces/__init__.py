"""Domain interfaces."""

from .browser import IBrowserAutomation
from .command_handler import ICommandHandler, ICommandRegistry
from .handlers import (
    IAuthenticationHandler,
    IFormFiller,
    IJobApplicationHandler,
    IOTPHandler,
)
from .llm import ILLMClient
from .resume_parser import IResumeParser
from .storage import IStorage
from .telegram import ITelegramBot

__all__ = [
    "IBrowserAutomation",
    "ITelegramBot",
    "ILLMClient",
    "IStorage",
    "IResumeParser",
    "IJobApplicationHandler",
    "IFormFiller",
    "IAuthenticationHandler",
    "IOTPHandler",
    "ICommandHandler",
    "ICommandRegistry",
]
