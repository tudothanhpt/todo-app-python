from dependency_injector import containers, providers
from todo_app.utils.file_service import FileService
from todo_app.utils.database_provider import DatabaseProvider
from todo_app.repositories.todo_repository import TodoRepository
from todo_app.services.todo_service import TodoService
from todo_app.controllers.todo_controller import TodoController
from todo_app.ui.main_window import MainWindow
from sqlmodel import Session

class Container(containers.DeclarativeContainer):
    # Provide FileService as a singleton
    file_service = providers.Singleton(FileService)

    # Provide DatabaseProvider using FileService
    database_provider = providers.Singleton(DatabaseProvider, file_service=file_service)

    # Use the Singleton's instance to call provide_engine
    engine = providers.Callable(database_provider.provided.provide_engine)
    session = providers.Singleton(Session, bind=engine)

    todo_repository = providers.Factory(TodoRepository, session=session)
    todo_service = providers.Factory(TodoService, repository=todo_repository)
    todo_controller = providers.Factory(TodoController, service=todo_service)

    # Pass controller, file_service, and database_provider to MainWindow
    main_window = providers.Factory(MainWindow, controller=todo_controller, file_service=file_service, database_provider=database_provider)
