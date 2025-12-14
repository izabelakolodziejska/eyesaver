import sys
from operator import truediv

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QCursor, QBrush, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from timer import TimerWidget

widgets = {
    'title': [],
    'button': [],
    'timer' : [],
    'text' : []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("eyesaver")
window.setFixedSize(400, 250)
#setStyleSheet messed with buttons (no button color was displayed)
palette = window.palette()
palette.setBrush(window.backgroundRole(), QBrush(QPixmap("background.jpg")))
window.setPalette(palette)
font = QFont('Sitka', 22)
font.setBold(True)

#vertical layout: title and two buttons
layout = QVBoxLayout()

def clear_widgets():
    for key in widgets:
        for w in widgets[key]:
            w.hide()
        widgets[key].clear()

def start_frame(function):
    clear_widgets()
    function()

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
    title.setFont(font)
    title.setStyleSheet("color: #6A006A; margin-top: 35px; margin-bottom: 30px;")
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    widgets['title'].append(title)
    layout.addWidget(widgets['title'][-1])

    start = create_bttn('start')
    start.clicked.connect(lambda: start_frame(frame2))
    widgets['button'].append(start)
    layout.addWidget(widgets['button'][-1], alignment=Qt.AlignmentFlag.AlignCenter)

    about = create_bttn('about')
    widgets['button'].append(about)
    about.clicked.connect(lambda: start_frame(frame3))
    layout.addWidget(widgets['button'][-1], alignment=Qt.AlignmentFlag.AlignCenter)



def frame2():
    def on_mode_changed(mode):
        if mode == "long":
            title2.setText("computer time!")
        else:
            title2.setText("now look away :)")


    title2 = QLabel("computer time!")
    title2.setFont(font)
    title2.setStyleSheet("color: #6A006A; margin-top: 35px; margin-bottom: 30px;")
    title2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    widgets['title'].append(title2)
    layout.addWidget(widgets['title'][-1])

    timer_widget = TimerWidget()
    widgets['timer'].append(timer_widget)
    layout.addWidget(widgets['timer'][-1])
    timer_widget.mode_changed.connect(on_mode_changed)

def frame3():
    desc = QLabel("This simple app is designed to help your eyes while using computer. It reminds you every 20 minutes about a 20 second 'away from monitor' break!")
    desc.setWordWrap(True)
    desc.setFont(font)
    desc.setStyleSheet(
        '''
        font-size: 18px;
        color: #6A006A;
        padding: 5px;
        margin-top: 25px
        '''
    )
    widgets['text'].append(desc)
    layout.addWidget(widgets['text'][-1])

    back = create_bttn('go back')
    back.clicked.connect(lambda: start_frame(frame1))
    widgets['button'].append(back)
    layout.addWidget(widgets['button'][-1], alignment=Qt.AlignmentFlag.AlignCenter)

start_frame(frame1)

window.setLayout(layout)

window.show()
sys.exit(app.exec())