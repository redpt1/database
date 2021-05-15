# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enodequery.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import base64
from one_png import img as one  # 引入img变量，赋别名为one
tmp = open('one.png', 'wb')  # 创建临时的文件
tmp.write(base64.b64decode(one))  ##把这个one图片解码出来，写入文件中去。
tmp.close()

class Ui_enode(object):
    def setupUi(self, enode):
        if not enode.objectName():
            enode.setObjectName(u"enode")
        enode.setWindowModality(Qt.NonModal)
        enode.setEnabled(True)
        enode.resize(780, 714)
        enode.setContextMenuPolicy(Qt.NoContextMenu)
        enode.setStyleSheet(u"*{\n"
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
        pix = pix.scaled(enode.width(), enode.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        enode.setPalette(palette)

        self.widget = QWidget(enode)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 780, 711))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background:#fff;")

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.enodeName = QLineEdit(self.widget)
        self.enodeName.setObjectName(u"enodeName")

        self.horizontalLayout_3.addWidget(self.enodeName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.enodeidList = QComboBox(self.widget)
        self.enodeidList.setObjectName(u"enodeidList")
        self.enodeidList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout_2.addWidget(self.enodeidList)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.enodenameList = QComboBox(self.widget)
        self.enodenameList.setObjectName(u"enodenameList")
        self.enodenameList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout.addWidget(self.enodenameList)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.queryButton = QPushButton(self.widget)
        self.queryButton.setObjectName(u"queryButton")
        self.queryButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.queryButton)

        self.queryButton_2 = QPushButton(self.widget)
        self.queryButton_2.setObjectName(u"queryButton_2")
        self.queryButton_2.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.queryButton_2)

        self.queryButton_3 = QPushButton(self.widget)
        self.queryButton_3.setObjectName(u"queryButton_3")
        self.queryButton_3.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.queryButton_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.retranslateUi(enode)

        QMetaObject.connectSlotsByName(enode)
    # setupUi

    def retranslateUi(self, enode):
        enode.setWindowTitle(QCoreApplication.translate("enode", u"基站信息", None))
        self.label.setText(QCoreApplication.translate("enode", u"\u57fa\u7ad9\u5168\u90e8\u5c0f\u533a\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("enode", u"\u57fa\u7ad9\u6807\u8bc6/\u540d\u79f0:", None))
        self.label_5.setText(QCoreApplication.translate("enode", u"\u57fa\u7ad9id\u5217\u8868\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("enode", u"\u57fa\u7ad9name\u5217\u8868\uff1a", None))
        self.queryButton.setText(QCoreApplication.translate("enode", u"\u67e5\u8be2", None))
        self.queryButton_2.setText(QCoreApplication.translate("enode", u"\u67e5\u8be2", None))
        self.queryButton_3.setText(QCoreApplication.translate("enode", u"\u67e5\u8be2", None))
    # retranslateUi

