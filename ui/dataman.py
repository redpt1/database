# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataman.ui'
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


class Ui_dataMan(object):
    def setupUi(self, dataMan):
        if not dataMan.objectName():
            dataMan.setObjectName(u"dataMan")
        dataMan.setWindowModality(Qt.NonModal)
        dataMan.setEnabled(True)
        dataMan.resize(808, 717)
        dataMan.setContextMenuPolicy(Qt.NoContextMenu)
        dataMan.setStyleSheet(u"*{\n"
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
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(dataMan.width(), dataMan.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        dataMan.setPalette(palette)
        self.label_3 = QLabel(dataMan)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 60, 191, 91))
        self.widget = QWidget(dataMan)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 170, 711, 481))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dataIn = QComboBox(self.widget)
        self.dataIn.addItem("")
        self.dataIn.addItem("")
        self.dataIn.addItem("")
        self.dataIn.addItem("")
        self.dataIn.setObjectName(u"dataIn")
        self.dataIn.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:0xfff;\n")

        self.horizontalLayout.addWidget(self.dataIn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.dataOut = QComboBox(self.widget)
        self.dataOut.setObjectName(u"dataOut")
        self.dataOut.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:0xfff;\n")

        self.horizontalLayout_2.addWidget(self.dataOut)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.infileaddr = QLineEdit(self.widget)
        self.infileaddr.setObjectName(u"infileaddr")

        self.horizontalLayout_3.addWidget(self.infileaddr)

        self.infileButton = QToolButton(self.widget)
        self.infileButton.setObjectName(u"infileButton")

        self.horizontalLayout_3.addWidget(self.infileButton)

        self.inButton = QPushButton(self.widget)
        self.inButton.setObjectName(u"inButton")
        self.inButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.horizontalLayout_3.addWidget(self.inButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.outfileaddr = QLineEdit(self.widget)
        self.outfileaddr.setObjectName(u"outfileaddr")

        self.horizontalLayout_4.addWidget(self.outfileaddr)

        self.outfileButton = QToolButton(self.widget)
        self.outfileButton.setObjectName(u"outfileButton")

        self.horizontalLayout_4.addWidget(self.outfileButton)

        self.outButton = QPushButton(self.widget)
        self.outButton.setObjectName(u"outButton")
        self.outButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.horizontalLayout_4.addWidget(self.outButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(dataMan)

        QMetaObject.connectSlotsByName(dataMan)
    # setupUi

    def retranslateUi(self, dataMan):
        dataMan.setWindowTitle(QCoreApplication.translate("dataMan", u"\u767b\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("dataMan", u"\u6570\u636e\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate("dataMan", u"\u6570\u636e\u5bfc\u5165", None))
        self.dataIn.setItemText(0, QCoreApplication.translate("dataMan", u"\u7f51\u7edc\u914d\u7f6e\u5bfc\u5165", None))
        self.dataIn.setItemText(1, QCoreApplication.translate("dataMan", u"KPI\u6307\u6807\u4fe1\u606f\u5bfc\u5165", None))
        self.dataIn.setItemText(2, QCoreApplication.translate("dataMan", u"PRB\u5e72\u6270\u4fe1\u606f\u5bfc\u5165", None))
        self.dataIn.setItemText(3, QCoreApplication.translate("dataMan", u"MRO\u6570\u636e\u5bfc\u5165", None))

        self.label_2.setText(QCoreApplication.translate("dataMan", u"\u6570\u636e\u5bfc\u51fa", None))
        self.label_4.setText(QCoreApplication.translate("dataMan", u"\u5bfc\u5165\u5730\u5740", None))
        self.infileButton.setText(QCoreApplication.translate("dataMan", u"...", None))
        self.inButton.setText(QCoreApplication.translate("dataMan", u"\u5bfc\u5165", None))
        self.label_5.setText(QCoreApplication.translate("dataMan", u"\u5bfc\u51fa\u5730\u5740", None))
        self.outfileButton.setText(QCoreApplication.translate("dataMan", u"...", None))
        self.outButton.setText(QCoreApplication.translate("dataMan", u"\u5bfc\u51fa", None))
    # retranslateUi

