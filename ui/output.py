# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_output(object):
    def setupUi(self, output):
        if not output.objectName():
            output.setObjectName(u"output")
        output.resize(850, 650)
        self.outButton = QPushButton(output)
        self.outButton.setObjectName(u"outButton")
        self.outButton.setGeometry(QRect(751, 600, 93, 28))
        self.chart = QWidget(output)
        self.chart.setObjectName(u"chart")
        self.chart.setGeometry(QRect(60, 20, 400, 300))
        self.chart.setMinimumSize(QSize(400, 300))

        self.retranslateUi(output)

        QMetaObject.connectSlotsByName(output)
    # setupUi

    def retranslateUi(self, output):
        output.setWindowTitle(QCoreApplication.translate("output", u"output", None))
        self.outButton.setText(QCoreApplication.translate("output", u"\u5bfc\u51fa", None))
    # retranslateUi

