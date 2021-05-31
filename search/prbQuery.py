from datetime import datetime
import xlwt
from PySide2.QtCore import QDateTime, QDate, QTime
from PySide2.QtWidgets import *
import re
import numpy as np
from PySide2 import QtGui
from PySide2 import QtCharts
from PySide2.QtCharts import QtCharts
from search import Output
from ui.prbquery import Ui_prb
from PySide2.QtCharts import *
from data.dataInput import *


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
        self.ui.queryButton1.clicked.connect(self.prbquery1)
        self.ui.queryButton2.clicked.connect(self.prbquery2)

        self.ui.newButton.clicked.connect(self.savefileAddr)

    def getwebName(self):  # 在数据库里获取名字
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        get = 'select `网元/基站名称` from `tbPRB`'
        self.cursor.execute(get)
        self.cursor.close()
        self.db.close()
        getN = self.cursor.fetchall()
        getN = np.array(getN)
        getN = np.unique(getN, axis=0)

        self.ui.webList.addItems(getN[:, 0])
        self.jud = getN[:, 0]

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


    def prbquery1(self):
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        series = QtCharts.QLineSeries()
        x_Aix = QtCharts.QDateTimeAxis()
        y_Aix = QtCharts.QValueAxis()

        t1 = self.ui.dateTimeEdits.text()
        t2 = self.ui.dateTimeEditf.text()
        #print(t1,t2)
        times = datetime.strptime(t1, "%Y/%m/%d %H:%M")
        timef = datetime.strptime(t2, "%Y/%m/%d %H:%M")

        if timef < times:
            QMessageBox.warning(self.message, '提示', '时间非法', QMessageBox.Yes)
            return
        if timef == times:
            QMessageBox.warning(self.message, '提示', '仅有一条数据无法绘制折线图', QMessageBox.Yes)
            return
        time1 = QDateTime()
        time1.setDate(QDate(int(t1.split('/')[0]), int(t1.split('/')[1].split('/')[0]), int(t1.split('/',2)[2].split(' ')[0])))
        time1.setTime(QTime(int(t1.split(' ')[1].split(':')[0]),0))

        time2 = QDateTime()
        time2.setDate(QDate(int(t2.split('/')[0]), int(t2.split('/')[1].split('/')[0]), int(t2.split('/',2)[2].split(' ')[0])))
        time2.setTime(QTime(int(t2.split(' ')[1].split(':')[0]),0))


        times = t1.split('/')[2]
        dates = int(times.split(' ')[0])
        hours = int(times.split(' ')[1].split(':')[0])
        timef = t2.split('/')[2]
        datef = int(timef.split(' ')[0])
        hourf = int(timef.split(' ')[1].split(':')[0])

        minn = 0xffffff
        maxx = - 0xfffff

        i = 1
        daysum = 0
        while dates < datef:
            while hours < 24:
                hour = str(hours)
                if len(hour) == 1:
                    hour = '0' + hour
                self.sql = 'select `' + self.get[self.ui.attrList.currentIndex()+4] + \
                           '` from tbPRBnew where `网元/基站名称` = \'' + self.ui.webList.currentText() + \
                '\' and 起始时间 like \'07/' + str(dates) + '/2020 ' + hour + '\''
                #print(self.sql)
                self.cursor.execute(self.sql)
                data = self.cursor.fetchall()
                #print(data)
                if(float(data[0][0])<minn) :
                    minn=float(data[0][0])
                if (float(data[0][0]) > maxx):
                    maxx = float(data[0][0])
                series.append(i, data[0][0])
                i += 1
                hours = hours + 1
                daysum+=1
            dates += 1
            hours = 0

        while hours <= hourf:
            hour = str(hours)
            if len(hour) == 1:
                hour = '0' + hour
            self.sql = 'select `' + self.get[self.ui.attrList.currentIndex() + 4] + \
                       '` from tbPRBnew where `网元/基站名称` = \'' + self.ui.webList.currentText() + \
                       '\' and 起始时间 like \'07/' + str(dates) + '/2020 ' + hour + '\''
            #print(self.sql)
            self.cursor.execute(self.sql)
            data = self.cursor.fetchall()
            print(data)
            if (float(data[0][0]) < minn):
                minn = float(data[0][0])
            if (float(data[0][0]) > maxx):
                maxx = float(data[0][0])
            series.append(i, data[0][0])
            i += 1
            hours = hours + 1
            daysum += 1


        self.cursor.close()
        self.db.close()


        y_Aix.setRange(float(minn), float(maxx))
        y_Aix.setLabelFormat("%.3f")
        x_Aix.setRange(time1, time2)
        x_Aix.setTickCount(daysum)
        x_Aix.setFormat("dd/HH")

        self.output = Output.OUTPUT(series, x_Aix, y_Aix)
        self.output.show()


    def prbquery2(self):
        if re.match('^[\u4e00-\u9fa5a-zA-Z0-9]+-[A-Z]+',self.ui.webName.text()):
            pass
        else:
            QMessageBox.warning(self.message, '提示', '名称非法', QMessageBox.Yes)
            return
        if self.ui.webName.text() in self.jud:
            pass
        else:
            QMessageBox.warning(self.message, '提示', '无该网元,请重新输入', QMessageBox.Yes)
            return


        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()

        series = QtCharts.QLineSeries()
        x_Aix = QtCharts.QDateTimeAxis()
        y_Aix = QtCharts.QValueAxis()

        t1 = self.ui.dateTimeEdits.text()
        t2 = self.ui.dateTimeEditf.text()

        times = datetime.strptime(t1, "%Y/%m/%d %H:%M")
        timef = datetime.strptime(t2, "%Y/%m/%d %H:%M")

        if timef < times:
            QMessageBox.warning(self.message, '提示', '时间非法', QMessageBox.Yes)
            return
        if timef == times:
            QMessageBox.warning(self.message, '提示', '仅有一条数据无法绘制折线图', QMessageBox.Yes)
            return

        time1 = QDateTime()
        time1.setDate(
            QDate(int(t1.split('/')[0]), int(t1.split('/')[1].split('/')[0]), int(t1.split('/', 2)[2].split(' ')[0])))
        time1.setTime(QTime(int(t1.split(' ')[1].split(':')[0]), 0))

        time2 = QDateTime()
        time2.setDate(
            QDate(int(t2.split('/')[0]), int(t2.split('/')[1].split('/')[0]), int(t2.split('/', 2)[2].split(' ')[0])))
        time2.setTime(QTime(int(t2.split(' ')[1].split(':')[0]), 0))

        times = t1.split('/')[2]
        dates = int(times.split(' ')[0])
        hours = int(times.split(' ')[1].split(':')[0])
        timef = t2.split('/')[2]
        datef = int(timef.split(' ')[0])
        hourf = int(timef.split(' ')[1].split(':')[0])

        minn = 0xffffff
        maxx = - 0xfffff
        i = 1
        daysum = 0
        while dates < datef:
            while hours < 24:
                hour = str(hours)
                if len(hour) == 1:
                    hour = '0' + hour
                self.sql = 'select `' + self.get[self.ui.attrList.currentIndex() + 4] + \
                           '` from tbPRBnew where `网元/基站名称` = \'' + self.ui.webName.text() + \
                           '\' and 起始时间 like \'07/' + str(dates) + '/2020 ' + hour + '\''
                #print(self.sql)
                self.cursor.execute(self.sql)
                data = self.cursor.fetchall()
                #print(data)
                if (float(data[0][0]) < minn):
                    minn = float(data[0][0])
                if (float(data[0][0]) > maxx):
                    maxx = float(data[0][0])
                series.append(i, data[0][0])
                i += 1
                hours = hours + 1
                daysum += 1
            dates += 1
            hours = 0

        while hours <= hourf:
            hour = str(hours)
            if len(hour) == 1:
                hour = '0' + hour
            self.sql = 'select `' + self.get[self.ui.attrList.currentIndex() + 4] + \
                       '` from tbPRBnew where `网元/基站名称` = \'' + self.ui.webName.text() + \
                       '\' and 起始时间 like \'07/' + str(dates) + '/2020 ' + hour + '\''
            #print(self.sql)
            self.cursor.execute(self.sql)
            data = self.cursor.fetchall()
            #print(data)
            if (float(data[0][0]) < minn):
                minn = float(data[0][0])
            if (float(data[0][0]) > maxx):
                maxx = float(data[0][0])
            series.append(i, data[0][0])
            i += 1
            hours = hours + 1
            daysum += 1
        self.cursor.close()
        self.db.close()
        y_Aix.setRange(float(minn), float(maxx))
        y_Aix.setLabelFormat("%.3f")
        x_Aix.setRange(time1, time2)
        x_Aix.setTickCount(daysum)
        x_Aix.setFormat("dd/HH")

        self.output = Output.OUTPUT(series, x_Aix, y_Aix)
        self.output.show()

    def savefileAddr(self):
        directory, ok = QFileDialog.getSaveFileName(self, "文件保存", "/", "Excel文件 (*.xls);;")
        self.outaddr = directory
        if ok:
            self.fileout()

    # def fileout(self):
    #     self.db = sqlConnect.connectdb()
    #     self.cursor = self.db.cursor()
    #     # 创建新表
    #     # self.cursor.execute("CREATE TABLE tbPRBnew LIKE tbPRB")
    #     book = xlwt.Workbook()
    #     sheet = book.add_sheet('sheet1')
    #
    #     # date = 17
    #     headflag = 0
    #
    #     for hour in range(0, 24):
    #         hours = str(hour)
    #         if len(hours) == 1:
    #             hours = '0' + hours
    #         sql = 'select * from tbPRB where 起始时间 like \'07/17/2020 ' + hours + ':%\''
    #         # print(sql)
    #         self.cursor.execute(sql)
    #
    #         fields = [field[0] for field in self.cursor.description]
    #         alldata = self.cursor.fetchall()
    #
    #         # head
    #         if headflag == 0:
    #             for col, field in enumerate(fields):
    #                 sheet.write(0, col, field)
    #             headflag = 1
    #
    #         i = 0
    #         print(len(alldata))
    #         for data in alldata:
    #             for col, field in enumerate(data):
    #                 if col > 3:
    #                     ##求平均值
    #                     prbvalue = float((alldata[i][col] + alldata[i + 323][col] + alldata[i + 647][col] +
    #                                       alldata[i + 969][col]) / 4)
    #                     sheet.write(i + 1 + hour * 323, col, prbvalue)
    #                 else:
    #                     sheet.write(i + 1 + hour * 323, col, field)
    #             i = i + 1
    #             if i > 322:
    #                 break
    #
    #     # date = 18,hour in range (0, 24)
    #     for hour in range(0, 24):
    #         hours = str(hour)
    #         if len(hours) == 1:
    #             hours = '0' + hours
    #         sql = 'select * from tbPRB where 起始时间 like \'07/18/2020 ' + hours + ':%\''
    #         # print(sql)
    #         self.cursor.execute(sql)
    #
    #         alldata = self.cursor.fetchall()
    #
    #         print(len(alldata))
    #         i = 0
    #         # print(hour)
    #         # print(len(alldata))
    #         for data in alldata:
    #             for col, field in enumerate(data):
    #                 if col > 3:
    #                     ##求平均值
    #                     prbvalue = float((alldata[i][col] + alldata[i + 323][col] + alldata[i + 647][col] +
    #                                       alldata[i + 969][col]) / 4)
    #                     sheet.write(i + 1 + hour * 323 + 7752, col, prbvalue)
    #                 else:
    #                     sheet.write(i + 1 + hour * 323 + 7752, col, field)
    #             i = i + 1
    #             if i > 322:
    #                 break
    #
    #     # date = 19,hour in range (0, 24)
    #     for hour in range(0, 24):
    #         hours = str(hour)
    #         if len(hours) == 1:
    #             hours = '0' + hours
    #         sql = 'select * from tbPRB where 起始时间 like \'07/19/2020 ' + hours + ':%\''
    #         # print(sql)
    #         self.cursor.execute(sql)
    #
    #         alldata = self.cursor.fetchall()
    #
    #         print(len(alldata))
    #         i = 0
    #         # print(hour)
    #         # print(len(alldata))
    #         for data in alldata:
    #             for col, field in enumerate(data):
    #                 if col > 3:
    #                     ##求平均值
    #                     prbvalue = float((alldata[i][col] + alldata[i + 323][col] + alldata[i + 647][col] +
    #                                       alldata[i + 969][col]) / 4)
    #                     sheet.write(i + 1 + hour * 323 + 15504, col, prbvalue)
    #                 else:
    #                     sheet.write(i + 1 + hour * 323 + 15504, col, field)
    #             i = i + 1
    #             if i > 322:
    #                 break
    #
    #     book.save(self.outaddr)
    #     QMessageBox.information(self.message, '提示', '导出成功', QMessageBox.Yes)
    #     self.pg = progressWindow.PWindow()
    #     self.pg.timer.start(100, self.pg)
    #     t1 = threading.Thread(target=self.inNew, args=(self.outaddr,))
    #     t1.start()

    def fileout(self):
        self.db = sqlConnect.connectdb()
        self.cursor = self.db.cursor()
        # 创建新表
        # self.cursor.execute("CREATE TABLE tbPRBnew LIKE tbPRB")
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')

        self.sql ='SELECT SUBSTRING_INDEX(`起始时间`,\':\',1) as s,`网元/基站名称`,'
        for i in range(4,len(self.get)):
            self.sql += 'avg(`'+self.get[i]+'`) as `'+ self.get[i] +'`'
            if (i < len(self.get)-1):
                self.sql +=','

        self.sql += ' from tbPRB group by s,`网元/基站名称`;'

        self.cursor.execute(self.sql)
        fields = [field[0] for field in self.cursor.description]

        for col, field in enumerate(fields):
            if col>0:
                sheet.write(0, col, field)
            else:
                sheet.write(0, col, '起始时间')
        i=0
        alldata = self.cursor.fetchall()
        for data in alldata:
            for col, field in enumerate(data):
                if col > 2:
                    sheet.write(i+1, col, float(alldata[i][col]))
                else:
                    sheet.write(i+1, col, field)
            i+=1

        book.save(self.outaddr)
        self.inNew(self.outaddr)
        QMessageBox.information(self.message, '提示', '导出成功并导入数据库', QMessageBox.Yes)



    def inNew(self, excel_file):
        datapd = pd.read_excel(excel_file)
        db = mysql_link()
        cursor = db.cursor()
        list = []
        std_type = datapd.iloc[1].values
        num = 0

        sql = sql_assemble(std_type, "`tbPRBnew`", datapd.columns.values)
        rnum = len(datapd)
        # print(f'data length of pandas{len(datapd)}')
        # print(datapd.iloc[1])
        for i in range(0, rnum):
            row_data = datapd.iloc[i].values
            flag = type_judgeprb(datapd.iloc[i].values, std_type, i)
            if flag == 0:
                continue
            elif flag == 1:
                rdata = tuple(row_data)
                list.append(rdata)
                num += 1
            if num >= 10000:
                #print("插入10000条数据，到%s" % i)
                cursor.executemany(sql, list)
                list.clear()
                num = 0
                db.commit()
        cursor.executemany(sql, list)
        #print("插入剩余不足10000条的数据，到%s" % i)
        db.commit()
        cursor.close()
        db.close()
