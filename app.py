import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("eyesaver")
window.setFixedSize(400, 250)
#additional css to prevent image distortion
window.setStyleSheet("""
    background-image: url(background.jpg);
    background-repeat: no-repeat;
    background-position: center;
""")

#vertical layout: title and two buttons
layout = QVBoxLayout()

#main title
title = QLabel("eyesaver~")
font = QFont('Sitka', 22)
font.setBold(True)
title.setFont(font)
title.setStyleSheet("color: white; margin-top: 45px;")
title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

#to do: bigger font, no background color id displayed
start = QPushButton("start")
start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
start.setStyleSheet("""
    QPushButton {
        background-color: #8B008B;         
        color: white;                    
        font-family: Sitka;                
        font-size: 12pt;                   
        border: none;                     
        border-radius: 10px;              
        padding: 6px 12px;                
    }
    QPushButton:hover {
        background-color: #9A32CD;        
    }
    QPushButton:pressed {
        background-color: #6A006A;         
    }
""")

layout.addWidget(title)
layout.addWidget(start)

window.setLayout(layout)

window.show()
sys.exit(app.exec())