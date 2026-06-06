from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QLineEdit
import sys
import random

# This is a simple PySide6 application
# Main Window is a class that inherits from QMainWindow
# It sets the title and geometry of the window in constructor
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Window App")
        self.setGeometry(100, 100, 400, 300)

        self._setup_ui()
        self._setup_events()

    def _setup_ui(self):
        #cointainer widget for the main window
        self.central_widget = QWidget(self)
        #Layout is created to be used in the central widget
        self.main_layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.email_input = QLineEdit()

        self.form_layout.addRow("Name:", self.name_input)
        self.form_layout.addRow("Email:", self.email_input)

        #Items to be added to the layout
        self.label = QLabel("Click the button")
        self.statusBar().showMessage("Please fill in all fields.")
        self.button_hello = QPushButton("Say Hello")
        self.button_clear = QPushButton("Clear Text")
        self.button_test_CLI = QPushButton("CLI Test & Color change")
        self.button_submit = QPushButton("Submit")
        self.button_clear_form = QPushButton("Clear Form")


        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button_hello)
        self.main_layout.addWidget(self.button_clear)
        self.main_layout.addWidget(self.button_test_CLI)
        
        #adding new layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.button_submit)
        self.main_layout.addWidget(self.button_clear_form)

        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)
        

    def _setup_events(self):
        #send signal when the button is clicked
        self.button_hello.clicked.connect(self.say_hello)
        self.button_clear.clicked.connect(self.clear_text)
        self.button_test_CLI.clicked.connect(self.change_btn_color)
        self.button_submit.clicked.connect(self.submit_form)
        self.button_clear_form.clicked.connect(self.clear_form)
        

    def say_hello(self):
        self.label.setText("Hello from function")

    def clear_text(self):
        self.label.setText("")

    def change_btn_color(self):
        print("Button Color changed")
        self.button_test_CLI.setStyleSheet(f"background-color: {self.randomize_color()};")

    def submit_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()

        #checking if the fields are not empty
        if name and email:
            self.statusBar().showMessage(f"Submitted: Name: {name}, Email: {email}")
        else:
            self.statusBar().showMessage("Please fill in all fields.")

    def clear_form(self):
        self.name_input.clear()
        self.email_input.clear()
        #self.statusBar().clearMessage()
        self.statusBar().showMessage("Form cleared.")

    def randomize_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"rgb({r}, {g}, {b})"

        
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