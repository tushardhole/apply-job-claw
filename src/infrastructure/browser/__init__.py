"""Browser infrastructure package."""

from .form_detector import FormDetector
from .playwright_browser import PlaywrightBrowser

__all__ = ["PlaywrightBrowser", "FormDetector"]
