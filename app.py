import sys
from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("eyesaver")
window.setFixedSize(100, 200)
window.setStyleSheet("background-image: url(background.jpg);")