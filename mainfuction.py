from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from loginClass import LoginWindow
from loginClass import SignWindow
from ui.fuction import Ui_fuction
from userManage import userInfo
from dataManage import dataManage
from SYSManage import SYSManage


import socket
import sys
import userSocket

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_fuction()
        self.ui.setupUi(self)
        self.input = LoginWindow()
        self.auth = 0 #权限 1--管理员 ， 0 -- 普通用户
        self.authstr = ''
        self.userId = ''  #账号
        self.passWrd= ''  #密码
        #self.serverSocket = userSocket.serverSocket #信息传输socket
        self.seInfoSocket = userSocket.seInfoSocket #验证信息端口
        self.userinfo = userInfo()
        self.dataman = dataManage()

        self.sysman = SYSManage()


        # 信号与槽
        self.ui.actionexit.triggered.connect(self.systemQuitFunc)
        self.ui.actionabout.triggered.connect(self.programAbout)
        self.ui.actionhelp.triggered.connect(self.programHelp)
        self.ui.userManButton.clicked.connect(self.usermanage)
        self.ui.dataManButton.clicked.connect(self.datamanage)

        self.ui.sysManButton.clicked.connect(self.sysmanshow)

        self.socketCheck()
        self.userLoginFunc()

    def socketCheck(self):
        try:
            #self.serverSocket.connect(('10.128.246.121', 1081))
            self.seInfoSocket.connect(('10.128.246.121', 1082))
            return True
        except socket.error as e:
            QMessageBox.warning(self, '警告', '请检测网络连接', QMessageBox.Yes)
            sys.exit(0)

    #数据管理
    def sysmanshow(self):
        if self.auth == 1:
            self.sysman.show()
        elif self.auth == 0:
            QMessageBox.warning(
                self,
                '提示',
                '只有管理员身份才能进入该界面',
                QMessageBox.Yes, QMessageBox.Yes
            )

    def programHelp(self):
         QMessageBox.information(
            self,
            '软件说明',
            '数据库系统\n'
            , QMessageBox.Yes, QMessageBox.Yes)

    def programAbout(self):
         QMessageBox.information(
            self,
            '关于',
            '开发人员 :lhb,lxr,zxy', QMessageBox.Yes, QMessageBox.Yes)

    #退出功能
    def systemQuitFunc(self):
        QCoreApplication.instance().quit()

     #状态显示
    def showCurrentStatus(self):

        if self.auth == 1:
            self.authstr = '管理员'
        elif self.auth == 0:
            self.authstr = '普通用户'

        self.statusbarShow('用户名: ' + str(self.userId) + '    权限: ' + self.authstr)

    def statusbarShow(self, string):
        self.ui.statusbar.showMessage(str(string), 0)
        self.ui.statusbar.setStyleSheet("background:rgba(255,255,255,255);")


    def event(self, QEvent):
        if QEvent.type() == QEvent.StatusTip:
            if QEvent.tip() == "":
                QEvent = QStatusTipEvent('用户名: ' + str(self.userId) + '    权限: ' + self.authstr)  # 此处为要始终显示的内容
        return super().event(QEvent)


    '''用户注册及注销(需要管理员权限才能登录)'''
    def signInWindow(self):
        self.sign = SignWindow()
        # 两个按钮的槽函数
        self.sign.ui.signButton.clicked.connect(self.signinAccept)
        self.sign.ui.delButton.clicked.connect(self.delUser)
        self.sign.show()

    #只有管理员权限才能进入该界面
    def userSignFunc(self):
        userId = self.input.ui.loginID.text()
        passWrd = self.input.ui.loginPswd.text()
        if len(userId) == 0 or len(passWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self, '提示', '只有管理员身份才能进入该界面', QMessageBox.Yes)
            self.userLoginFunc()
            return
        else:
            userInfo = 'mmt@' + userId + ',' + passWrd  # 加入密码头
            self.seInfoSocket.send(userInfo.encode('gbk'))
            userState = self.seInfoSocket.recv(7).decode('gbk')
            print(userState)
            if userState == 'mmt@OK1':
                QMessageBox.information(self, '欢迎', '管理员,您可以对用户进行注册注销操作', QMessageBox.Yes)
                self.userId = userId
                self.passWrd = passWrd
                self.signInWindow()

            elif userState == 'mmt@OK2':
                QMessageBox.warning(self, '提示', '只有管理员身份才能进入该界面', QMessageBox.Yes)
                self.userLoginFunc()
                return

            elif userState == 'mmt@NO':
                QMessageBox.critical(self, '提示', '请输入正确的账号或密码', QMessageBox.Yes)
                self.userLoginFunc()
                return


    def signinAccept(self):
        siuserId, sipassWrd = self.sign.ui.signID.text(), self.sign.ui.signPswd.text() #注册的账号密码
        if len(siuserId) == 0 or len(sipassWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self, '提示', '请注册合法账号或密码', QMessageBox.Yes)
            self.userSignFunc()
            return
        else:
            siuserInfo = 'zc@' + siuserId + ',' + sipassWrd # 加入注册头和绑定本机ip
            self.seInfoSocket.send(siuserInfo.encode('gbk'))
            siuserState = self.seInfoSocket.recv(5).decode('gbk')
            print(siuserState)
            if siuserState == 'zc@OK':
                QMessageBox.information(self, '提示', '注册成功', QMessageBox.Yes)
                self.sign.close()


            elif siuserState == 'zc@NO':
                QMessageBox.warning(self, '提示', '注册失败,已经存在该用户', QMessageBox.Yes)
                self.signInWindow()
                return

    def delUser(self):
        deluserId, delpassWrd = self.sign.ui.signID.text(), self.sign.ui.signPswd.text()  # 注册的账号密码
        if len(deluserId) == 0 or len(delpassWrd) == 0:  # 如果非法输入
            QMessageBox.warning(self, '提示', '请输入合法账号或密码', QMessageBox.Yes)
            self.userSignFunc()
            return
        else:
            deluserInfo = 'del@' + deluserId + ',' + delpassWrd  # 加入注册头和绑定本机ip
            self.seInfoSocket.send(deluserInfo.encode('gbk'))
            deluserState = self.seInfoSocket.recv(6).decode('gbk')
            print(deluserState)
            if deluserState == 'del@OK':
                QMessageBox.information(self, '提示', '成功注销用户', QMessageBox.Yes)
                self.sign.close()
            elif deluserState == 'del@NO':
                QMessageBox.warning(self, '提示', '注销失败，请检查是否存在该账户或者密码输入错误', QMessageBox.Yes)
                self.signInWindow()
                return

  ######################################################################
    '''用户登录认证'''
    def userLoginFunc(self):
        self.input = LoginWindow()
        self.input.ui.loginPswd.setEchoMode(QLineEdit.Password)  # 设置掩码模式
        # 两个按钮的槽函数
        self.input.ui.loginButton.clicked.connect(self.loginAccept)
        self.input.ui.signinButton.clicked.connect(self.userSignFunc)
        self.input.show()

    def loginAccept(self):
        userId = self.input.ui.loginID.text()
        passWrd = self.input.ui.loginPswd.text()
        if len(userId)==0 or len(passWrd)==0: #如果非法输入
            QMessageBox.warning(self, '提示', '请输入账号或密码', QMessageBox.Yes)
            self.userLoginFunc()
            return
        else:
            userInfo ='mmt@'+userId +','+ passWrd #加入密码头
            self.seInfoSocket.send(userInfo.encode('gbk'))
            userState = self.seInfoSocket.recv(7).decode('gbk')
            print(userState)
            if userState =='mmt@OK1'  :
                QMessageBox.information(self, '欢迎', '您好，管理员', QMessageBox.Yes)
                self.userId = userId
                self.passWrd = passWrd
                self.auth = 1
                self.loginSuccess()
            elif userState =='mmt@OK2'  :
                QMessageBox.information(self, '欢迎', '您好， 普通用户', QMessageBox.Yes)
                self.userId = userId
                self.passWrd = passWrd
                self.loginSuccess()
            elif userState == 'mmt@NO':
                QMessageBox.critical(self, '提示', '请输入正确的账号或密码', QMessageBox.Yes)
                self.userLoginFunc()
                return

    def loginSuccess(self):
        self.input.close()
        self.show()
        self.showCurrentStatus()



    ############################################################################
        # 用户管理操作
    def usermanage(self):
        if self.auth == 1 :
            self.userinfo=userInfo()
            self.userinfo.show()
            self.userinfo.getuserInfo()
        else :
            QMessageBox.warning(self, '提示', '只有管理员身份才能进入该界面', QMessageBox.Yes)


        #数据管理操作
    def datamanage(self):
        if self.auth == 1 :
            self.dataman = dataManage()
            self.dataman.show()
        else :
            QMessageBox.warning(self, '提示', '只有管理员身份才能进入该界面', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication([])
    mainw = MainWindow()
    mainw.setWindowTitle('数据库')

    app.exec_()
