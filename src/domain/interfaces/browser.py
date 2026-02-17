"""Browser automation interface."""

from typing import Protocol, Optional, List, Dict, Any
from abc import abstractmethod


class IBrowserAutomation(Protocol):
    """Interface for browser automation operations."""

    @abstractmethod
    async def navigate(self, url: str) -> None:
        """
        Navigate to a URL.
        
        Args:
            url: URL to navigate to
        """
        ...

    @abstractmethod
    async def get_current_url(self) -> str:
        """
        Get the current page URL.
        
        Returns:
            Current page URL
        """
        ...

    @abstractmethod
    async def get_page_title(self) -> str:
        """
        Get the current page title.
        
        Returns:
            Page title
        """
        ...

    @abstractmethod
    async def find_element(
        self, selector: str, timeout: Optional[float] = None
    ) -> Optional[Any]:
        """
        Find an element by CSS selector or XPath.
        
        Args:
            selector: CSS selector or XPath
            timeout: Optional timeout in seconds
            
        Returns:
            Element if found, None otherwise
        """
        ...

    @abstractmethod
    async def find_elements(
        self, selector: str, timeout: Optional[float] = None
    ) -> List[Any]:
        """
        Find multiple elements by CSS selector or XPath.
        
        Args:
            selector: CSS selector or XPath
            timeout: Optional timeout in seconds
            
        Returns:
            List of elements
        """
        ...

    @abstractmethod
    async def click(self, selector: str, timeout: Optional[float] = None) -> None:
        """
        Click an element.
        
        Args:
            selector: CSS selector or XPath
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def fill(
        self, selector: str, value: str, timeout: Optional[float] = None
    ) -> None:
        """
        Fill an input field.
        
        Args:
            selector: CSS selector or XPath
            value: Value to fill
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def select_option(
        self,
        selector: str,
        value: str,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Select an option from a dropdown.
        
        Args:
            selector: CSS selector or XPath for the select element
            value: Option value to select
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def upload_file(
        self,
        selector: str,
        file_path: str,
        timeout: Optional[float] = None,
    ) -> None:
        """
        Upload a file to a file input.
        
        Args:
            selector: CSS selector or XPath for the file input
            file_path: Path to the file to upload
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def wait_for_element(
        self, selector: str, timeout: Optional[float] = None
    ) -> None:
        """
        Wait for an element to appear.
        
        Args:
            selector: CSS selector or XPath
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def wait_for_navigation(
        self, timeout: Optional[float] = None
    ) -> None:
        """
        Wait for page navigation to complete.
        
        Args:
            timeout: Optional timeout in seconds
        """
        ...

    @abstractmethod
    async def get_text(self, selector: str, timeout: Optional[float] = None) -> str:
        """
        Get text content of an element.
        
        Args:
            selector: CSS selector or XPath
            timeout: Optional timeout in seconds
            
        Returns:
            Text content
        """
        ...

    @abstractmethod
    async def get_attribute(
        self,
        selector: str,
        attribute: str,
        timeout: Optional[float] = None,
    ) -> Optional[str]:
        """
        Get an attribute value of an element.
        
        Args:
            selector: CSS selector or XPath
            attribute: Attribute name
            timeout: Optional timeout in seconds
            
        Returns:
            Attribute value or None
        """
        ...

    @abstractmethod
    async def screenshot(self, path: Optional[str] = None) -> bytes:
        """
        Take a screenshot.
        
        Args:
            path: Optional path to save screenshot
            
        Returns:
            Screenshot bytes
        """
        ...

    @abstractmethod
    async def execute_script(self, script: str) -> Any:
        """
        Execute JavaScript in the browser.
        
        Args:
            script: JavaScript code to execute
            
        Returns:
            Script execution result
        """
        ...

    @abstractmethod
    async def detect_forms(self) -> List[Dict[str, Any]]:
        """
        Detect all forms on the current page.
        
        Returns:
            List of form information dictionaries
        """
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close the browser."""
        ...
