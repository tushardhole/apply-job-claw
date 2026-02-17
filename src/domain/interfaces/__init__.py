"""Domain interfaces."""

from .browser import IBrowserAutomation
from .telegram import ITelegramBot
from .llm import ILLMClient
from .storage import IStorage
from .resume_parser import IResumeParser
from .handlers import (
    IJobApplicationHandler,
    IFormFiller,
    IAuthenticationHandler,
    IOTPHandler,
)
from .command_handler import ICommandHandler, ICommandRegistry

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
