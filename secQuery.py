from PySide2.QtWidgets import *
import sqlConnect
import numpy as np
from PySide2 import QtGui

from ui.sectorquery import Ui_sector


class secQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_sector()
        self.ui.setupUi(self)
        self.getsectorName()
        self.ui.queryButton.clicked.connect(self.sectorquery)
        self.sql = ''
        self.model = QtGui.QStandardItemModel()
        self.message = QWidget()

    def getsectorName(self):#在数据库里获取名字
            self.db=sqlConnect.connectdb()
            self.cursor=self.db.cursor()
            get = 'select SECTOR_NAME from `tbCell`'
            self.cursor.execute(get)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            getN = self.cursor.fetchall()
            getN = np.array(getN)
            self.ui.sectorList.addItems(getN[:,0])




    def sectorquery(self):
        #
        self.model.clear()
        read = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = \'tbCell\''

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.cursor.execute(read)
        get = self.cursor.fetchall()
        get = np.array(get)
        get = get[:,0]

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)

        if len(self.ui.sectorName.text()) == 0:
            sectorname = self.ui.sectorList.currentText()
            self.sql = 'select * from tbCell where SECTOR_NAME = \'' + sectorname + '\';'
            self.cursor.execute(self.sql)
            i = 0
            for line in self.cursor.fetchall():
                for row in line:
                    item = QtGui.QStandardItem(str(row))
                    self.model.setItem(i, 1, item)
                    item = QtGui.QStandardItem(str(get[i - 1]))
                    self.model.setItem(i, 0, item)
                    i = i + 1
            self.ui.tableView.setModel(self.model)


        else:
            #id查询
            if '0' <= self.ui.sectorName.text()[0] <= '9':
                sectorid = self.ui.sectorName.text()
                self.sql = 'select * from tbCell where SECTOR_ID = \'' + sectorid +'\''
                self.cursor.execute(self.sql)
                i = 0
                if self.cursor.rowcount == 0:
                    QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
                else:
                    for line in self.cursor.fetchall():
                        for row in line:
                            item = QtGui.QStandardItem(str(row))
                            self.model.setItem(i, 1, item)
                            item = QtGui.QStandardItem(str(get[i - 1]))
                            self.model.setItem(i, 0, item)
                            i = i + 1
                    self.ui.tableView.setModel(self.model)

            else:
                sectorname = self.ui.sectorName.text()
                self.sql = 'select * from tbCell where SECTOR_NAME = \'' + sectorname + '\''
                self.cursor.execute(self.sql)
                i = 0
                if self.cursor.rowcount == 0:
                    QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
                else:
                    for line in self.cursor.fetchall():
                        for row in line:
                            item = QtGui.QStandardItem(str(row))
                            self.model.setItem(i, 1, item)
                            item = QtGui.QStandardItem(str(get[i - 1]))
                            self.model.setItem(i, 0, item)
                            i = i + 1
                    self.ui.tableView.setModel(self.model)

        self.cursor.close()
        self.db.close()