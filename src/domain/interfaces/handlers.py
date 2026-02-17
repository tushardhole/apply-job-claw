"""Handler interfaces for job application flow."""

from typing import Protocol, Optional, List, Dict, Any
from abc import abstractmethod


class IJobApplicationHandler(Protocol):
    """Interface for job application orchestration."""

    @abstractmethod
    async def start_application(
        self,
        user_id: int,
        job_url: str,
    ) -> int:
        """
        Start a new job application process.
        
        Args:
            user_id: User ID
            job_url: Job application URL
            
        Returns:
            Application ID
        """
        ...

    @abstractmethod
    async def process_application(
        self,
        application_id: int,
    ) -> Dict[str, Any]:
        """
        Process a job application (main orchestration method).
        
        Args:
            application_id: Application ID
            
        Returns:
            Status dictionary with application state
        """
        ...

    @abstractmethod
    async def handle_user_response(
        self,
        application_id: int,
        response: str,
    ) -> Dict[str, Any]:
        """
        Handle user response to a question.
        
        Args:
            application_id: Application ID
            response: User's response text
            
        Returns:
            Status dictionary
        """
        ...

    @abstractmethod
    async def handle_otp(
        self,
        application_id: int,
        otp_code: str,
    ) -> Dict[str, Any]:
        """
        Handle OTP code from user.
        
        Args:
            application_id: Application ID
            otp_code: OTP code
            
        Returns:
            Status dictionary
        """
        ...

    @abstractmethod
    async def cancel_application(self, application_id: int) -> None:
        """
        Cancel an ongoing application.
        
        Args:
            application_id: Application ID
        """
        ...


class IFormFiller(Protocol):
    """Interface for form filling operations."""

    @abstractmethod
    async def detect_form_fields(self) -> List[Dict[str, Any]]:
        """
        Detect all form fields on the current page.
        
        Returns:
            List of form field dictionaries with type, name, selector, etc.
        """
        ...

    @abstractmethod
    async def fill_field(
        self,
        field_info: Dict[str, Any],
        value: str,
    ) -> None:
        """
        Fill a single form field.
        
        Args:
            field_info: Field information dictionary
            value: Value to fill
        """
        ...

    @abstractmethod
    async def fill_form(
        self,
        form_data: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """
        Fill an entire form with provided data.
        
        Args:
            form_data: Dictionary mapping field names to values
            
        Returns:
            List of fields that couldn't be filled automatically
        """
        ...

    @abstractmethod
    async def submit_form(self) -> bool:
        """
        Submit the current form.
        
        Returns:
            True if submission successful, False otherwise
        """
        ...


class IAuthenticationHandler(Protocol):
    """Interface for authentication operations."""

    @abstractmethod
    async def detect_login_required(self) -> bool:
        """
        Detect if login is required on the current page.
        
        Returns:
            True if login is required, False otherwise
        """
        ...

    @abstractmethod
    async def perform_login(
        self,
        credentials: Dict[str, str],
    ) -> bool:
        """
        Perform login with provided credentials.
        
        Args:
            credentials: Dictionary with username/email and password
            
        Returns:
            True if login successful, False otherwise
        """
        ...

    @abstractmethod
    async def detect_otp_required(self) -> bool:
        """
        Detect if OTP verification is required.
        
        Returns:
            True if OTP required, False otherwise
        """
        ...

    @abstractmethod
    async def submit_otp(self, otp_code: str) -> bool:
        """
        Submit OTP code for verification.
        
        Args:
            otp_code: OTP code
            
        Returns:
            True if OTP accepted, False otherwise
        """
        ...


class IOTPHandler(Protocol):
    """Interface for OTP handling operations."""

    @abstractmethod
    async def request_otp_from_user(
        self,
        user_id: int,
        application_id: int,
        message: str,
    ) -> None:
        """
        Request OTP code from user via Telegram.
        
        Args:
            user_id: User ID
            application_id: Application ID
            message: Message to send to user
        """
        ...

    @abstractmethod
    async def wait_for_otp(
        self,
        application_id: int,
        timeout: Optional[float] = None,
    ) -> Optional[str]:
        """
        Wait for OTP code from user.
        
        Args:
            application_id: Application ID
            timeout: Optional timeout in seconds
            
        Returns:
            OTP code or None if timeout
        """
        ...
