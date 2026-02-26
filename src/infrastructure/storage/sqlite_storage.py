"""SQLite storage implementation."""

import json
from typing import Optional, List, Dict, Any
from datetime import datetime

import aiosqlite

from src.domain.interfaces.storage import IStorage
from src.infrastructure.storage.migrations import MigrationManager


class SQLiteStorage(IStorage):
    """SQLite implementation of IStorage interface."""

    def __init__(self, db_path: str):
        """
        Initialize SQLite storage.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.migration_manager = MigrationManager(db_path)

    async def initialize(self) -> None:
        """Initialize database schema."""
        await self.migration_manager.initialize_database()

    async def create_user(self, telegram_chat_id: int) -> int:
        """Create a new user."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "INSERT INTO users (telegram_chat_id) VALUES (?)",
                (telegram_chat_id,),
            )
            await db.commit()
            return cursor.lastrowid

    async def get_user_by_telegram_id(
        self, telegram_chat_id: int
    ) -> Optional[Dict[str, Any]]:
        """Get user by Telegram chat ID."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM users WHERE telegram_chat_id = ?",
                (telegram_chat_id,),
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None

    async def save_user_config(
        self,
        user_id: int,
        telegram_bot_token: str,
        openai_key: str,
        model_name: str,
        model_base_url: str,
    ) -> None:
        """Save user configuration."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT INTO user_configs 
                (user_id, telegram_bot_token, openai_key, model_name, model_base_url, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    telegram_bot_token = excluded.telegram_bot_token,
                    openai_key = excluded.openai_key,
                    model_name = excluded.model_name,
                    model_base_url = excluded.model_base_url,
                    updated_at = excluded.updated_at
                """,
                (
                    user_id,
                    telegram_bot_token,
                    openai_key,
                    model_name,
                    model_base_url,
                    datetime.now().isoformat(),
                ),
            )
            await db.commit()

    async def get_user_config(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user configuration."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM user_configs WHERE user_id = ?", (user_id,)
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None

    async def save_user_profile(
        self, user_id: int, profile_data: Dict[str, Any]
    ) -> None:
        """Save user profile."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT INTO user_profiles 
                (user_id, personal_info, work_authorization, education, 
                 work_experience, skills, additional_questions, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    personal_info = excluded.personal_info,
                    work_authorization = excluded.work_authorization,
                    education = excluded.education,
                    work_experience = excluded.work_experience,
                    skills = excluded.skills,
                    additional_questions = excluded.additional_questions,
                    updated_at = excluded.updated_at
                """,
                (
                    user_id,
                    json.dumps(profile_data.get("personal_info")),
                    json.dumps(profile_data.get("work_authorization")),
                    json.dumps(profile_data.get("education", [])),
                    json.dumps(profile_data.get("work_experience", [])),
                    json.dumps(profile_data.get("skills")),
                    json.dumps(profile_data.get("additional_questions", {})),
                    datetime.now().isoformat(),
                ),
            )
            await db.commit()

    async def get_user_profile(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user profile."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM user_profiles WHERE user_id = ?", (user_id,)
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    data = dict(row)
                    # Parse JSON fields
                    for field in [
                        "personal_info",
                        "work_authorization",
                        "education",
                        "work_experience",
                        "skills",
                        "additional_questions",
                    ]:
                        if data.get(field):
                            data[field] = json.loads(data[field])
                        elif field in ["education", "work_experience", "additional_questions"]:
                            data[field] = [] if field != "additional_questions" else {}
                    return data
                return None

    async def save_resume(
        self, user_id: int, file_path: str, file_type: str
    ) -> int:
        """Save resume file information."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "INSERT INTO resumes (user_id, file_path, file_type) VALUES (?, ?, ?)",
                (user_id, file_path, file_type),
            )
            await db.commit()
            return cursor.lastrowid

    async def get_resume(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user's resume."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM resumes WHERE user_id = ? ORDER BY uploaded_at DESC LIMIT 1",
                (user_id,),
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None

    async def save_cover_letter(
        self, user_id: int, content: str, file_path: Optional[str] = None
    ) -> int:
        """Save cover letter."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "INSERT INTO cover_letters (user_id, content, file_path) VALUES (?, ?, ?)",
                (user_id, content, file_path),
            )
            await db.commit()
            return cursor.lastrowid

    async def get_cover_letter(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get user's cover letter."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM cover_letters WHERE user_id = ? ORDER BY uploaded_at DESC LIMIT 1",
                (user_id,),
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
                return None

    async def create_job_application(self, user_id: int, job_url: str) -> int:
        """Create a new job application record."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "INSERT INTO job_applications (user_id, job_url) VALUES (?, ?)",
                (user_id, job_url),
            )
            await db.commit()
            application_id = cursor.lastrowid
            
            # Add initial history entry
            await self.add_application_history(
                application_id, "created", {"job_url": job_url}
            )
            
            return application_id

    async def update_job_application(
        self,
        application_id: int,
        status: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Update job application status."""
        async with aiosqlite.connect(self.db_path) as db:
            completed_at = (
                datetime.now().isoformat() if status == "completed" else None
            )
            await db.execute(
                """
                UPDATE job_applications 
                SET status = ?, metadata = ?, completed_at = ?
                WHERE application_id = ?
                """,
                (
                    status,
                    json.dumps(metadata) if metadata else None,
                    completed_at,
                    application_id,
                ),
            )
            await db.commit()

    async def get_job_application(
        self, application_id: int
    ) -> Optional[Dict[str, Any]]:
        """Get job application by ID."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM job_applications WHERE application_id = ?",
                (application_id,),
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    data = dict(row)
                    if data.get("metadata"):
                        data["metadata"] = json.loads(data["metadata"])
                    return data
                return None

    async def get_user_applications(
        self, user_id: int, limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Get user's job applications."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            query = "SELECT * FROM job_applications WHERE user_id = ? ORDER BY started_at DESC"
            if limit:
                query += f" LIMIT {limit}"
            
            async with db.execute(query, (user_id,)) as cursor:
                rows = await cursor.fetchall()
                applications = []
                for row in rows:
                    data = dict(row)
                    if data.get("metadata"):
                        data["metadata"] = json.loads(data["metadata"])
                    applications.append(data)
                return applications

    async def add_application_history(
        self,
        application_id: int,
        event_type: str,
        event_data: Dict[str, Any],
    ) -> None:
        """Add an event to application history."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "INSERT INTO application_history (application_id, event_type, event_data) VALUES (?, ?, ?)",
                (application_id, event_type, json.dumps(event_data)),
            )
            await db.commit()

    async def get_application_history(
        self, application_id: int
    ) -> List[Dict[str, Any]]:
        """Get application history."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM application_history WHERE application_id = ? ORDER BY timestamp ASC",
                (application_id,),
            ) as cursor:
                rows = await cursor.fetchall()
                history = []
                for row in rows:
                    data = dict(row)
                    if data.get("event_data"):
                        data["event_data"] = json.loads(data["event_data"])
                    history.append(data)
                return history
