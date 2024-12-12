from PySide6.QtWidgets import QApplication
from todo_app.container.container import Container
import sys

def main():
    app = QApplication(sys.argv)
    container = Container()
    main_window = container.main_window()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
