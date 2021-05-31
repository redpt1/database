from PySide2.QtWidgets import *
import sqlConnect
import numpy as np
from PySide2 import QtGui
from PySide2 import QtCharts
from PySide2.QtCharts import QtCharts
from datetime import datetime
from ui.prbquery import Ui_prb
from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtGui import *
from ui.output import Ui_output

class OUTPUT(QWidget):
    def __init__(self, series, x_Aix, y_Aix):
        super().__init__()
        self.ui = Ui_output()
        self.ui.setupUi(self)

        self.series = series
        self.x_Aix = x_Aix
        self.y_Aix = y_Aix
        self.chart()

        self.ui.outButton.clicked.connect(self.output)
        self.message = QWidget()

    def output(self):
        directory,ok = QFileDialog.getSaveFileName(self, "文件保存", "/", "图片文件 (*.png);;(*.jpeg)")
        self.outaddr = directory
        print(directory)
        if ok:
            self.savePic()

    def savePic(self):
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.ui.chart.winId())
        image = pix.toImage()
        image.save(self.outaddr)
        QMessageBox.information(self.message, '提示', '导出成功', QMessageBox.Yes)

    def chart(self):
        chartView = QtCharts.QChartView(self.ui.chart)
        chartView.chart().setAxisY(self.y_Aix, series=self.series)
        chartView.chart().setAxisX(self.x_Aix, series=self.series)
        chartView.chart().legend().hide()
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().addSeries(self.series)
        self.ui.chart.setGeometry(0, 0, 800, 600)
        chartView.setGeometry(0, 0, self.ui.chart.width(), self.ui.chart.height())

