# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'query.ui'
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

class Ui_query(object):
    def setupUi(self, query):
        if not query.objectName():
            query.setObjectName(u"query")
        query.resize(490, 554)
        self.verticalLayout_2 = QVBoxLayout(query)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(query)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"padding:2px 4px;\n"
"border:2px;")
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(query.width(), query.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        query.setPalette(palette)
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
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 90, 254, 371))
        self.layoutWidget.setStyleSheet(u"background:transparent;\n")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sectorButton = QPushButton(self.layoutWidget)
        self.sectorButton.setObjectName(u"sectorButton")
        self.sectorButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.sectorButton)

        self.enodeButton = QPushButton(self.layoutWidget)
        self.enodeButton.setObjectName(u"enodeButton")
        self.enodeButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.enodeButton)

        self.kpiButton = QPushButton(self.layoutWidget)
        self.kpiButton.setObjectName(u"kpiButton")
        self.kpiButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.kpiButton)

        self.prbButton = QPushButton(self.layoutWidget)
        self.prbButton.setObjectName(u"prbButton")
        self.prbButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.prbButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(query)

        QMetaObject.connectSlotsByName(query)
    # setupUi

    def retranslateUi(self, query):
        query.setWindowTitle(QCoreApplication.translate("query", u"查询", None))
        self.label.setText(QCoreApplication.translate("query", u"\u67e5\u8be2\u529f\u80fd\u754c\u9762", None))
        self.sectorButton.setText(QCoreApplication.translate("query", u"\u5c0f\u533a\u914d\u7f6e\u4fe1\u606f\u67e5\u8be2", None))
        self.enodeButton.setText(QCoreApplication.translate("query", u"\u57fa\u7ad9eNodeB\u4fe1\u606f\u67e5\u8be2", None))
        self.kpiButton.setText(QCoreApplication.translate("query", u"\u5c0f\u533aKPI\u6307\u6807\u4fe1\u606f\u67e5\u8be2", None))
        self.prbButton.setText(QCoreApplication.translate("query", u"PRB\u4fe1\u606f\u7edf\u8ba1\u4e0e\u67e5\u8be2", None))
    # retranslateUi

