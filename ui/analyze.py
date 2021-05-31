# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyze.ui'
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

class Ui_analyze(object):
    def setupUi(self, analyze):
        if not analyze.objectName():
            analyze.setObjectName(u"analyze")
        analyze.resize(490, 554)
        self.verticalLayout_2 = QVBoxLayout(analyze)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(analyze)
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
        self.layoutWidget.setGeometry(QRect(60, 90, 339, 371))
        self.layoutWidget.setStyleSheet(u"background:transparent;\n")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.c2lButton = QPushButton(self.layoutWidget)
        self.c2lButton.setObjectName(u"c2lButton")
        self.c2lButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.c2lButton)

        self.sectorButton = QPushButton(self.layoutWidget)
        self.sectorButton.setObjectName(u"sectorButton")
        self.sectorButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")
        palette = QPalette()
        pix = QPixmap("one.png")
        pix = pix.scaled(analyze.width(), analyze.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        analyze.setPalette(palette)
        self.verticalLayout.addWidget(self.sectorButton)

        self.netButton = QPushButton(self.layoutWidget)
        self.netButton.setObjectName(u"netButton")
        self.netButton.setStyleSheet(u"border:2px groove gray;\n"
"padding:2px 4px;\n"
"color:#fff;\n"
"border-radius:5px;\n"
"background:#03a9f4;\n"
"font-size:25px;")

        self.verticalLayout.addWidget(self.netButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(analyze)

        QMetaObject.connectSlotsByName(analyze)
    # setupUi

    def retranslateUi(self, analyze):
        analyze.setWindowTitle(QCoreApplication.translate("analyze", u"分析", None))
        self.label.setText(QCoreApplication.translate("analyze", u"\u5206\u6790\u529f\u80fd\u754c\u9762", None))
        self.c2lButton.setText(QCoreApplication.translate("analyze", u"\u4e3b\u90bb\u5c0f\u533aC2I\u5e72\u6270\u5206\u6790", None))
        self.sectorButton.setText(QCoreApplication.translate("analyze", u"\u91cd\u53e0\u8986\u76d6\u5e72\u6270\u5c0f\u533a\u5206\u6790", None))
        self.netButton.setText(QCoreApplication.translate("analyze", u"\u7f51\u7edc\u5e72\u6270\u7ed3\u6784\u5206\u6790", None))
    # retranslateUi

