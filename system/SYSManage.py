from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sqlConnect
from sysman import Ui_SYSMAN
from system.MODIFY import SYSMODIFY


class SYSManage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SYSMAN()
        self.ui.setupUi(self)
        self.config = ''
        self.configshow = QTextBrowser()
        self.configshow.setStyleSheet(
            u"background:white;\n"
            "font-size:20px;"
        )
        self.configshow.setFixedSize(500, 600)
        self.configshow.setWindowTitle('数据库配置信息')

        self.modify = SYSMODIFY()
        self.ui.databaseconfigButton.clicked.connect(self.sys_databaseconfig)
        self.ui.databasemodifyButton.clicked.connect(self.sys_databasemodify)




    def sys_databaseconfig(self):

        db = sqlConnect.connectdb()
        cursor = db.cursor()

        ##数据库连接数
        execute = 'show processlist'
        connect = 0
        cursor.execute(execute)
        results = cursor.fetchall()

        self.configshow.clear()
        for row in results:
            connect += 1

        self.configshow.append('数据库连接：' + str(connect) + '\n')
        ##

        ##数据库服务器
        self.configshow.append('数据库服务器：39.102.140.167\n')
        ##

        ##数据库配置
        self.configshow.append('数据库配置：')
        execute = 'show global variables'
        cursor.execute(execute)
        results = cursor.fetchall()
        for row in results:
            self.configshow.append(str(row[0]) + '  ' + str(row[1]))
        ##

        c = self.configshow.textCursor()
        QTextCursor.setPosition(c, 0)
        self.configshow.setTextCursor(c)

        self.configshow.show()

        cursor.close()
        db.close()

    def sys_databasemodify(self):
        self.modify.ui.lineEdit.clear()
        self.modify.ui.lineEdit_2.clear()
        self.modify.show()
