# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kpiquery.ui'
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

class Ui_kpi(object):
    def setupUi(self, kpi):
        if not kpi.objectName():
            kpi.setObjectName(u"kpi")
        kpi.setWindowModality(Qt.NonModal)
        kpi.setEnabled(True)
        kpi.resize(1024, 762)
        kpi.setContextMenuPolicy(Qt.NoContextMenu)
        kpi.setStyleSheet(u"*{\n"
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
        pix = pix.scaled(kpi.width(), kpi.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        kpi.setPalette(palette)
        self.widget = QWidget(kpi)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1021, 761))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.sectorName = QLineEdit(self.widget)
        self.sectorName.setObjectName(u"sectorName")

        self.horizontalLayout.addWidget(self.sectorName)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.sectornameList = QComboBox(self.widget)
        self.sectornameList.setObjectName(u"sectornameList")
        self.sectornameList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout_2.addWidget(self.sectornameList)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.dateEditS = QDateEdit(self.widget)
        self.dateEditS.setObjectName(u"dateEditS")

        self.horizontalLayout_3.addWidget(self.dateEditS)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.dateEditF = QDateEdit(self.widget)
        self.dateEditF.setObjectName(u"dateEditF")

        self.horizontalLayout_3.addWidget(self.dateEditF)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.queryButton = QPushButton(self.widget)
        self.queryButton.setObjectName(u"queryButton")
        self.queryButton.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_3.addWidget(self.queryButton)

        self.queryButton_2 = QPushButton(self.widget)
        self.queryButton_2.setObjectName(u"queryButton_2")
        self.queryButton_2.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_3.addWidget(self.queryButton_2)

        self.queryButton_4 = QPushButton(self.widget)
        self.queryButton_4.setObjectName(u"queryButton_4")
        self.queryButton_4.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"")

        self.verticalLayout_3.addWidget(self.queryButton_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.attrList = QComboBox(self.widget)
        self.attrList.setObjectName(u"attrList")
        self.attrList.setStyleSheet(u"border-radius:5px;\n"
"border:2px groove gray;\n"
"background:#fff")

        self.horizontalLayout_5.addWidget(self.attrList)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background:#fff\n"
"")

        self.verticalLayout_4.addWidget(self.graphicsView)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background:#fff;")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.retranslateUi(kpi)

        QMetaObject.connectSlotsByName(kpi)
    # setupUi

    def retranslateUi(self, kpi):
        kpi.setWindowTitle(QCoreApplication.translate("kpi", u"\u767b\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("kpi", u"\u5c0f\u533a\u540d\u79f0:", None))
        self.label_3.setText(QCoreApplication.translate("kpi", u"\u5c0f\u533a\u5217\u8868\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2\u533a\u95f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("kpi", u"-", None))
        self.queryButton.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2", None))
        self.queryButton_2.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2", None))
        self.queryButton_4.setText(QCoreApplication.translate("kpi", u"\u67e5\u8be2", None))
        self.label_8.setText(QCoreApplication.translate("kpi", u"\u5c5e\u6027\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("kpi", u"\u5c5e\u6027\u56fe\u793a\uff1a", None))
        self.label.setText(QCoreApplication.translate("kpi", u"\u5c0f\u533a\u5c5e\u6027\u5217\u8868", None))
    # retranslateUi

