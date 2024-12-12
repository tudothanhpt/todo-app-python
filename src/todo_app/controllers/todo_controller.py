from todo_app.services.todo_service import TodoService

class TodoController:
    def __init__(self, service: TodoService):
        self.service = service

    def create_todo(self, title: str, description: str):
        return self.service.add_todo(title, description)

    def list_todos(self):
        return self.service.get_todos()

    def modify_todo(self, todo_id: int, title: str = None, description: str = None, isfinished: bool = None):
        return self.service.update_todo(todo_id, title, description, isfinished)

    def remove_todo(self, todo_id: int):
        return self.service.delete_todo(todo_id)