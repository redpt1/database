import xlwt
from PySide2.QtWidgets import *
import os
import Output
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
from Output import OUTPUT


class prbQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_prb()
        self.ui.setupUi(self)
        self.getwebName()
        self.get = self.getAttr()
        self.sql = ''
        self.model = QtGui.QStandardItemModel()
        self.message = QWidget()
        self.ui.queryButton1.clicked.connect(self.prbquery)
        self.ui.queryButton2.clicked.connect(self.prbquery)

        self.ui.newButton.clicked.connect(self.savefileAddr)

    def getwebName(self):  # 在数据库里获取名字
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        get = 'select `网元/基站名称` from `tbPRB`'
        self.cursor.execute(get)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        getN = self.cursor.fetchall()
        getN = np.array(getN)
        getN = np.unique(getN, axis=0)
        self.ui.webList.addItems(getN[:, 0])

    def getAttr(self):
        read = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = \'tbPRB\''
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        self.cursor.execute(read)
        get = self.cursor.fetchall()
        get = np.array(get)
        [rows, cols] = get.shape
        list = []
        for i in range(4, rows):
            for j in range(cols):
                a = str(get[i, j]).split("(", 1)[0]
                a = a.replace(' ', '')
                list.append(a)
        self.cursor.close()
        self.db.close()
        self.ui.attrList.addItems(list)
        return get[:, 0]

    #todo:完成图表绘制
    def prbquery(self):
        series = QtCharts.QLineSeries()
        x_Aix = QtCharts.QValueAxis()
        y_Aix = QtCharts.QValueAxis()

        ##test
        series.append(1, 1)
        series.append(2, 2)
        x_Aix.setRange(0, 2)
        y_Aix.setRange(0, 2)
        ##

        ##query and series.append()

        ##
        self.output = Output.OUTPUT(series, x_Aix, y_Aix)
        self.output.show()

    def savefileAddr(self):
        directory, ok = QFileDialog.getSaveFileName(self, "文件保存", "/", "Excel文件 (*.xls);;")
        self.outaddr = directory
        self.fileout()

    # todo:完成生成新表操作
    def fileout(self):
            self.db = sqlConnect.connectdb()
            self.cursor = self.db.cursor()
            self.outaddr = self.ui.outfileaddr.text()


            sql = 'select * from tbPRB'
            self.cursor.execute(sql)
            ##
            fields = [field[0] for field in self.cursor.description]
            ##
            alldata = self.cursor.fetchall()
            ##
            book = xlwt.Workbook()
            sheet = book.add_sheet('sheet1')
            for col, field in enumerate(fields):
                sheet.write(0, col, field)
            row = 1
            for data in alldata:
                for col, field in enumerate(data):
                    sheet.write(row, col, field)
                row += 1

            book.save(self.outaddr)
            QMessageBox.warning(self.message, '提示', '导出成功', QMessageBox.Yes)

