from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, \
    QTableWidget, QTableWidgetItem, QFileDialog
from todo_app.utils.file_service import FileService
from todo_app.utils.database_provider import DatabaseProvider
from todo_app.ui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, controller, file_service: FileService, database_provider: DatabaseProvider):
        super(MainWindow, self).__init__()
        self.controller = controller
        self.file_service = file_service
        self.database_provider = database_provider
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to slots
        self.ui.newFileButton.clicked.connect(self.on_new_file_clicked)
        self.ui.openFileButton.clicked.connect(self.on_open_file_clicked)

    def on_new_file_clicked(self):
        """Handle 'New File' button click."""
        # Open a file dialog to create a new database file
        file_path, _ = QFileDialog.getSaveFileName(None, "Create New Database File", "", "SQLite Files (*.db)")
        if file_path:
            try:
                # Create the new database
                self.file_service.create_new_database(file_path)
                # After creating the file, set up the engine
                self.database_provider.reset_engine(file_path)
                print(f"New database created at: {file_path}")
            except FileExistsError as e:
                print(str(e))

    def on_open_file_clicked(self):
        """Handle 'Open File' button click."""
        # Open a file dialog to select an existing database file
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Database File", "", "SQLite Files (*.db)")
        if file_path:
            try:
                # Open the selected database
                self.file_service.open_existing_database(file_path)
                # Set up the engine with the selected database
                self.database_provider.reset_engine(file_path)
                print(f"Opened database file: {file_path}")
            except FileNotFoundError as e:
                print(str(e))
