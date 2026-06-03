from PySide6.QtWidgets import QApplication, QMainWindow
import sys

# This is a simple PySide6 application
# Main Window is a class that inherits from QMainWindow
# It sets the title and geometry of the window in constructor
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Window App")
        self.setGeometry(100, 100, 400, 300)

# The main block checks if the script is run directly (not imported as a module)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #app.exec() starts the event loop, 
    #sys.exit() ensures that the application exits when the event loop is terminated
    sys.exit(app.exec())