from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QLabel


class TimerWidget(QWidget):
    def __init__(self):
        super.__init__()

        self.time_20min = 20 * 60
        self.time_20sec = 20

        self.mode = 'long'
        self.remaining_seconds = self.time_20min

        self.label = QLabel(self.format_time(self.remaining_seconds))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        else:
            #to do: dźwięk końca
            #new timer for eye rest
            if self.mode == 'long':
                self.mode = 'short'
                self.remaining_seconds = self.time_20sec
            else:
                self.mode = 'long'
                self.remaining_seconds = self.time_20min
        self.label.setText(self.format_time(self.remaining_seconds))

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{m:02d}:{s:02d}"

