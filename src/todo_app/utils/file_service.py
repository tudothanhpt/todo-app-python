import os
from sqlmodel import create_engine


class FileService:
    def __init__(self, default_db_url: str = "sqlite:///todo_app.db"):
        self.default_db_url = default_db_url

    def create_new_database(self, db_url: str = None) -> str:
        """Create a new database file at the specified location."""
        if db_url is None:
            db_url = self.default_db_url

        # If the database already exists, do nothing
        if os.path.exists(db_url.replace("sqlite:///", "")):
            raise FileExistsError(f"Database file already exists: {db_url}")

        # Create a new database file (SQLite will automatically create it if it doesn't exist)
        engine = create_engine(db_url, echo=True)
        return db_url

    def open_existing_database(self, db_url: str = None) -> str:
        """Open an existing database."""
        if db_url is None:
            db_url = self.default_db_url

        # Check if the database exists
        if not os.path.exists(db_url.replace("sqlite:///", "")):
            raise FileNotFoundError(f"Database file does not exist: {db_url}")

        return db_url
