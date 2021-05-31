# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'network.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_web(object):
    def setupUi(self, web):
        if not web.objectName():
            web.setObjectName(u"web")
        web.resize(1017, 784)
        self.graphicsView = QGraphicsView(web)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 1011, 781))

        self.retranslateUi(web)

        QMetaObject.connectSlotsByName(web)
    # setupUi

    def retranslateUi(self, web):
        web.setWindowTitle(QCoreApplication.translate("web", u"web", None))
    # retranslateUi

