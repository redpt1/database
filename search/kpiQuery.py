from PySide2.QtWidgets import *
import sqlConnect
import numpy as np
from PySide2 import QtGui
from PySide2 import QtCharts
from PySide2.QtCharts import QtCharts
from datetime import datetime
from ui.kpiquery import Ui_kpi
from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtGui import *

class kpiQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_kpi()
        self.ui.setupUi(self)
        self.getsectorName()
        self.get = self.getAttr()
        self.ui.queryButton.clicked.connect(self.sectorquery)
        self.ui.queryButton_2.clicked.connect(self.sectorquery_2)
        self.ui.queryButton_4.clicked.connect(self.drawQuery)
        self.sql = ''
        self.model = QtGui.QStandardItemModel()
        self.message = QWidget()

    def getsectorName(self):  # 在数据库里获取名字
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        get = 'select 小区名称 from `tbKPI`'
        self.cursor.execute(get)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        getN = self.cursor.fetchall()
        getN = np.array(getN)
        getN = np.unique(getN, axis=0)
        self.ui.sectornameList.addItems(getN[:, 0])

    def getAttr(self):
        read = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = \'tbKPI\''
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

    def sectorquery(self):
        self.model.clear()

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)

        sectorname = self.ui.sectorName.text()
        self.sql = 'select * from tbKPI where 小区名称 = \'' + sectorname + '\';'
        self.cursor.execute(self.sql)

        k = 0
        for head in self.get:
            item = QtGui.QStandardItem(str(head))
            self.model.setItem(k, 0, item)
            k = k + 1

        if self.cursor.rowcount == 0:
            QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
        else:
            i = 0
            j = 0
            for line in self.cursor.fetchall():
                j = j + 1
                i = 0
                for row in line:
                    item = QtGui.QStandardItem(str(row))
                    self.model.setItem(i, j, item)
                    i = i + 1
            self.ui.tableView.setModel(self.model)
        self.cursor.close()
        self.db.close()

    def sectorquery_2(self):
        self.model.clear()

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)

        sectorname = self.ui.sectornameList.currentText()
        self.sql = 'select * from tbKPI where 小区名称 = \'' + sectorname + '\';'
        self.cursor.execute(self.sql)

        k = 0
        for head in self.get:
            item = QtGui.QStandardItem(str(head))
            self.model.setItem(k, 0, item)
            k = k + 1

        if self.cursor.rowcount == 0:
            QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
        else:
            i = 0
            j = 0
            for line in self.cursor.fetchall():
                j = j + 1
                i = 0
                for row in line:
                    item = QtGui.QStandardItem(str(row))
                    self.model.setItem(i, j, item)
                    i = i + 1
            self.ui.tableView.setModel(self.model)
        self.cursor.close()
        self.db.close()

    def drawQuery(self):
        self.flag = 0 #用于记录数据是否小于1

        times = datetime.strptime(self.ui.dateEditS.text(), "%Y/%m/%d")
        timef = datetime.strptime(self.ui.dateEditF.text(), "%Y/%m/%d")

        if timef < times:
            QMessageBox.warning(self.message, '提示', '时间非法', QMessageBox.Yes)
            return
        if timef == times:
            QMessageBox.warning(self.message, '提示', '仅有一条数据无法绘制折线图', QMessageBox.Yes)
            return

        times = datetime.strftime(times, '%m/%d/%Y %H:%M:%S')
        timef = datetime.strftime(timef, '%m/%d/%Y %H:%M:%S')

        time1 = QDateTime()
        time1.setDate(QDate(int(times.split('/')[2].split(' ')[0]), int(times.split('/')[0]), int(times.split('/')[1])))

        time2 = QDateTime()
        time2.setDate(QDate(int(timef.split('/')[2].split(' ')[0]), int(timef.split('/')[0]), int(timef.split('/')[1])))


        dates = int(times.split('/')[1])
        datef = int(timef.split('/')[1])

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        series = QtCharts.QLineSeries()
        if self.ui.attrList.currentText().find('率') != -1:
            self.flag = 1

        datamax = 0
        datamin = 0xffffff
        count = datef - dates + 1


        for date in range(dates, datef + 1):
            time = times.split('/')[0] + '/' + str(date) + '/' + times.split('/')[2]
            que = '`' + self.get[self.ui.attrList.currentIndex() + 4] + '`'
            self.sql = 'select ' + que + \
                       ' from tbKPI where 起始时间 = \'' + time + '\' and `小区名称` = \'' + self.ui.webName.text() + '\''
            self.cursor.execute(self.sql)
            Xtime = QDateTime()
            Xtime.setDate(QDate(int(times.split('/')[2].split(' ')[0]), int(times.split('/')[0]), date))


            if self.cursor.rowcount == 0:
                pass
            else:
                count = count - 1
                for data in self.cursor.fetchall():
                    if data[0] is None:
                        QMessageBox.warning(self.message, '提示', '该数据不合法无法画出图像', QMessageBox.Yes)
                        return
                    if self.flag == 0:
                        if int(data[0]) > datamax:
                            datamax = int(data[0])
                        if int(data[0]) < datamin:
                            datamin = int(data[0])
                        #print(data[0])
                        series.append(float(Xtime.toMSecsSinceEpoch()), float(data[0]))


                    else:
                        if float(data[0]) > datamax:
                            datamax = float(data[0])
                        if float(data[0]) < datamin:
                            datamin = float(data[0])
                        #print(data[0])
                        series.append(float(Xtime.toMSecsSinceEpoch()), float(data[0]))

        x_Aix = QtCharts.QDateTimeAxis()
        x_Aix.setRange(time1, time2)
        x_Aix.setTickCount(datef - dates + 1)
        x_Aix.setFormat("MM/dd/yyyy")
        y_Aix = QtCharts.QValueAxis()
        y_Aix.setRange(float(datamin), float(datamax))

        if self.flag == 0 and datamin != datamax:
            y_Aix.setTickType(QtCharts.QValueAxis.TickType.TicksDynamic)
            y_Aix.setTickAnchor(datamin)
            y_Aix.setTickInterval((datamax - datamin) / ((datef - dates + 1)+2))
            y_Aix.setLabelFormat("%E") # 科学计数法

        elif datamin == datamax == 0 :
            y_Aix.setRange(float(0),float(1))
            y_Aix.setTickCount(2)
            y_Aix.setLabelFormat("%u")




        elif self.flag == 1:
            y_Aix.setLabelFormat("%.3f")

        ##
        if count == datef - dates + 1:
            QMessageBox.warning(self.message, '提示', '未查询到数据', QMessageBox.Yes)
            return
        elif count > 0:
            QMessageBox.warning(self.message, '提示', '存在某天数据为空', QMessageBox.Yes)

        self.pic = QWidget()
        self.pic.setWindowTitle('折线统计图')

        chartView = QtCharts.QChartView(self.pic)
        chartView.chart().addSeries(series)
        chartView.chart().setAxisY(y_Aix,series=series)
        chartView.chart().setAxisX(x_Aix,series=series)

        chartView.chart().legend().hide()
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.setGeometry(0, 0, self.pic.width(), self.pic.height())

        self.pic.setGeometry(400, 390, 695, 520)
        self.pic.show()
