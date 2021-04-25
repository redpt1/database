# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fuction.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import base64
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from one_png import img as one  # 引入img变量，赋别名为one

tmp = open('one.png', 'wb')  # 创建临时的文件
tmp.write(base64.b64decode(one))  ##把这个one图片解码出来，写入文件中去。
tmp.close()
class Ui_fuction(object):
    def setupUi(self, fuction):
        if not fuction.objectName():
            fuction.setObjectName(u"fuction")
        fuction.resize(710, 696)
#if QT_CONFIG(accessibility)
        fuction.setAccessibleName(u"function")
#endif // QT_CONFIG(accessibility)
        fuction.setStyleSheet(u"font-size:24px;\n"
"font-family:sans-serif;\n"
"")
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(fuction.width(), fuction.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        fuction.setPalette(palette)
        self.actionload = QAction(fuction)
        self.actionload.setObjectName(u"actionload")
        self.actionhelp = QAction(fuction)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionabout = QAction(fuction)
        self.actionabout.setObjectName(u"actionabout")
        self.actionaddfriend = QAction(fuction)
        self.actionaddfriend.setObjectName(u"actionaddfriend")
        self.action_app = QAction(fuction)
        self.action_app.setObjectName(u"action_app")
        self.actionexit = QAction(fuction)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(fuction)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"padding:2px 4px;\n"
"border:2px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 70, 441, 541))
        self.verticalLayoutWidget.setStyleSheet("background:transparent;\n")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.sysManButton = QPushButton(self.verticalLayoutWidget)
        self.sysManButton.setObjectName(u"sysManButton")
        font = QFont()
        font.setFamily(u"sans-serif")
        self.sysManButton.setFont(font)
        self.sysManButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.sysManButton)

        self.userManButton = QPushButton(self.verticalLayoutWidget)
        self.userManButton.setObjectName(u"userManButton")
        self.userManButton.setFont(font)
        self.userManButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.userManButton)

        self.dataManButton = QPushButton(self.verticalLayoutWidget)
        self.dataManButton.setObjectName(u"dataManButton")
        self.dataManButton.setFont(font)
        self.dataManButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.dataManButton)

        self.busSearchButton = QPushButton(self.verticalLayoutWidget)
        self.busSearchButton.setObjectName(u"busSearchButton")
        self.busSearchButton.setFont(font)
        self.busSearchButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.busSearchButton)

        self.busAnaButton = QPushButton(self.verticalLayoutWidget)
        self.busAnaButton.setObjectName(u"busAnaButton")
        self.busAnaButton.setFont(font)
        self.busAnaButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.busAnaButton)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 151, 61))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#fff;\n"
"background:transparent;\n"
"font-size:30px;")

        self.verticalLayout_2.addWidget(self.frame)

        fuction.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(fuction)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 30))
        self.menutest = QMenu(self.menubar)
        self.menutest.setObjectName(u"menutest")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        fuction.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(fuction)
        self.statusbar.setObjectName(u"statusbar")
        fuction.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menutest.addAction(self.actionexit)
        self.menu.addAction(self.actionhelp)
        self.menu.addAction(self.actionabout)

        self.retranslateUi(fuction)

        QMetaObject.connectSlotsByName(fuction)
    # setupUi

    def retranslateUi(self, fuction):
        fuction.setWindowTitle(QCoreApplication.translate("fuction", u"MainWindow", None))
        self.actionload.setText(QCoreApplication.translate("fuction", u"\u767b\u5f55", None))
        self.actionhelp.setText(QCoreApplication.translate("fuction", u"\u5e2e\u52a9", None))
        self.actionabout.setText(QCoreApplication.translate("fuction", u"\u5173\u4e8e", None))
        self.actionaddfriend.setText(QCoreApplication.translate("fuction", u"\u6dfb\u52a0\u597d\u53cb", None))
        self.action_app.setText(QCoreApplication.translate("fuction", u"&app", None))
        self.actionexit.setText(QCoreApplication.translate("fuction", u"\u9000\u51fa", None))
        self.sysManButton.setText(QCoreApplication.translate("fuction", u"\u7cfb\u7edf\u7ba1\u7406", None))
        self.userManButton.setText(QCoreApplication.translate("fuction", u"\u7528\u6237\u7ba1\u7406", None))
        self.dataManButton.setText(QCoreApplication.translate("fuction", u"\u6570\u636e\u7ba1\u7406", None))
        self.busSearchButton.setText(QCoreApplication.translate("fuction", u"\u4e1a\u52a1\u67e5\u8be2", None))
        self.busAnaButton.setText(QCoreApplication.translate("fuction", u"\u4e1a\u52a1\u5206\u6790", None))
        self.label.setText(QCoreApplication.translate("fuction", u"\u529f\u80fd\u754c\u9762", None))
        self.menutest.setTitle(QCoreApplication.translate("fuction", u"\u9009\u9879", None))
        self.menu.setTitle(QCoreApplication.translate("fuction", u"\u5e2e\u52a9", None))
    # retranslateUi

