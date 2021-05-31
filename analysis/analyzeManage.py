import pandas as pd
from PySide2 import QtGui
from PySide2.QtWidgets import *

from analysis.webui import webui
from data.dataInput import mysql_link, sql_assemble
from ui.analyze import Ui_analyze

import sqlConnect

import xlwt
from scipy.stats import norm
from analysis.webManage import webpic
from analysis.InterManage import inter, inputx


class analyzeManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_analyze()
        self.ui.setupUi(self)
        self.message = QWidget()

        self.sql = ''
        self.db = sqlConnect.connectdb()

        self.ui.c2lButton.clicked.connect(self.c2lanalyze)
        self.ui.sectorButton.clicked.connect(self.inputxx)
        self.ui.netButton.clicked.connect(self.webpicput)

    def webpicput(self):
        webpic()
        self.pic=webui()
        self.pic.show()
    def inputxx(self):
        inputx()
        QMessageBox.information(self.message, '提示', '统计完成并导入数据库', QMessageBox.Yes)

    def c2lanalyze(self):
        ##
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        sheet.write(0, 0, 'ServingSector')
        sheet.write(0, 1, 'InterferingSector')
        sheet.write(0, 2, 'C2I_mean')
        sheet.write(0, 3, 'std')
        sheet.write(0, 4, 'PrbC2I9')
        sheet.write(0, 5, 'PrbABS6')
        ##
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        i = 1
        minn = 500
        self.sql = 'select ServingSector,InterferingSector,avg(LtescRSRP-LteNcRSRP)mean,STDDEV_SAMP(LteScRSRP-LteNcRSRP) std from tbMROData group by ServingSector,InterferingSector ' \
                   'having count(LtescRSRP) >=' + str(minn)
        self.cursor.execute(self.sql)
        all_sector = self.cursor.fetchall()
        for data in all_sector:

            prb9 = norm.cdf(x=9, loc=float(data[2]), scale=float(data[3]))
            prb6 = norm.cdf(x=6, loc=float(data[2]), scale=float(data[3])) - norm.cdf(x=-6, loc=float(data[2]), scale=float(data[3]))

            sheet.write(i, 0, data[0])
            sheet.write(i, 1, data[1])
            sheet.write(i, 2, float(data[2]))
            sheet.write(i, 3, float(data[3]))
            sheet.write(i, 4, prb6)
            sheet.write(i, 5, prb9)
            i += 1
        self.cursor.close()
        self.db.close()
        book.save('tbC2Inew.xls')

        self.tbc2iinput('tbC2Inew.xls')
        QMessageBox.information(self.message, '提示', '统计完成并导入数据库', QMessageBox.Yes)

    def tbc2iinput(self,excel_file):
        sql='insert ignore into `tbC2Inew` (`ServingSector`,`InterferingSector`,`C2I_mean`,`std`,`PrbC2I9`,`PrbABS6`) ' \
            'VALUES(%s,%s,%s,%s,%s,%s)'
        datapd = pd.read_excel(excel_file)

        db = mysql_link()
        cursor = db.cursor()
        list = []

        rnum = len(datapd)
        for i in range(1, rnum):
            row_data = datapd.iloc[i].values
            rdata = tuple(row_data)
            list.append(rdata)
        cursor.executemany(sql, list)
        db.commit()
        cursor.close()
        db.close()