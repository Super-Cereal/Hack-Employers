from PyQt5.QtWidgets import QMainWindow, QApplication
from interface import Ui_MainWindow
from time import sleep
import sys
import pyautogui
import random


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.run = False

    def update(self):
        while True:
            if self.run:
                x, y = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)
                time_dur = time_sleep = random.uniform(0.2, 1.5)
                pyautogui.moveTo(x, y, duration=time_dur, tween=pyautogui.easeInOutQuad)
                sleep(time_sleep)
            app.processEvents()

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            self.run = False if self.run else True

    def closeEvent(self, event):
        sys.exit()


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    WIDTH, HEIGHT = pyautogui.size()

    app = QApplication(sys.argv)
    inter = Interface()
    inter.show()
    inter.update()
