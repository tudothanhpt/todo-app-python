from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, \
    QTableWidget, QTableWidgetItem, QFileDialog

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("TODO Application")

        # Central Widget
        self.centralWidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Layouts
        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.inputLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        # Input Fields
        self.titleLineEdit = QLineEdit()
        self.titleLineEdit.setPlaceholderText("Enter title")
        self.descriptionTextEdit = QTextEdit()
        self.descriptionTextEdit.setPlaceholderText("Enter description")

        # Buttons
        self.addButton = QPushButton("Add TODO")
        self.deleteButton = QPushButton("Delete TODO")
        self.refreshButton = QPushButton("Refresh TODOs")
        self.newFileButton = QPushButton("New File")
        self.openFileButton = QPushButton("Open File")

        # TODO Table
        self.todoTable = QTableWidget()
        self.todoTable.setColumnCount(4)
        self.todoTable.setHorizontalHeaderLabels(["ID", "Title", "Description", "Finished"])

        # Arrange Layouts
        self.inputLayout.addWidget(self.titleLineEdit)
        self.inputLayout.addWidget(self.descriptionTextEdit)

        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.addWidget(self.refreshButton)
        self.buttonLayout.addWidget(self.newFileButton)
        self.buttonLayout.addWidget(self.openFileButton)

        self.mainLayout.addLayout(self.inputLayout)
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.todoTable)

        # Connect buttons to slots
        self.newFileButton.clicked.connect(self.on_new_file_clicked)
        self.openFileButton.clicked.connect(self.on_open_file_clicked)

    def on_new_file_clicked(self):
        """Handle 'New File' button click."""
        # Open a file dialog to create a new database file
        file_path, _ = QFileDialog.getSaveFileName(None, "Create New Database File", "", "SQLite Files (*.db)")
        if file_path:
            # Handle creating a new database file
            # You can call your service or logic here to create the new file
            print(f"Creating new file at: {file_path}")
            # Code to create the database goes here (e.g., call FileService)
            # self.file_service.create_new_database(file_path)

    def on_open_file_clicked(self):
        """Handle 'Open File' button click."""
        # Open a file dialog to select an existing database file
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Database File", "", "SQLite Files (*.db)")
        if file_path:
            # Handle opening the selected file
            print(f"Opening file: {file_path}")
            # Code to open the database goes here (e.g., call FileService)
            # self.file_service.open_existing_database(file_path)
