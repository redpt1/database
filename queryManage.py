from PySide2.QtWidgets import *

from ui.query import Ui_query
from secQuery import secQuery

class queryManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_query()
        self.ui.setupUi(self)

        self.ui.sectorButton.clicked.connect(self.sectorQuery)

    def sectorQuery(self):
        self.sector=secQuery()
        self.sector.show()