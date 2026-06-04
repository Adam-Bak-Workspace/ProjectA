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
        title_label = QLabel("Welcome to app made with PySide6")
        subtitle_label = QLabel("Some buttons")
        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Cancel")


        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addWidget(button_ok)
        layout.addWidget(button_cancel)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
                       

# The main block checks if the script is run directly (not imported as a module)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #app.exec() starts the event loop, 
    #sys.exit() ensures that the application exits when the event loop is terminated
    sys.exit(app.exec())