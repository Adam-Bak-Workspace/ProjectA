from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

# This is a simple PySide6 application
# Main Window is a class that inherits from QMainWindow
# It sets the title and geometry of the window in constructor
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Window App")
        self.setGeometry(100, 100, 400, 300)

        #cointainer widget for the main window
        central_widget = QWidget(self)

        #Layout is created to be used in the central widget
        layout = QVBoxLayout()

        #Items to be added to the layout
        self.label = QLabel("Click the button")
        button_hello = QPushButton("Say Hello")
        button_clear = QPushButton("Clear Text")
        button_CLI_test = QPushButton("CLI Test")


        #send signal when the button is clicked
        button_CLI_test.clicked.connect(self.CLI_test)
        button_hello.clicked.connect(self.say_hello)
        button_clear.clicked.connect(self.clear_text)
        
        layout.addWidget(self.label)
        layout.addWidget(button_hello)
        layout.addWidget(button_clear)
        layout.addWidget(button_CLI_test)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    #Signal test
    def CLI_test(self):
        print("Signal was sent from the button")
    def say_hello(self):
        self.label.setText("Hello from function")
    def clear_text(self):
        self.label.setText("")
        
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