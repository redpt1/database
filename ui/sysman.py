# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysman.ui'
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


class Ui_SYSMAN(object):
    def setupUi(self, SYSMAN):
        if not SYSMAN.objectName():
            SYSMAN.setObjectName(u"SYSMAN")
        SYSMAN.resize(490, 554)
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(SYSMAN.width(), SYSMAN.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        SYSMAN.setPalette(palette)
        self.verticalLayout_2 = QVBoxLayout(SYSMAN)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(SYSMAN)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background:transparent;\n"
"border-radius:15px;\n"
"padding:2px 4px;\n"
"border:2px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 200, 61))
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#fff;\n"
"background:transparent;\n"
"font-size:30px;")
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 170, 245, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.databaseconfigButton = QPushButton(self.verticalLayoutWidget)
        self.databaseconfigButton.setObjectName(u"databaseconfigButton")
        self.databaseconfigButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.databaseconfigButton.sizePolicy().hasHeightForWidth())
        self.databaseconfigButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        self.databaseconfigButton.setFont(font1)
        self.databaseconfigButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.databaseconfigButton)

        self.databasemodifyButton = QPushButton(self.verticalLayoutWidget)
        self.databasemodifyButton.setObjectName(u"databasemodifyButton")
        sizePolicy1.setHeightForWidth(self.databasemodifyButton.sizePolicy().hasHeightForWidth())
        self.databasemodifyButton.setSizePolicy(sizePolicy1)
        self.databasemodifyButton.setFont(font1)
        self.databasemodifyButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")

        self.verticalLayout.addWidget(self.databasemodifyButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(SYSMAN)

        QMetaObject.connectSlotsByName(SYSMAN)
    # setupUi

    def retranslateUi(self, SYSMAN):
        SYSMAN.setWindowTitle(QCoreApplication.translate("SYSMAN", u"系统管理", None))
        self.label.setText(QCoreApplication.translate("SYSMAN", u"\u7cfb\u7edf\u7ba1\u7406\u754c\u9762", None))
        self.databaseconfigButton.setText(QCoreApplication.translate("SYSMAN", u"\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.databasemodifyButton.setText(QCoreApplication.translate("SYSMAN", u"\u4fee\u6539\u6570\u636e\u5e93\u53c2\u6570", None))
    # retranslateUi

