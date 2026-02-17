"""Database migration utilities."""

import json
from typing import Optional
from datetime import datetime

import aiosqlite

from src.infrastructure.storage.schema import DatabaseSchema


class MigrationManager:
    """Manages database migrations."""

    def __init__(self, db_path: str):
        """
        Initialize migration manager.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path

    async def initialize_database(self) -> None:
        """
        Initialize database with all tables and indexes.
        
        This creates the database file if it doesn't exist and sets up
        all required tables and indexes.
        """
        async with aiosqlite.connect(self.db_path) as db:
            # Create all tables
            for sql in DatabaseSchema.get_create_tables_sql():
                await db.execute(sql)
            
            # Create all indexes
            for sql in DatabaseSchema.get_create_indexes_sql():
                await db.execute(sql)
            
            # Create migrations table to track schema version
            await db.execute("""
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    version INTEGER PRIMARY KEY,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Record initial migration
            await db.execute("""
                INSERT OR IGNORE INTO schema_migrations (version) VALUES (1)
            """)
            
            await db.commit()

    async def get_schema_version(self) -> Optional[int]:
        """
        Get current schema version.
        
        Returns:
            Schema version number or None if not initialized
        """
        try:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute(
                    "SELECT MAX(version) FROM schema_migrations"
                ) as cursor:
                    row = await cursor.fetchone()
                    return row[0] if row and row[0] is not None else None
        except aiosqlite.OperationalError:
            # Table doesn't exist yet
            return None
