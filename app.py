from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton,
    QFormLayout, QLineEdit
)

import sys

# Main Window is a class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 1000, 900)

        self._setup_ui()
        self._setup_events()

    #Setup the user interface by creating widgets and arranging them in layouts
    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        #1st form layout for input fields
        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        
        #Action buttons
        self.button_add = QPushButton("Add Contact")
        self.button_clear = QPushButton("Clear Fields")

    def _setup_events(self):
        pass
        

        
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