from sqlmodel import create_engine
from todo_app.utils.file_service import FileService


class DatabaseProvider:
    def __init__(self, file_service: FileService):
        self.file_service = file_service
        self.engine = None

    def provide_engine(self, database_url: str = None):
        if not database_url:
            database_url = "sqlite:///todo_app.db"  # Default to the provided database URL if not specified

        # Open or create the database file
        database_url = self.file_service.open_existing_database(database_url)

        if not self.engine:
            self.engine = create_engine(database_url, echo=True)

        return self.engine

    def reset_engine(self, database_url: str):
        """Allows resetting the engine with a new database URL."""
        database_url = self.file_service.open_existing_database(database_url)
        self.engine = create_engine(database_url, echo=True)
        return self.engine
