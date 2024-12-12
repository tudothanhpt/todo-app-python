from todo_app.repositories.models import Todo
from todo_app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_todo(self, title: str, description: str):
        todo = Todo(title=title, description=description)
        return self.repository.add(todo)

    def get_todos(self):
        return self.repository.get_all()

    def update_todo(self, todo_id: int, title: str = None, description: str = None, isfinished: bool = None):
        todo = self.repository.get_by_id(todo_id)
        if todo:
            if title is not None:
                todo.title = title
            if description is not None:
                todo.description = description
            if isfinished is not None:
                todo.isfinished = isfinished
            return self.repository.update(todo)
        return None

    def delete_todo(self, todo_id: int):
        return self.repository.delete(todo_id)