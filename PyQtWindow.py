from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class PyQtWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Window')
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        
        self.cycle_color_button = QPushButton('Cycle Color')
        self.cycle_color_button.setFixedSize(64, 64)
        self.cycle_color_button.setStyleSheet("background-color: #4B0082; color: white;")
        self.cycle_color_button.clicked.connect(self.cycle_color)
        self.layout.addWidget(self.cycle_color_button, alignment=Qt.AlignTop | Qt.AlignHCenter)
        
        self.exit_button = QPushButton('Exit')
        self.exit_button.setFixedSize(64, 64)
        self.exit_button.setStyleSheet("background-color: #DC143C; color: white;")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignBottom | Qt.AlignLeft)
        
        self.setLayout(self.layout)
        self.setStyleSheet("background-color: #2F4F4F;")  # Dark Slate Gray
        self.dark = False
    
    def cycle_color(self):
        if self.dark:
            self.cycle_color_button.setStyleSheet("background-color: #4B0082; color: white;")  # Indigo
        else:
            self.cycle_color_button.setStyleSheet("background-color: #8B0000; color: white;")  # Dark Red
        self.dark = not self.dark

def run_pyqt():
    app = QApplication([])
    window = PyQtWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    run_pyqt()
