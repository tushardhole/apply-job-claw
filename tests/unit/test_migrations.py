"""Unit tests for database migrations."""

import pytest
import tempfile
import os

from src.infrastructure.storage.migrations import MigrationManager
from src.infrastructure.storage.schema import DatabaseSchema


@pytest.fixture
def db_path():
    """Create a temporary database path."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
        path = tmp.name
    
    yield path
    
    # Cleanup
    if os.path.exists(path):
        os.unlink(path)


@pytest.mark.asyncio
async def test_initialize_database(db_path):
    """Test database initialization."""
    manager = MigrationManager(db_path)
    await manager.initialize_database()
    
    # Check that schema version was recorded
    version = await manager.get_schema_version()
    assert version == 1


@pytest.mark.asyncio
async def test_schema_tables_creation(db_path):
    """Test that all tables are created."""
    import aiosqlite
    
    manager = MigrationManager(db_path)
    await manager.initialize_database()
    
    async with aiosqlite.connect(db_path) as db:
        # Check that all tables exist
        tables = [
            "users",
            "user_configs",
            "user_profiles",
            "resumes",
            "cover_letters",
            "job_applications",
            "application_history",
            "schema_migrations",
        ]
        
        for table in tables:
            async with db.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
            ) as cursor:
                row = await cursor.fetchone()
                assert row is not None, f"Table {table} was not created"


@pytest.mark.asyncio
async def test_schema_indexes_creation(db_path):
    """Test that indexes are created."""
    import aiosqlite
    
    manager = MigrationManager(db_path)
    await manager.initialize_database()
    
    async with aiosqlite.connect(db_path) as db:
        # Check that indexes exist
        async with db.execute(
            "SELECT name FROM sqlite_master WHERE type='index'"
        ) as cursor:
            indexes = [row[0] for row in await cursor.fetchall()]
            
            # Check for some key indexes
            assert "idx_users_telegram_chat_id" in indexes
            assert "idx_job_applications_user_id" in indexes


def test_schema_sql_generation():
    """Test that schema SQL can be generated."""
    tables_sql = DatabaseSchema.get_create_tables_sql()
    assert len(tables_sql) > 0
    assert all("CREATE TABLE" in sql.upper() for sql in tables_sql)
    
    indexes_sql = DatabaseSchema.get_create_indexes_sql()
    assert len(indexes_sql) > 0
    assert all("CREATE INDEX" in sql.upper() for sql in indexes_sql)
