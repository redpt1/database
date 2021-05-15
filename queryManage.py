from PySide2.QtWidgets import *

from ui.query import Ui_query
from secQuery import secQuery
from enoQuery import enoQuery


class queryManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_query()
        self.ui.setupUi(self)

        self.ui.sectorButton.clicked.connect(self.sectorQuery)
        self.ui.enodeButton.clicked.connect(self.enodeQuery)
    def sectorQuery(self):
        self.sector=secQuery()
        self.sector.show()

    def enodeQuery(self):
        self.enode = enoQuery()
        self.enode.show()