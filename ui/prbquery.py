# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prbquery.ui'
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

class Ui_prb(object):
    def setupUi(self, prb):
        if not prb.objectName():
            prb.setObjectName(u"kpi")
        prb.setWindowModality(Qt.NonModal)
        prb.setEnabled(True)
        prb.resize(708, 257)
        prb.setContextMenuPolicy(Qt.NoContextMenu)
        prb.setStyleSheet(u"*{\n"
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
        pix = pix.scaled(prb.width(), prb.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        prb.setPalette(palette)
        self.newButton = QPushButton(prb)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setGeometry(QRect(520, 160, 121, 81))
        self.newButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")
        self.widget = QWidget(prb)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 2, 638, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.webList = QComboBox(self.widget)
        self.webList.setObjectName(u"webList")
        self.webList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout_4.addWidget(self.webList)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.webName = QLineEdit(self.widget)
        self.webName.setObjectName(u"webName")

        self.horizontalLayout.addWidget(self.webName)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.dateTimeEdits = QDateTimeEdit(self.widget)
        self.dateTimeEdits.setObjectName(u"dateTimeEdits")
        self.dateTimeEdits.setDate(QDate(2020, 7, 17))

        self.horizontalLayout_2.addWidget(self.dateTimeEdits)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.dateTimeEditf = QDateTimeEdit(self.widget)
        self.dateTimeEditf.setObjectName(u"dateTimeEditf")
        self.dateTimeEditf.setDate(QDate(2020, 7, 19))

        self.horizontalLayout_2.addWidget(self.dateTimeEditf)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.attrList = QComboBox(self.widget)
        self.attrList.setObjectName(u"attrList")
        self.attrList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout_3.addWidget(self.attrList)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.widget1 = QWidget(prb)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(650, 0, 51, 81))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.queryButton1 = QPushButton(self.widget1)
        self.queryButton1.setObjectName(u"queryButton1")
        self.queryButton1.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.queryButton1)

        self.queryButton2 = QPushButton(self.widget1)
        self.queryButton2.setObjectName(u"queryButton2")
        self.queryButton2.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_2.addWidget(self.queryButton2)

        self.widget2 = QWidget(prb)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(30, 180, 451, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")



        self.retranslateUi(prb)

        QMetaObject.connectSlotsByName(prb)
    # setupUi

    def retranslateUi(self, kpi):
        kpi.setWindowTitle(QCoreApplication.translate("kpi", u"prb信息", None))
        self.newButton.setText(QCoreApplication.translate("kpi", u"\u751f\u6210\u65b0\u8868", None))
        self.label_3.setText(QCoreApplication.translate("kpi", u"\u7f51\u5143\u5217\u8868\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("kpi", u"\u7f51\u5143\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2\u533a\u95f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("kpi", u"-", None))
        self.label_8.setText(QCoreApplication.translate("kpi", u"\u5c5e\u6027\uff1a", None))
        self.queryButton1.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2", None))
        self.queryButton2.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2", None))
    # retranslateUi

