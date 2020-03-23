from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from time import sleep
import sys
import pyautogui
import random


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.run = False

    def update(self):
        while True:
            x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
            pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            self.update()


if __name__ == "__main__":
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True
    WIDTH, HEIGHT = pyautogui.size()

    app = QApplication(sys.argv)
    inter = Interface()
    inter.show()
    app.exec()
