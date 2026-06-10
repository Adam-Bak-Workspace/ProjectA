from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton,
    QFormLayout, QLineEdit, QTableWidget,
    QTableWidgetItem
)

import sys

# Main Window is a class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 1000, 900)

        self.contacts = []

        self._setup_ui()
        self._setup_events()

    #Setup the user interface by creating widgets and arranging them in layouts
    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        #1 - form layout for input fields
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        
        #2 - action buttons
        self.button_add = QPushButton("Add Contact")
        self.button_clear = QPushButton("Clear All")

        #3 - contact table
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Name", "Email"])

        #come back to set vertical header to false and alternateing color
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button_add)
        main_layout.addWidget(self.button_clear)
        main_layout.addWidget(QLabel("Contact List"))
        main_layout.addWidget(self.table)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.statusBar().showMessage("Ready")


    def _setup_events(self):
        self.button_add.clicked.connect(self.add_contact)


    def add_contact(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        if not name or not email:
            self.statusBar().showMessage("Please enter a name and email.")
            return

        #Add data to the table
        self.contacts.append((name, email))

        #Update the table with the new contact
        self.table.setRowCount(len(self.contacts))

        #table test
        for row, (name, email) in enumerate(self.contacts):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(email))
        
        self.name_input.clear()
        self.email_input.clear()
        self.statusBar().showMessage(f"{name} with email: {email} Submitted.")



    # def clear_contacts(self):
    #     self.table.setRowCount(0)
    #     self.statusBar().showMessage("All contacts cleared.")


        
#this function will load ctyle from .qss file
def load_stylesheet():                      
    with open("style.qss", "r") as style_file:
        qss = style_file.read()
        app.setStyleSheet(qss)


# The main block checks if the script is run directly (not imported as a module)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # use function to load the stylesheet from the file 
    load_stylesheet()
    window = MainWindow()
    window.show()
    #app.exec() starts the event loop, 
    #sys.exit() ensures that the application exits when the event loop is terminated
    sys.exit(app.exec())