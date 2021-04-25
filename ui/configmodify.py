# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configmodify.ui'
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


class Ui_MODIFY(object):
    def setupUi(self, MODIFY):
        MODIFY.setObjectName("MODIFY")
        MODIFY.resize(607, 600)
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(MODIFY.width(), MODIFY.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        MODIFY.setPalette(palette)
        MODIFY.setStyleSheet(u"font-size:24px;\n"
"font-family:sans-serif;")
        self.verticalLayout_2 = QVBoxLayout(MODIFY)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.frame = QFrame(MODIFY)
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
        self.label.setGeometry(QRect(180, 20, 231, 61))
        font = QFont()
        font.setFamily(u"sans-serif")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#fff;\n"
"background:transparent;\n"
"font-size:30px;")
        self.databaseconfigButton = QPushButton(self.frame)
        self.databaseconfigButton.setObjectName(u"databaseconfigButton")
        self.databaseconfigButton.setEnabled(True)
        self.databaseconfigButton.setGeometry(QRect(390, 480, 171, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.databaseconfigButton.sizePolicy().hasHeightForWidth())
        self.databaseconfigButton.setSizePolicy(sizePolicy1)
        self.databaseconfigButton.setFont(font)
        self.databaseconfigButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"background:#03a9f4")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 140, 471, 221))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background : transparent;\n"
"color:white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"background:white")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background:transparent;\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background:white")
        self.lineEdit_2.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(MODIFY)

        QMetaObject.connectSlotsByName(MODIFY)
    # setupUi

    def retranslateUi(self, MODIFY):
        MODIFY.setWindowTitle(QCoreApplication.translate("MODIFY", u"配置", None))
        self.label.setText(QCoreApplication.translate("MODIFY", u"\u4fee\u6539\u6570\u636e\u5e93\u53c2\u6570", None))
        self.databaseconfigButton.setText(QCoreApplication.translate("MODIFY", u"\u63d0\u4ea4", None))
        self.label_2.setText(QCoreApplication.translate("MODIFY", u"\u6570\u636e\u5e93\u8fde\u63a5\u65f6\u957f", None))
        self.label_4.setText(QCoreApplication.translate("MODIFY", u"\u6570\u636e\u5e93\u7f13\u51b2\u533a\u5927\u5c0f", None))
    # retranslateUi

