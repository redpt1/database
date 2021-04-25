# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userman.ui'
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

class Ui_userMan(object):
    def setupUi(self, userMan):
        if not userMan.objectName():
            userMan.setObjectName(u"userMan")
        userMan.setWindowModality(Qt.NonModal)
        userMan.setEnabled(True)
        userMan.resize(827, 714)
        userMan.setContextMenuPolicy(Qt.NoContextMenu)
        userMan.setStyleSheet(u"*{\n"
"                font-size:24px;\n"
"                font-family:sans-serif;\n"
"                }\n"
"                Form{\n"
"                background-color:white;\n"
"                }\n"
"                QFrame{\n"
"                background:rgba(255,255,255,255);\n"
"                border-radius:15px;\n"
"                }\n"
"                QPushButton{\n"
"                background:#03a9f4;\n"
"                color:#fff;\n"
"                border-radius:15px;\n"
"                }\n"
"                QLineEdit{\n"
"                border-radius:15px;\n"
"                color:#03a9f4;\n"
"                }\n"
"                QLabel{\n"
"                color:#fff;\n"
"                background:transparent;\n"
"                font-size:30px;\n"
"                }\n"
"            ")
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(userMan.width(), userMan.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        userMan.setPalette(palette)
        self.verticalLayoutWidget = QWidget(userMan)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(490, 410, 260, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.adduserButton = QPushButton(self.verticalLayoutWidget)
        self.adduserButton.setObjectName(u"adduserButton")
        self.adduserButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.adduserButton)

        self.deluserButton = QPushButton(self.verticalLayoutWidget)
        self.deluserButton.setObjectName(u"deluserButton")
        self.deluserButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.deluserButton)

        self.changeauthButton = QPushButton(self.verticalLayoutWidget)
        self.changeauthButton.setObjectName(u"changeauthButton")
        self.changeauthButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.changeauthButton)

        self.widget = QWidget(userMan)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 421, 701))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_5.addWidget(self.listView)

        self.widget1 = QWidget(userMan)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(438, 81, 381, 261))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.userID = QLineEdit(self.widget1)
        self.userID.setObjectName(u"userID")

        self.horizontalLayout_2.addWidget(self.userID)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.userPswd = QLineEdit(self.widget1)
        self.userPswd.setObjectName(u"userPswd")

        self.horizontalLayout_3.addWidget(self.userPswd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.userAuth = QComboBox(self.widget1)
        self.userAuth.addItem("")
        self.userAuth.addItem("")
        self.userAuth.setObjectName(u"userAuth")
        self.userAuth.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.horizontalLayout.addWidget(self.userAuth)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(userMan)

        QMetaObject.connectSlotsByName(userMan)
    # setupUi

    def retranslateUi(self, userMan):
        userMan.setWindowTitle(QCoreApplication.translate("userMan", u"用户信息", None))
        self.adduserButton.setText(QCoreApplication.translate("userMan", u"\u6dfb\u52a0", None))
        self.deluserButton.setText(QCoreApplication.translate("userMan", u"\u5220\u9664", None))
        self.changeauthButton.setText(QCoreApplication.translate("userMan", u"\u4fee\u6539", None))
        self.label.setText(QCoreApplication.translate("userMan", u"\u7528\u6237\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("userMan", u"\u7528\u6237\u540d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("userMan", u"\u5bc6\u7801\uff1a  ", None))
        self.label_3.setText(QCoreApplication.translate("userMan", u"\u6743\u9650\uff1a", None))
        self.userAuth.setItemText(0, QCoreApplication.translate("userMan", u"admin", None))
        self.userAuth.setItemText(1, QCoreApplication.translate("userMan", u"user", None))

    # retranslateUi

