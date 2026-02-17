"""Database schema definitions for SQLite storage."""

from typing import List


class DatabaseSchema:
    """Database schema definitions and migration utilities."""

    @staticmethod
    def get_create_tables_sql() -> List[str]:
        """
        Get SQL statements to create all tables.
        
        Returns:
            List of CREATE TABLE SQL statements
        """
        return [
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_chat_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS user_configs (
                config_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                telegram_bot_token TEXT NOT NULL,
                openai_key TEXT NOT NULL,
                model_name TEXT NOT NULL,
                model_base_url TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                UNIQUE(user_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS user_profiles (
                profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                personal_info TEXT,  -- JSON
                work_authorization TEXT,  -- JSON
                education TEXT,  -- JSON array
                work_experience TEXT,  -- JSON array
                skills TEXT,  -- JSON
                additional_questions TEXT,  -- JSON
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
                UNIQUE(user_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS resumes (
                resume_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                file_path TEXT NOT NULL,
                file_type TEXT NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS cover_letters (
                cover_letter_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                file_path TEXT,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS job_applications (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                job_url TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                metadata TEXT,  -- JSON
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS application_history (
                history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id INTEGER NOT NULL,
                event_type TEXT NOT NULL,
                event_data TEXT,  -- JSON
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (application_id) REFERENCES job_applications(application_id) ON DELETE CASCADE
            )
            """,
        ]

    @staticmethod
    def get_create_indexes_sql() -> List[str]:
        """
        Get SQL statements to create indexes for better query performance.
        
        Returns:
            List of CREATE INDEX SQL statements
        """
        return [
            "CREATE INDEX IF NOT EXISTS idx_users_telegram_chat_id ON users(telegram_chat_id)",
            "CREATE INDEX IF NOT EXISTS idx_user_configs_user_id ON user_configs(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_user_profiles_user_id ON user_profiles(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_resumes_user_id ON resumes(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_cover_letters_user_id ON cover_letters(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_job_applications_user_id ON job_applications(user_id)",
            "CREATE INDEX IF NOT EXISTS idx_job_applications_status ON job_applications(status)",
            "CREATE INDEX IF NOT EXISTS idx_application_history_application_id ON application_history(application_id)",
        ]
