from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("eyesaver")

        button = QPushButton('start')

        self.setFixedSize(350, 300)

        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
