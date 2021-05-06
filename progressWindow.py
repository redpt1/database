
from PySide2.QtWidgets import *
from PySide2.QtCore import QBasicTimer
import sys
class pWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('导入进度')
        self.show()
        self.doAction()

    def timerEvent(self, e):
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        print("do action")
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    window = pWindow()
    window.show()


