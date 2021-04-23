# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign.ui'
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

class Ui_sign(object):
    def setupUi(self, sign):
        if not sign.objectName():
            sign.setObjectName(u"sign")
        sign.setWindowModality(Qt.NonModal)
        sign.setWindowFlags(Qt.FramelessWindowHint)
        sign.setEnabled(True)
        sign.resize(600, 500)
        sign.setContextMenuPolicy(Qt.NoContextMenu)
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(sign.width(), sign.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        sign.setPalette(palette)
        sign.setStyleSheet(u"*{\n"
"                font-size:24px;\n"
"                font-family:sans-serif;\n"
"                }\n"
"                Form{\n"
"                background-color:white;\n"
"                }\n"
"                QFrame{\n"
"                background:rgba(0,0,0,0.8);\n"
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
        self.frame = QFrame(sign)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 80, 400, 300))
        self.frame.setStyleSheet(u"border:2px;\n"
"border-radius:5px;\n"
"padding:2px 4px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 200, 40))
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 170, 171, 121))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.signButton = QPushButton(self.verticalLayoutWidget)
        self.signButton.setObjectName(u"signButton")
        self.signButton.setStyleSheet(u"border:2px white;\n"
"border-radius:5px;\n"
"padding:2px 4px;\n"
"color:rgb(0, 0, 0)")

        self.verticalLayout_2.addWidget(self.signButton)

        self.delButton = QPushButton(self.verticalLayoutWidget)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setStyleSheet(u"border-radius:5px;\n"
"padding:2px 4px;\n"
"border:2px white;\n"
"color:0x000000;")

        self.verticalLayout_2.addWidget(self.delButton)

        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 50, 361, 121))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.signID = QLineEdit(self.verticalLayoutWidget_2)
        self.signID.setObjectName(u"signID")
        self.signID.setStyleSheet(u"border:2px;\n"
"border-radius:5px;\n"
"padding:2px 4px;\n"
"color:gray")

        self.verticalLayout_3.addWidget(self.signID)

        self.signPswd = QLineEdit(self.verticalLayoutWidget_2)
        self.signPswd.setObjectName(u"signPswd")
        self.signPswd.setStyleSheet(u"border:2px;\n"
"border-radius:5px;\n"
"padding:2px 4px;\n"
"color:gray")

        self.verticalLayout_3.addWidget(self.signPswd)


        self.retranslateUi(sign)

        QMetaObject.connectSlotsByName(sign)
    # setupUi

    def retranslateUi(self, sign):
        sign.setWindowTitle(QCoreApplication.translate("sign", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("sign", u"\u6ce8\u518c/\u6ce8\u9500", None))
        self.signButton.setText(QCoreApplication.translate("sign", u"\u6ce8\u518c", None))
        self.delButton.setText(QCoreApplication.translate("sign", u"\u6ce8\u9500\u8d26\u6237", None))
        self.signID.setPlaceholderText(QCoreApplication.translate("sign", u"\u8d26\u53f7", None))
        self.signPswd.setText("")
        self.signPswd.setPlaceholderText(QCoreApplication.translate("sign", u"\u5bc6\u7801", None))
    # retranslateUi

