from ui.enodequery import Ui_enode

from PySide2.QtWidgets import *
import sqlConnect
import numpy as np
from PySide2 import QtGui


class enoQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_enode()
        self.ui.setupUi(self)
        self.getName()
        self.getID()
        self.ui.queryButton.clicked.connect(self.enodequery_id_name)
        self.ui.queryButton_2.clicked.connect(self.enodequery_idlist)
        self.ui.queryButton_3.clicked.connect(self.enodequery_namelist)
        self.get = self.getAttr()
        self.sql = ''
        self.model = QtGui.QStandardItemModel()
        self.message = QWidget()

    def getName(self):  # 在数据库里获取名字
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        get = 'select ENODEB_NAME from `tbCell`'
        self.cursor.execute(get)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        getN = self.cursor.fetchall()
        getN = np.array(getN)
        getN = np.unique(getN, axis=0)
        self.ui.enodenameList.addItems(getN[:, 0])

    def getID(self):
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        get = 'select ENODEBID from `tbCell`'
        self.cursor.execute(get)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        getN = self.cursor.fetchall()
        getN = np.array(getN)
        getN = np.unique(getN, axis=0)
        self.ui.enodeidList.addItems(getN[:, 0])

    def getAttr(self):
        read = 'select COLUMN_NAME from information_schema.COLUMNS where table_name = \'tbCell\''
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        self.cursor.execute(read)
        get = self.cursor.fetchall()
        get = np.array(get)
        get = get[:, 0]
        self.cursor.close()
        self.db.close()
        return get


    def enodequery_id_name(self):
        self.model.clear()

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)


        # id查询
        if '0' <= self.ui.enodeName.text()[0] <= '9':
            enodeid = self.ui.enodeName.text()
            self.sql = 'select * from tbCell where ENODEBID = \'' + enodeid + '\''
            self.cursor.execute(self.sql)

            if self.cursor.rowcount == 0:
                QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
            else:
                k = 0
                for head in self.get:
                    item = QtGui.QStandardItem(str(head))
                    self.model.setItem(k, 0, item)
                    k = k + 1

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

        else:
            sectorname = self.ui.enodeName.text()
            self.sql = 'select * from tbCell where ENODEB_NAME = \'' + sectorname + '\''
            self.cursor.execute(self.sql)
            i = 0
            j = 0
            if self.cursor.rowcount == 0:
                QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
            else:
                k = 0
                for head in self.get:
                    item = QtGui.QStandardItem(str(head))
                    self.model.setItem(k, 0, item)
                    k = k + 1

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

    def enodequery_idlist(self):
        self.model.clear()

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)

        enodeid = self.ui.enodeidList.currentText()
        self.sql = 'select * from tbCell where ENODEBID = \'' + enodeid + '\';'
        self.cursor.execute(self.sql)

        k = 0
        for head in self.get:
            item = QtGui.QStandardItem(str(head))
            self.model.setItem(k, 0, item)
            k = k + 1

        i = 0
        j = 0

        if self.cursor.rowcount == 0:
            QMessageBox.warning(self.message, '提示', '无结果', QMessageBox.Yes)
        else:
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

    def enodequery_namelist(self):
        self.model.clear()

        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)

        enodename = self.ui.enodenameList.currentText()
        self.sql = 'select * from tbCell where ENODEB_NAME = \'' + enodename + '\';'
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