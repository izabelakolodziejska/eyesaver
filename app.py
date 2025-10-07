import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor, QBrush, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("eyesaver")
window.setFixedSize(400, 250)
#setStyleSheet messed with buttons (no button color was displayed)
palette = window.palette()
palette.setBrush(window.backgroundRole(), QBrush(QPixmap("background.jpg")))
window.setPalette(palette)

#vertical layout: title and two buttons
layout = QVBoxLayout()

#main title
title = QLabel("eyesaver~")
font = QFont('Sitka', 22)
font.setBold(True)
title.setFont(font)
title.setStyleSheet("color: #fff9ed; margin-top: 45px;")
title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

start = QPushButton("start")
start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
start.setFixedSize(200, 50)
start.setStyleSheet("""
    QPushButton {
        background-color: #bf87a3;         
        color: #fff9ed;                    
        font-family: Sitka;                
        font-size: 15pt;      
        font-weight: bold;             
        border: none;                     
        border-radius: 10px;              
        padding: 6px 12px;     
    }
    QPushButton:hover {
        background-color: #a06b85;        
    }
    QPushButton:pressed {
        background-color: #6A006A;         
    }
""")

layout.addWidget(title)
layout.addWidget(start, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)

window.show()
sys.exit(app.exec())