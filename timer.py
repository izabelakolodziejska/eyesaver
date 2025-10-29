from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from playsound import playsound


class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.time_20min = 10 #20 * 60
        self.time_20sec = 20

        self.mode = 'long'
        self.remaining_seconds = self.time_20min

        self.label = QLabel(self.format_time(self.remaining_seconds))
        font = QFont('Sitka', 33)
        font.setBold(True)
        self.label.setStyleSheet("color: #6A006A; margin-top: 35px; margin-bottom: 30px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        else:
            #new timer for eye rest
            if self.mode == 'long':
                playsound('conveniencestorering.wav')
                self.mode = 'short'
                self.remaining_seconds = self.time_20sec
            else:
                playsound('success-jingle.wav')
                self.mode = 'long'
                self.remaining_seconds = self.time_20min
        self.label.setText(self.format_time(self.remaining_seconds))

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{m:02d}:{s:02d}"

