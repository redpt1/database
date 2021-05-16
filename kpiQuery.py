from PySide2.QtWidgets import *
import sqlConnect
import numpy as np
from PySide2 import QtGui

from ui.kpiquery import Ui_kpi


class kpiQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_kpi()
        self.ui.setupUi(self)
        self.getsectorName()
        self.getAddr()
        #self.ui.queryButton.clicked.connect(self.sectorquery)
        #self.sql = ''
        #self.model = QtGui.QStandardItemModel()
        #self.message = QWidget()

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

    def getAddr(self):
        read = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = \'tbKPI\''
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        self.cursor.execute(read)
        get = self.cursor.fetchall()
        get = np.array(get)
        #attr=get[4:,0]
        [rows, cols] = get.shape
        list = []
        for i in range(4,rows):
            for j in range(cols):
                a = str(get[i, j]).split("(",1)[0]
                list.append(a)
        self.cursor.close()
        self.db.close()
        self.ui.attrList.addItems(list)


