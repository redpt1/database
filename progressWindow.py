from PySide2 import QtWidgets
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import dataInput

class PWindow(QWidget):
    def __init__(self):
        super(PWindow, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("导入进度")
        self.setGeometry(300,100,300,150)
        #载入进度条控件
        self.pgb=QProgressBar(self)
        self.pgb.move(50,50)
        self.pgb.resize(200,20)

        #配置一个值表示进度条的当前进度
        self.pv=0

        #申明一个时钟控件
        self.timer=QBasicTimer()

        #设置进度条的范围
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setValue(self.pv)

        self.show()



    def timerEvent(self,e):
        if self.pv == 100:
            self.timer.stop()
            self.close()

        else:
            self.pv=(dataInput.i/dataInput.rnum)*100
            self.pgb.setValue(self.pv)

