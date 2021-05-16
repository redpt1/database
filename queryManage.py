from PySide2.QtWidgets import *

from ui.query import Ui_query
from secQuery import secQuery
from enoQuery import enoQuery
from kpiQuery import kpiQuery

class queryManage(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_query()
        self.ui.setupUi(self)

        self.ui.sectorButton.clicked.connect(self.sectorQuery)
        self.ui.enodeButton.clicked.connect(self.enodeQuery)
        self.ui.kpiButton.clicked.connect(self.kpQuery)


    def sectorQuery(self):
        self.sector=secQuery()
        self.sector.show()

    def enodeQuery(self):
        self.enode = enoQuery()
        self.enode.show()

    def kpQuery(self):
        self.kpi = kpiQuery()
        self.kpi.show()