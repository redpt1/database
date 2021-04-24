# # 用户管理界面（只有管理员权限才能进入）
import socket
import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from ui.userman import Ui_userMan
import userSocket
import json
import numpy as np
class userInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_userMan()
        self.ui.setupUi(self)
        self.serverSocket = userSocket.serverSocket  # 信息传输socket
        self.seInfoSocket = userSocket.seInfoSocket  # 验证信息端口
        self.getState = ''
        self.message = QWidget()

        self.ui.adduserButton.clicked.connect(self.adduser)
        self.ui.deluserButton.clicked.connect(self.deluser)
        self.ui.changeauthButton.clicked.connect(self.changeuser)

    def getuserInfo(self):
        getInfo = 'get@'
        self.seInfoSocket.send(getInfo.encode('gbk'))
        self.getState = self.seInfoSocket.recv(1024).decode()
        self.getState = json.loads(self.getState)

        slm=QStringListModel()
        slm.setStringList(np.array(self.getState)[:,0] )
        self.ui.listView.setModel(slm)
        self.ui.listView.clicked.connect(self.click)


    # 点击获得详细信息
    def click(self,qModelIndex):
        a = qModelIndex.row()
        self.ui.userID.setText(self.getState[a][0])
        self.ui.userPswd.setText(self.getState[a][1])
        now = self.ui.userAuth.currentIndex()
        if self.getState[a][2] == 'admin':
            self.ui.userAuth.setItemText(now,'admin')
            self.ui.userAuth.setItemText(1-now, 'user')

        else :
            self.ui.userAuth.setItemText(now, 'user')
            self.ui.userAuth.setItemText(1 - now, 'admin')

    # 添加用户
    def adduser(self):
        adduserId, addpassWrd, addAuth = self.ui.userID.text(), self.ui.userPswd.text() ,self.ui.userAuth.currentText() # 注册的账号密码
        if len(adduserId) == 0 or len(addpassWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self.message, '提示', '请输入合法账号或密码', QMessageBox.Yes)
            return
        else:
            adduserInfo = 'add@' + adduserId + ',' + addpassWrd  +','+addAuth# 加入注册头
            self.seInfoSocket.send(adduserInfo.encode('gbk'))
            adduserState = self.seInfoSocket.recv(6).decode('gbk')
            print(adduserState)
            if adduserState == 'add@OK':
                QMessageBox.information(self.message, '提示', '添加成功', QMessageBox.Yes)
                self.getuserInfo()

            elif adduserState == 'add@NO':
                QMessageBox.warning(self.message, '提示', '添加失败,已经存在该用户', QMessageBox.Yes)
                return

    # 删除用户
    def deluser(self):
        deluserId, delpassWrd = self.ui.userID.text(), self.ui.userPswd.text()  # 注册的账号密码
        if len(deluserId) == 0 or len(delpassWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self.message, '提示', '请输入合法账号或密码', QMessageBox.Yes)
            return
        else:
            deluserInfo = 'del@' + deluserId + ',' + delpassWrd  # 加入注册头和绑定本机ip
            self.seInfoSocket.send(deluserInfo.encode('gbk'))
            deluserState = self.seInfoSocket.recv(6).decode('gbk')
            print(deluserState)
            if deluserState == 'del@OK':
                QMessageBox.information(self.message, '提示', '成功删除用户', QMessageBox.Yes)
                self.getuserInfo()

            elif deluserState == 'del@NO':
                QMessageBox.warning(self.message, '提示', '删除失败，请检查是否存在该账户或者密码输入错误', QMessageBox.Yes)
                return

    # 修改用户
    def changeuser(self):
        chuserId, chpassWrd, chAuth = self.ui.userID.text(), self.ui.userPswd.text(), self.ui.userAuth.currentText()  # 注册的账号密码
        if len(chuserId) == 0 or len(chpassWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self.message, '提示', '请输入合法账号或密码', QMessageBox.Yes)
            return
        else:
            chuserInfo = 'cha@' + chuserId + ',' + chpassWrd + ',' + chAuth  # 加入注册头
            self.seInfoSocket.send(chuserInfo.encode('gbk'))
            chuserState = self.seInfoSocket.recv(6).decode('gbk')
            print(chuserState)
            if chuserState == 'cha@OK':
                QMessageBox.information(self.message, '提示', '更改成功', QMessageBox.Yes)
                self.getuserInfo()

            elif chuserState == 'cha@NO':
                QMessageBox.warning(self.message, '提示', '更改失败', QMessageBox.Yes)
                return