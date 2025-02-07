import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QCursor, QIcon, QFont, QFontDatabase
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtGui, QtCore
import time


class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0, self)
        self.display = QLabel(self)
        self.start_button = QPushButton("START", self)
        self.stop_button = QPushButton("STOP", self)
        self.reset_button = QPushButton("RESET", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("StopWatch")
        self.setFixedSize(600, 400)
        self.display.setText("00:00:00")

        self.start_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.display)
        buttons = QHBoxLayout()
        buttons.addWidget(self.start_button)
        buttons.addWidget(self.stop_button)
        buttons.addWidget(self.reset_button)
        mainLayout.addLayout(buttons)
        self.setLayout(mainLayout)

        self.display.setObjectName("display")
        self.start_button.setObjectName("start")
        self.stop_button.setObjectName("stop")
        self.reset_button.setObjectName("reset")

        self.setStyleSheet("""
            Timer {
                background-color: #44A781;
            }
            QLabel#display {
                min-height: 200px;
                max-height: 200px;
                min-width: 500px;
                max-width: 1250px;
                background-color: black;
                color: white;
                font-size: 100px;
                border-radius: 5px;
                padding: 1px;
                text-align: right;
            }
            QPushButton#start, #stop, #reset {
                height: 40px;
                background-color: #75A794;
                font-size: 30px;
                font-weight: bold;
                margin: 10px;
                border-radius: 4px;
            }
        """)

        self.start_button.clicked.connect(self.start_timer)
        self.start_button.clicked.connect(self.stop_timer)
        self.start_button.clicked.connect(self.reset_timer)
        self.time.timeout.connect(self.format_time)
        
    def start_timer(self):
        self.timer.start(10)

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        pass

    def format_time(self, time):
        hours = time.hours()
        minutes = time.minutes()
        seconds = time.seconds()
        milliseconds = time.msec()
        return f"{hours}:{minutes}:{seconds}.{milliseconds}"

    def update_time(self):
        self.time = self.time.addMSec(10)
        self.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())