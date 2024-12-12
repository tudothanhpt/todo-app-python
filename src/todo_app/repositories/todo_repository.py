from sqlmodel import Session
from todo_app.repositories.models import Todo

class TodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, todo: Todo):
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def get_all(self):
        return self.session.query(Todo).all()

    def get_by_id(self, todo_id: int):
        return self.session.query(Todo).filter(Todo.id == todo_id).first()

    def update(self, todo: Todo):
        self.session.add(todo)
        self.session.commit()
        return todo

    def delete(self, todo_id: int):
        todo = self.get_by_id(todo_id)
        if todo:
            self.session.delete(todo)
            self.session.commit()
        return todo