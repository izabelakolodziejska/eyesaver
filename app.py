import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor, QBrush, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from timer import TimerWidget

widgets = {
    'title': [],
    'button': [],
    'timer' :[]
}

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

def clear_widgets():
    for key in widgets:
        for w in widgets[key]:
            w.hide()
        widgets[key].clear()

def start_timer():
    clear_widgets()
    frame2()

def create_bttn(name):
    bttn = QPushButton(name)
    bttn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    bttn.setFixedSize(150, 50)
    bttn.setStyleSheet("""
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
    return bttn


def frame1():
    #main title
    title = QLabel("eyesaver~")
    font = QFont('Sitka', 22)
    font.setBold(True)
    title.setFont(font)
    title.setStyleSheet("color: #6A006A; margin-top: 35px; margin-bottom: 30px;")
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    widgets['title'].append(title)
    layout.addWidget(widgets['title'][-1])

    start = create_bttn('start')
    start.clicked.connect(start_timer)
    widgets['button'].append(start)
    layout.addWidget(widgets['button'][-1], alignment=Qt.AlignmentFlag.AlignCenter)

    settings = create_bttn('settings')
    widgets['button'].append(settings)
    layout.addWidget(widgets['button'][-1], alignment=Qt.AlignmentFlag.AlignCenter)



def frame2():
    def on_mode_changed(mode):
        if mode == "long":
            title2.setText("computer time!")
        else:
            title2.setText("now look away :)")


    title2 = QLabel("computer time!")
    font2 = QFont('Sitka', 22)
    font2.setBold(True)
    title2.setFont(font2)
    title2.setStyleSheet("color: #6A006A; margin-top: 35px; margin-bottom: 30px;")
    title2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    widgets['title'].append(title2)
    layout.addWidget(widgets['title'][-1])

    timer_widget = TimerWidget()
    widgets['timer'].append(timer_widget)
    layout.addWidget(widgets['timer'][-1])
    timer_widget.mode_changed.connect(on_mode_changed)

frame1()

window.setLayout(layout)

window.show()
sys.exit(app.exec())