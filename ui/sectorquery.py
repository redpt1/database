# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sectorquery.ui'
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

class Ui_sector(object):
    def setupUi(self, sector):
        if not sector.objectName():
            sector.setObjectName(u"sector")
        sector.setWindowModality(Qt.NonModal)
        sector.setEnabled(True)
        sector.resize(827, 714)
        sector.setContextMenuPolicy(Qt.NoContextMenu)
        sector.setStyleSheet(u"*{\n"
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
        pix = pix.scaled(sector.width(), sector.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        sector.setPalette(palette)
        

        self.layoutWidget = QWidget(sector)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 421, 701))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.listView = QListView(self.layoutWidget)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"background:#fff")
        self.verticalLayout_5.addWidget(self.listView)

        self.layoutWidget1 = QWidget(sector)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(438, 81, 381, 261))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sectorName = QLineEdit(self.layoutWidget1)
        self.sectorName.setObjectName(u"sectorName")

        self.horizontalLayout_3.addWidget(self.sectorName)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.sectorList = QComboBox(self.layoutWidget1)
        self.sectorList.setObjectName(u"sectorList")
        self.sectorList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.horizontalLayout.addWidget(self.sectorList)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.queryButton = QPushButton(sector)
        self.queryButton.setObjectName(u"queryButton")
        self.queryButton.setGeometry(QRect(500, 420, 258, 28))
        self.queryButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.retranslateUi(sector)

        QMetaObject.connectSlotsByName(sector)
    # setupUi

    def retranslateUi(self, sector):
        sector.setWindowTitle(QCoreApplication.translate("sector", u"小区信息", None))
        self.label.setText(QCoreApplication.translate("sector", u"\u5c0f\u533a\u8be6\u7ec6\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("sector", u"\u5c0f\u533a\u540d\u79f0/ID\uff1a  ", None))
        self.label_3.setText(QCoreApplication.translate("sector", u"\u5c0f\u533a\u5217\u8868\uff1a", None))
        self.queryButton.setText(QCoreApplication.translate("sector", u"\u67e5\u8be2", None))
    # retranslateUi

