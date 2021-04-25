# # 用户管理界面（只有管理员权限才能进入）
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui.dataman import Ui_dataMan

import userSocket



class dataManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dataMan()
        self.ui.setupUi(self)

        #self.sSocket =   # 数据库连接口

        self.message = QWidget()
        self.inaddr = ''
        self.outaddr = ''
        self.ui.infileButton.clicked.connect(self.getfileAddr)
        self.ui.outfileButton.clicked.connect(self.savefileAddr)
        self.ui.inButton.clicked.connect(self.fileIn)
        self.ui.outButton.clicked.connect(self.fileOut)



    # 获得导入地址
    def getfileAddr(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "./",
                                                          "分隔符文件 (*.csv);;Excel文件 (*.xlsx)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.inaddr = fileName
        self.ui.infileaddr.setText(self.inaddr)

    #获得保存目录
    def savefileAddr(self):
        directory = QFileDialog.getExistingDirectory(self,
                                                     "文件保存",
                                                     "./",
                                                     )
        self.outaddr = directory
        self.ui.outfileaddr.setText(self.outaddr)



    #数据导入
    def fileIn(self):
        type = self.ui.dataIn.currentIndex()
        print(type)
        self.inaddr = self.ui.infileaddr.text()
        if len(self.inaddr) == 0:
            QMessageBox.warning(self.message, '提示', '导入失败，请选择有效地址', QMessageBox.Yes)
            return
        # 数据库接入
        '''
        if type == 0: # 	网络配置信息导入
        elif type == 1: #  	KPI指标信息导入
        elif type == 2: #	PRB干扰信息导入
        elif type == 3:#	MRO数据导入
            '''

    #数据导出
    def fileOut(self):
        type = self.ui.dataIn.currentIndex()
        print(type)
        self.outaddr = self.ui.outfileaddr.text()
        if len(self.outaddr) == 0:
            QMessageBox.warning(self.message, '提示', '导出失败，请选择有效地址', QMessageBox.Yes)
            return
        #数据库接入
        '''
                if type == 0: # 	
                elif type == 1: #  	
                elif type == 2: #	
                elif type == 3:#	
                    '''