# # 用户管理界面（只有管理员权限才能进入）
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui.dataman import Ui_dataMan

import sqlConnect
import xlwt
import os
import numpy as np


class dataManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dataMan()
        self.ui.setupUi(self)

        # self.sSocket =   # 数据库连接口

        self.message = QWidget()

        self.inaddr = ''
        self.outaddr = ''
        self.name = '' #自定义文件名
        self.ui.infileButton.clicked.connect(self.getfileAddr)
        self.ui.outfileButton.clicked.connect(self.savefileAddr)
        self.ui.inButton.clicked.connect(self.fileIn)
        self.ui.outButton.clicked.connect(self.fileOut)

        ##

        sql = 'show tables'
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        for name in self.cursor.fetchall():
            # print(name[0])
            self.ui.dataOut.addItem(name[0])
        self.cursor.close()
        self.db.close()

        ##

    # 获得导入地址
    def getfileAddr(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "./",
                                                         "Excel文件 (*.xls);;分隔符文件 (*.csv)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.inaddr = fileName
        self.ui.infileaddr.setText(self.inaddr)

    # 获得保存目录
    def savefileAddr(self):
        directory = QFileDialog.getExistingDirectory(self,
                                                     "文件保存",
                                                     "./",
                                                     )
        self.outaddr = directory
        self.ui.outfileaddr.setText(self.outaddr)


    def getDbname(self):  # Get item/choice
        Dbname = QDialog()
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        self.cursor.execute('SHOW TABLES')

        items = self.cursor.fetchall()
        print(items)
        self.cursor.close()
        self.db.close()

        items = np.array(items)

        item, okPressed = QInputDialog.getItem(Dbname, "选择", "表名:", items[:, 0], 0, False)

        if okPressed and item:
            return item




    # 数据导入
    def fileIn(self):
        type = self.ui.dataIn.currentIndex()
        print(type)
        self.inaddr = self.ui.infileaddr.text()
        if len(self.inaddr) == 0:
            QMessageBox.warning(self.message, '提示', '导入失败，请选择有效地址', QMessageBox.Yes)
            return

        self.dbName = self.getDbname() # 选择的表名


        '''
        if type == 0: # 	网络配置信息导入
        
        
        
        
        elif type == 1: #  	KPI指标信息导入
        
        
        elif type == 2: #	PRB干扰信息导入
        
        
        elif type == 3:#	MRO数据导入
        
        
            '''



    #自定义文件名称框
    def getName(self):
        filename = QDialog()
        text, okPressed = QInputDialog.getText(filename, '输入文件名', '文件名', QLineEdit.Normal)
        if okPressed :
            if len(text)!=0:
                if (os.path.exists(self.outaddr+'/'+text+'.xls')): #重名文件
                     return 2
                else : #成功
                    self.name = text
                    return 1

            if len(text)==0:#名字为空
                return 3
        else :
            return 0

    # 数据导出
    def fileOut(self):
        if len(self.outaddr) == 0:
            QMessageBox.warning(self.message, '提示', '导出失败，请选择有效地址', QMessageBox.Yes)
            return

        tablename = self.ui.dataOut.currentText()
        mode = self.getName()

        if(mode==1) :
            self.db = sqlConnect.connectdb()
            self.cursor = self.db.cursor()
            self.outaddr = self.ui.outfileaddr.text()

            sql = 'select * from ' + tablename
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
            outaddr = self.ui.outfileaddr.text()

            book.save(outaddr + "/%s.xls" % self.name)
            ##
            QMessageBox.warning(self.message, '提示', '导出成功', QMessageBox.Yes)

        elif (mode == 2):
            QMessageBox.warning(self.message, '提示', '导出失败，文件名重复', QMessageBox.Yes)
            return
        elif (mode == 3):
            QMessageBox.warning(self.message, '提示', '导出失败，文件名为空', QMessageBox.Yes)
            return
        elif(mode == 0):
            return