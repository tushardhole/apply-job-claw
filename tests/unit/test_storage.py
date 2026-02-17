"""Unit tests for SQLiteStorage."""

import pytest
import tempfile
import os
from datetime import datetime

from src.infrastructure.storage.sqlite_storage import SQLiteStorage


@pytest.fixture
async def storage():
    """Create a temporary storage instance for testing."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
        db_path = tmp.name
    
    storage = SQLiteStorage(db_path)
    await storage.initialize()
    
    yield storage
    
    # Cleanup
    if os.path.exists(db_path):
        os.unlink(db_path)


@pytest.mark.asyncio
async def test_create_user(storage):
    """Test creating a user."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    assert user_id is not None
    assert isinstance(user_id, int)


@pytest.mark.asyncio
async def test_get_user_by_telegram_id(storage):
    """Test getting user by Telegram chat ID."""
    # Create user
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    # Get user
    user = await storage.get_user_by_telegram_id(telegram_chat_id=12345)
    assert user is not None
    assert user["user_id"] == user_id
    assert user["telegram_chat_id"] == 12345


@pytest.mark.asyncio
async def test_get_user_by_telegram_id_not_found(storage):
    """Test getting non-existent user."""
    user = await storage.get_user_by_telegram_id(telegram_chat_id=99999)
    assert user is None


@pytest.mark.asyncio
async def test_save_and_get_user_config(storage):
    """Test saving and retrieving user config."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    await storage.save_user_config(
        user_id=user_id,
        telegram_bot_token="test_token",
        openai_key="test_key",
        model_name="gpt-4",
        model_base_url="https://api.openai.com/v1",
    )
    
    config = await storage.get_user_config(user_id=user_id)
    assert config is not None
    assert config["telegram_bot_token"] == "test_token"
    assert config["openai_key"] == "test_key"
    assert config["model_name"] == "gpt-4"
    assert config["model_base_url"] == "https://api.openai.com/v1"


@pytest.mark.asyncio
async def test_update_user_config(storage):
    """Test updating existing user config."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    # Save initial config
    await storage.save_user_config(
        user_id=user_id,
        telegram_bot_token="old_token",
        openai_key="old_key",
        model_name="gpt-3.5",
        model_base_url="https://api.openai.com/v1",
    )
    
    # Update config
    await storage.save_user_config(
        user_id=user_id,
        telegram_bot_token="new_token",
        openai_key="new_key",
        model_name="gpt-4",
        model_base_url="https://api.openai.com/v1",
    )
    
    config = await storage.get_user_config(user_id=user_id)
    assert config["telegram_bot_token"] == "new_token"
    assert config["model_name"] == "gpt-4"


@pytest.mark.asyncio
async def test_save_and_get_user_profile(storage):
    """Test saving and retrieving user profile."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    profile_data = {
        "personal_info": {"name": "John Doe", "email": "john@example.com"},
        "work_authorization": {"status": "Authorized"},
        "education": [{"degree": "BS", "school": "University"}],
        "work_experience": [{"title": "Engineer", "company": "Tech Corp"}],
        "skills": {"languages": ["Python", "JavaScript"]},
        "additional_questions": {"salary": "100k"},
    }
    
    await storage.save_user_profile(user_id=user_id, profile_data=profile_data)
    
    profile = await storage.get_user_profile(user_id=user_id)
    assert profile is not None
    assert profile["personal_info"]["name"] == "John Doe"
    assert len(profile["education"]) == 1
    assert len(profile["work_experience"]) == 1


@pytest.mark.asyncio
async def test_save_and_get_resume(storage):
    """Test saving and retrieving resume."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    resume_id = await storage.save_resume(
        user_id=user_id, file_path="/path/to/resume.pdf", file_type="pdf"
    )
    assert resume_id is not None
    
    resume = await storage.get_resume(user_id=user_id)
    assert resume is not None
    assert resume["file_path"] == "/path/to/resume.pdf"
    assert resume["file_type"] == "pdf"


@pytest.mark.asyncio
async def test_save_and_get_cover_letter(storage):
    """Test saving and retrieving cover letter."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    cover_letter_id = await storage.save_cover_letter(
        user_id=user_id, content="Cover letter content", file_path="/path/to/cover.txt"
    )
    assert cover_letter_id is not None
    
    cover_letter = await storage.get_cover_letter(user_id=user_id)
    assert cover_letter is not None
    assert cover_letter["content"] == "Cover letter content"
    assert cover_letter["file_path"] == "/path/to/cover.txt"


@pytest.mark.asyncio
async def test_create_job_application(storage):
    """Test creating a job application."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    application_id = await storage.create_job_application(
        user_id=user_id, job_url="https://example.com/job/123"
    )
    assert application_id is not None
    
    application = await storage.get_job_application(application_id=application_id)
    assert application is not None
    assert application["job_url"] == "https://example.com/job/123"
    assert application["status"] == "pending"


@pytest.mark.asyncio
async def test_update_job_application(storage):
    """Test updating job application status."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    application_id = await storage.create_job_application(
        user_id=user_id, job_url="https://example.com/job/123"
    )
    
    await storage.update_job_application(
        application_id=application_id,
        status="completed",
        metadata={"notes": "Successfully applied"},
    )
    
    application = await storage.get_job_application(application_id=application_id)
    assert application["status"] == "completed"
    assert application["metadata"]["notes"] == "Successfully applied"
    assert application["completed_at"] is not None


@pytest.mark.asyncio
async def test_get_user_applications(storage):
    """Test getting user's job applications."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    
    # Create multiple applications
    app1_id = await storage.create_job_application(
        user_id=user_id, job_url="https://example.com/job/1"
    )
    app2_id = await storage.create_job_application(
        user_id=user_id, job_url="https://example.com/job/2"
    )
    
    applications = await storage.get_user_applications(user_id=user_id)
    assert len(applications) == 2
    
    # Test with limit
    applications_limited = await storage.get_user_applications(
        user_id=user_id, limit=1
    )
    assert len(applications_limited) == 1


@pytest.mark.asyncio
async def test_application_history(storage):
    """Test application history tracking."""
    user_id = await storage.create_user(telegram_chat_id=12345)
    application_id = await storage.create_job_application(
        user_id=user_id, job_url="https://example.com/job/123"
    )
    
    # Add history entries
    await storage.add_application_history(
        application_id=application_id,
        event_type="form_filled",
        event_data={"field_count": 10},
    )
    await storage.add_application_history(
        application_id=application_id,
        event_type="submitted",
        event_data={"timestamp": datetime.now().isoformat()},
    )
    
    history = await storage.get_application_history(application_id=application_id)
    assert len(history) >= 3  # At least created + 2 custom events
    assert any(event["event_type"] == "created" for event in history)
    assert any(event["event_type"] == "form_filled" for event in history)
    assert any(event["event_type"] == "submitted" for event in history)
