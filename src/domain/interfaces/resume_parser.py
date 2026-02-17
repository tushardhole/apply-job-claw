"""Resume parser interface."""

from typing import Protocol, Dict, Any
from abc import abstractmethod


class IResumeParser(Protocol):
    """Interface for resume parsing operations."""

    @abstractmethod
    async def parse(self, file_path: str) -> Dict[str, Any]:
        """
        Parse a resume file and extract structured data.
        
        Args:
            file_path: Path to the resume file (PDF or DOCX)
            
        Returns:
            Dictionary containing parsed resume data:
            - personal_info: Dict with name, email, phone, address, etc.
            - work_authorization: Dict with authorization status
            - education: List of education entries
            - work_experience: List of work experience entries
            - skills: Dict with technical skills, languages, certifications
        """
        ...

    @abstractmethod
    async def extract_personal_info(self, file_path: str) -> Dict[str, Any]:
        """
        Extract personal information from resume.
        
        Args:
            file_path: Path to the resume file
            
        Returns:
            Dictionary with personal info (name, email, phone, address, etc.)
        """
        ...

    @abstractmethod
    async def extract_education(self, file_path: str) -> list[Dict[str, Any]]:
        """
        Extract education history from resume.
        
        Args:
            file_path: Path to the resume file
            
        Returns:
            List of education dictionaries
        """
        ...

    @abstractmethod
    async def extract_work_experience(self, file_path: str) -> list[Dict[str, Any]]:
        """
        Extract work experience from resume.
        
        Args:
            file_path: Path to the resume file
            
        Returns:
            List of work experience dictionaries
        """
        ...

    @abstractmethod
    async def extract_skills(self, file_path: str) -> Dict[str, Any]:
        """
        Extract skills and certifications from resume.
        
        Args:
            file_path: Path to the resume file
            
        Returns:
            Dictionary with skills, languages, certifications
        """
        ...
