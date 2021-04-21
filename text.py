from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from ui.mainwindow import Ui_MainWindow
from ui.login import Ui_Form
import pygame
import base64
from music_mp3 import music as music  # 引入img变量，赋别名为one


import Russia

import socket
import threading
import time
import numpy as np
import re
import sqlite3

tmp = open('music.mp3', 'wb')  # 创建临时的文件

tmp.write(base64.b64decode(music))  ##把这个one图片解码出来，写入文件中去。
tmp.close()
class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        file = r'./music.mp3'  # 音乐的路径
        pygame.mixer.init()  # 初始化
        track = pygame.mixer.music.load(file)  # 加载音乐文件
        pygame.mixer.music.play()  # 开始播放音乐流

        # self.ui.loginButton.setShortcut('enter')
        # self.ui.loginButton.setShortcut('ctrl+return')

    def loginFunc(self):
        return {'ID': self.ui.loginID.text()}


class MainWindow(QMainWindow):
    textSendSignal = Signal(QPushButton, str, QColor)
    textClearSignal = Signal(QPushButton, str, QColor)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.input = LoginWindow()

        self.hostIp = str(localIP())  # 10.128.248.94
        self.hostPort = 1080
        self.userId = ''  #账号
        self.passWrd= ''  #密码
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 信息传输socket
        self.serverSocket.connect(('10.128.246.121', 1081))
        self.seInfoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #验证信息端口
        self.seInfoSocket.connect(('10.128.246.121', 1082))
        # (begin) 数据库添加 ========
        self.friendList = [['好友列表']]
        self.initSQL()
        #  (end)  数据库添加 ========

        # （begin）列表--------
        # 列表加载
        slm = QStringListModel();  # 创建mode
        slm.setStringList(np.array(self.friendList)[:,0])  # 将数据设置到model

        # 列表右键拓展
        self.ui.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listView.customContextMenuRequested[QPoint].connect(self.listWidgetContext)
        self.ui.listView.setModel(slm)  # 绑定 listView 和 model
        # （end）列表--------

        # 信号与槽
        self.textSendSignal.connect(self.printToGui)
        self.textClearSignal.connect(self.clearToGui)
        self.ui.SendButton.clicked.connect(self.threadOfSendMessage)
        self.ui.ResetButton.clicked.connect(self.clearSendText)
        self.ui.listView.clicked.connect(self.clickedlist)
        self.ui.actionexit.triggered.connect(self.systemQuitFunc)
        self.ui.actionaddfriend.triggered.connect(self.addFriendFunc)
        self.ui.actionabout.triggered.connect(self.programAbout)
        self.ui.actionhelp.triggered.connect(self.programHelp)

        self.ui.actionstop.triggered.connect(self.myStop)
        self.ui.actioncontinue.triggered.connect(self.myContinue)

        self.ui.actionrussia.triggered.connect(Russia.main)


        # 监听窗口线程
        self.thr = threading.Thread(target=self.recvMessageFunc)
        self.thr.daemon = 1
        self.thr.start()

        self.ShortcutSetting()

        self.userLoginFunc()
  #初始化数据库======================
    def initSQL(self):
        self.con = sqlite3.connect('friend.db',check_same_thread= False)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS FRIENDS(FRIENDID TEXT NOT NULL,FRIENDIP TEXT NOT NULL);")
        self.con.commit()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS CHAT(
                              FROMID TEXT NOT NULL,
                              TOID TEXT NOT NULL,
                              TIME TEXT NOT NULL,
                              INFO TEXT NOT NULL);''')
        self.con.commit()
        cursor = self.cur.execute("SELECT FRIENDID FROM FRIENDS")
        for row in cursor:
            self.friendList.append([str(row[0])])  # 添加的数组数据
            print(self.friendList)
 #初始化数据库===========
    def programHelp(self):
        choice = QMessageBox.information(
            self,
            '快捷键说明',
            '  Ctrl+Q    :  退出\n'
            'Ctrl+Enter  :  发送', QMessageBox.Yes, QMessageBox.Yes)

    def programAbout(self):
        choice = QMessageBox.information(
            self,
            '关于',
            '开发人员 :lhb,yz,zxy', QMessageBox.Yes, QMessageBox.Yes)

    def listWidgetContext(self, point):
        listRightMenu = QMenu(self.ui.listView)

        addAction = QAction(u"添加", self, triggered=self.addFriendFunc)  # 也可以指定自定义对象事件
        alterAction = QAction(u"修改", self, triggered=lambda: self.alterFriendFunc())  # 也可以指定自定义对象事件
        removeAction = QAction(u"删除", self, triggered=lambda: self.deleteFriendFunc())  # 也可以指定自定义对象事件
        # //or  removeAction.triggered.connect(lambda:self.deleteFriendFunc(point))
        listRightMenu.addAction(addAction)
        listRightMenu.addAction(alterAction)
        listRightMenu.addAction(removeAction)
        listRightMenu.exec_(QCursor.pos())

    def systemQuitFunc(self):
        self.con.close()
        QCoreApplication.instance().quit()


   # 点击列表中好友，显示聊天记录=============
    def clickedlist(self, qModelIndex):
        id = self.friendList[qModelIndex.row()][0]
        self.showCurrentStatus()
        print("clicked", id)
        cursor = self.cur.execute("SELECT FROMID,TOID,TIME,INFO FROM CHAT WHERE (FROMID=:fromID AND TOID=:selfID) OR (FROMID=:selfID AND TOID=:toID) ;",{"fromID": id, "toID": id,"selfID":self.userId})

        self.con.commit()
        self.clearToGui(self.ui.textBrowser, '', 'black')
        for row in cursor:
            self.textSendSignal.emit(self.ui.textBrowser, row[0] + '  ' + row[2], 'gray')
            self.textSendSignal.emit(self.ui.textBrowser, '  ' + row[3], 'gray')

    def prt_sql(self):
        conn = sqlite3.connect('friend.db')
        c = conn.cursor()
        c.execute("select * from CHAT;")
        columns_tuple = c.fetchall()
        print(columns_tuple)
        conn.commit()
        conn.close()

    def printToGui(self, object, text, textColor):
        object.setTextColor(QColor(textColor))
        object.append(str(text))

    def clearToGui(self, object, remindMessage, messageColor):
        object.setText('')
        object.setPlaceholderText(str(remindMessage))

    def clearSendText(self):
        self.textClearSignal.emit(self.ui.textEdit, '', 'black')

    def threadOfSendMessage(self):
        ts = threading.Thread(target=self.sendMessageFunc)
        ts.start()


   #(begin)收发数据================
    def recvMessageFunc(self):
        selectindex = self.ui.listView.currentIndex()
        pos = selectindex.row()
        toID = str(self.friendList[pos][0])
        selfSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 验证信息端口
        selfSocket.bind((self.hostIp, self.hostPort))
        selfSocket.listen(1)
        while True:
            cliSocket, addr=selfSocket.accept()
            print(addr)
            recvData = cliSocket.recv(1024)
            recvFromID,recvToid,recvTime,recvInfo = recvData.decode('gbk').split(',',3)
            print(recvFromID,recvToid,recvTime,recvInfo)
            self.cur.execute("INSERT INTO CHAT (FROMID,TOID,TIME,INFO) VALUES (?,?,?,?)",
                             (recvFromID,recvToid, recvTime, recvInfo))
            self.con.commit()
            self.prt_sql()
            if recvToid == self.userId:
                recv_time = recvTime
                self.textSendSignal.emit(self.ui.textBrowser, recvFromID+ '  ' + recv_time, 'red')
                self.textSendSignal.emit(self.ui.textBrowser, '  ' + recvInfo, 'black')
                print("收到了消息%s:%s" % (str(recvFromID), recvInfo))


    def sendMessageFunc(self):
        sendMsg = self.ui.textEdit.toPlainText()
        selectindex = self.ui.listView.currentIndex()
        pos = selectindex.row()
        toID = str(self.friendList[pos][0]) #获取toID
        print(toID)
        print(self.userId)
        if (sendMsg):
            sendTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            self.textSendSignal.emit(self.ui.textBrowser, self.userId + '  ' + sendTime + ' [本地]', '#87CEEB')
            self.textSendSignal.emit(self.ui.textBrowser, '  ' + sendMsg, 'black')
            self.textClearSignal.emit(self.ui.textEdit, '', 'black')

            self.cur.execute("INSERT INTO CHAT (FROMID,TOID,TIME,INFO) VALUES (?,?,?,?)",
                             (self.userId,toID,str(sendTime),str(sendMsg)))
            self.con.commit()
            sendInfo=self.userId+','+toID+','+str(sendTime)+','+str(sendMsg)
            try:
                self.serverSocket.send(sendInfo.encode("gbk"))
            except Exception as e:
                self.statusbarShow(e)
            except OSError as osE:
                self.statusbarShow(osE)
            except:
                pass
        else:
            self.textClearSignal.emit(self.ui.textEdit, '输入不能为空', 'black')
   #(end)收发数据==========================

    # (begin) 快捷键设置------------
    def ShortcutSetting(self):
        QShortcut(QKeySequence(self.tr('Ctrl+Q')), self, self.close)
        self.ui.SendButton.setShortcut('ctrl+return')
        self.ui.SendShortcut.currentIndexChanged.connect(self.setSendButtonShortcut)
        self.input.ui.loginButton.setShortcut('Enter')

    def setSendButtonShortcut(self):
        change = self.ui.SendShortcut.currentText()
        if change == 'Ctrl+Enter':
            self.ui.SendButton.setShortcut(change.replace('Enter', 'return'))
        elif change == 'Enter':
            QShortcut(QKeySequence(self.tr('return')), self, self.ui.SendButton.click)
    #  (end)  快捷键设置------------


    # (begin)  old ========
    def accept(self, object):
        self.setHostIP(object.ui.loginIP.text())
        self.setHostPort(object.ui.loginPort.text())

    def childAccept(self):
        self.accept(self.input)
        self.show()
        self.clearToGui(self.input.ui.loginID, '', 'black')
        self.clearToGui(self.input.ui.loginPswd, '', 'black')
        # self.child.ui.loginIP.setText()
        self.input.close()

    #  (end)  old ========
    def showCurrentStatus(self):
        self.statusbarShow('Login ID: ' + str(self.userId) + '    IP:' + str(self.hostIp))


    def statusbarShow(self, string):
        self.ui.statusbar.showMessage(str(string), 0)

    # (begin) 用户登录 ========
    def userLoginFunc(self):
        self.input = LoginWindow()
        self.input.ui.loginPswd.setEchoMode(QLineEdit.Password)#设置掩码模式
        self.input.ui.loginButton.setShortcut('Enter')#设置快捷键
        self.input.show()
       #两个按钮的槽函数
        self.input.ui.loginButton.clicked.connect(self.loginAccept)
        self.input.ui.signinButton.clicked.connect(self.signinAccept)

    def myStop(self):
        pygame.mixer.init()
        pygame.mixer.music.pause()

    def myContinue(self):
        pygame.mixer.init()
        pygame.mixer.music.unpause()

    #(begin) 用户登录认证========
    def loginAccept(self):
        userId, passWrd = self.input.ui.loginID.text(), self.input.ui.loginPswd.text()
        if len(userId)==0 or len(passWrd)==0: #如果非法输入
            self.input.close()
            QMessageBox.warning(self, '提示', '请输入账号或密码', QMessageBox.Yes)
            self.userLoginFunc()
            return
        else:
            userInfo ='mmt@'+userId +','+ passWrd #加入密码头
            self.seInfoSocket.send(userInfo.encode('gbk'))
            userState = self.seInfoSocket.recv(6).decode('gbk')
            print(userState)
            if userState =='mmt@OK'  :
                self.userId = userId
                self.passWrd = passWrd
            elif userState == 'mmt@NO':
                self.input.close()
                QMessageBox.warning(self, '提示', '请输入正确的账号或密码', QMessageBox.Yes)
                self.userLoginFunc()
                return
        self.input.close()
        self.show()
        self.printToGui(self.ui.textBrowser, '单击左侧列表开启聊天系统，右键打开拓展菜单\n', 'black')
        self.statusbarShow('Login ID: ' + str(userId) + '    IP:' + str(self.hostIp))#显示当前登录账号及ip
    #(end)用户登录验证========

    # (begin)用户注册========
    def signinAccept(self):
        siuserId, sipassWrd = self.input.ui.loginID.text(), self.input.ui.loginPswd.text() #注册的账号密码
        if len(siuserId) == 0 or len(sipassWrd) == 0:  # 如果非法输入
            self.input.close()
            QMessageBox.warning(self, '提示', '请注册合法账号或密码', QMessageBox.Yes)
            self.userLoginFunc()
            return
        else:
            siuserInfo = 'zc@' + siuserId + ',' + sipassWrd + ',' + str(self.hostIp) # 加入注册头和绑定本机ip
            self.seInfoSocket.send(siuserInfo.encode('gbk'))
            siuserState = self.seInfoSocket.recv(5).decode('gbk')
            print(siuserState)
            if siuserState == 'zc@OK':
                QMessageBox.warning(self, '提示', '注册成功并已经登录', QMessageBox.Yes)
                self.userId = siuserId
                self.passWrd = sipassWrd
            elif siuserState == 'zc@NO':
                self.input.close()
                QMessageBox.warning(self, '提示', '注册失败', QMessageBox.Yes)
                self.userLoginFunc()
                return
        self.input.close()
        self.show()
        self.printToGui(self.ui.textBrowser, '单击左侧列表开启聊天系统，右键打开拓展菜单\n', 'black')
        self.statusbarShow('ID: ' + str(siuserId) + '   IP:' + str(self.hostIp))  # 显示当前登录账号及ip
    #  (end)  用户注册 ========

    # (begin) 增加好友功能 ========
    def addFriendFunc(self):
        self.input = LoginWindow()
        self.input.ui.label.setText('添加好友')
        self.input.ui.loginButton.setText('添加')
        self.input.ui.loginButton.colorCount()
        self.input.ui.loginID.setPlaceholderText('好友账号')
        self.input.ui.loginPswd.setVisible(False) #设为不可见
        self.input.ui.loginButton.setShortcut('Enter')
        self.input.ui.signinButton.setText('关闭')
        self.input.show()

        self.input.ui.loginButton.clicked.connect(self.addFriendAccept)
        self.input.ui.signinButton.clicked.connect(self.closeFriendFunc)

    def closeFriendFunc(self): #关闭添加好友框
        self.input.close()

    def addFriendAccept(self):
        seInfoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        seInfoSocket.connect(('10.128.248.94', 1082))
        friendID = self.input.ui.loginID.text()
        if len(friendID)==0:
            self.input.close()
            QMessageBox.warning(self, '警告', '请输入正确的账号', QMessageBox.Yes)
            self.addFriendFunc()
            return
        else:
            addInfo = 'add@' + friendID
            seInfoSocket.send(addInfo.encode('gbk'))
            addState = seInfoSocket.recv(6).decode('gbk')
            if addState == 'add@OK':
                QMessageBox.warning(self, '提示', '成功添加好友！', QMessageBox.Yes)
                friendIP =seInfoSocket.recv(15).decode('gbk')
                self.cur.execute("INSERT INTO FRIENDS(FRIENDID,FRIENDIP) VALUES (?,?)",(friendID,friendIP))
                self.con.commit()
                self.friendList.append([friendID])
                print("addFriendAccept", friendID,friendIP)
            elif addState == 'add@NO':
                self.input.close()
                QMessageBox.warning(self, '提示', '添加失败，请检查账号是否正确', QMessageBox.Yes)
                self.addFriendFunc()
                return
        print('frindList:', self.friendList)
        itemmodel = self.ui.listView.model()  # 取数据存储数据条数
        count = itemmodel.rowCount()  # count为列表单项的总数
        selectindex = self.ui.listView.currentIndex()  # 取当前选择的数据项位置
        Pos = count  # 当前没有选择则插入到最后位置
        itemmodel.insertRow(Pos)  # 执行插入位置列表项元素扩充
        index = itemmodel.index(Pos, 0)  # 取插入位置的元素项
        stritem = friendID  # 设置插入内容
        itemmodel.setData(index, stritem, Qt.DisplayRole)  # 将内容更新到插入位置
        self.input.close()
        self.showCurrentStatus()
    #  (end)  增加好友功能 ========


    # (begin) 修改好友备注名 ========
    def alterFriendFunc(self):
        selectindex = self.ui.listView.currentIndex()
        pos = selectindex.row()
        ID= str(self.friendList[pos][0])
        self.input = LoginWindow()
        self.input.ui.label.setText('修改备注')
        self.input.ui.loginButton.setText('修改')
        self.input.ui.loginButton.colorCount()
        self.input.ui.loginID.setText(ID)
        self.input.ui.loginPswd.setVisible(False)
        self.input.ui.signinButton.setText('关闭')
        self.input.ui.loginButton.setShortcut('Enter')

        self.input.show()
        self.input.ui.loginButton.clicked.connect(lambda:self.alterFriendAccept(pos))
        self.input.ui.signinButton.clicked.connect(self.closeAlterFriend)

    def closeAlterFriend(self):
        self.input.close()


    def alterFriendAccept(self, Pos):
        selectindex = self.ui.listView.currentIndex()
        pos = selectindex.row()
        oldId = str(self.friendList[pos][0])
        alterFriendId = self.input.ui.loginID.text()

        if len(alterFriendId)==0:
            self.input.close()
            QMessageBox.warning(self, '警告', '请输入合法备注', QMessageBox.Yes)
            self.alterFriendFunc()
            return
        self.cur.execute("UPDATE FRIENDS SET FRIENDID = :newid WHERE FRIENDID = :oldid", {"newid":alterFriendId,"oldid":oldId})
        self.con.commit()
        itemmodel = self.ui.listView.model()
        index = itemmodel.index(Pos, 0)  # 取插入位置的元素项
        stritem = alterFriendId # 设置插入内容
        itemmodel.setData(index, stritem, Qt.DisplayRole)  # 将内容更新到插入位置
        self.input.close()
    #  (end)  修改好友功能 ========


    # (begin) 删除好友功能 ========
    def deleteFriendFunc(self):
        selectindex = self.ui.listView.currentIndex()
        itemmodel = self.ui.listView.model()
        if selectindex.isValid():
            Pos = selectindex.row()
            print("pos=", Pos)  # 取当前选择的数据项位置的顺序索引
        else:
            print("空选项")
            return
        if Pos == 0:
            return
        itemmodel.removeRow(Pos)
        self.cur.execute("DELETE FROM FRIENDS WHERE FRIENDID=:ID;",
                         {"ID": self.friendList[Pos][0]})
        self.con.commit()
        self.friendList.pop(Pos)
    #  (end)  删除好友功能 ========

    # 测试函数 ========
    def testprint(self):
        print("in test")





def localIP():
    hostname = socket.gethostname()
    print("Host name: %s" % hostname)
    sysinfo = socket.gethostbyname_ex(hostname)
    ip_addr = sysinfo[2]
    return ip_addr[-1]


def main():
    app = QApplication([])

    mainw = MainWindow()
    mainw.setWindowTitle('QO')
    # mainw.show()

    app.exec_()


if __name__ == '__main__':
    main()
