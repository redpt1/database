from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from ui.userman import Ui_userMan
import userSocket

from configmodify import Ui_MODIFY


class SYSMODIFY(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MODIFY()
        self.ui.setupUi(self)
        self.ui.databaseconfigButton.clicked.connect(self.commit)
        self.connecttime = ''
        self.buffersize = ''


    def commit(self):
        self.connecttime = self.ui.lineEdit.text()
        self.buffersize = self.ui.lineEdit_2.text()

        if (len(self.connecttime) != 0 and not self.connecttime.isdigit()) or (len(self.buffersize) != 0 and not self.buffersize.isdigit()):
            # 出错提示
            QMessageBox.information(
                self,
                '提示',
                '配置格式非法，请检查格式',
                QMessageBox.Yes, QMessageBox.Yes
                )
            return

        if len(self.connecttime) == 0 and len(self.buffersize) == 0:
            # 出错提示
            QMessageBox.information(
                self,
                '提示',
                '输入为空，请重新输入',
                QMessageBox.Yes, QMessageBox.Yes
            )
            return


        else:
            if len(self.connecttime) != 0:
                execute = 'set global wait_timeout ='+str(self.connecttime)
                userSocket.cursor.execute(execute)

            if len(self.buffersize) != 0:
                execute = 'set global key_buffer_size ='+str(self.buffersize)
                userSocket.cursor.execute(execute)

            QMessageBox.information(
                self,
                '提示',
                '数据库配置修改成功',
                QMessageBox.Yes, QMessageBox.Yes
            )