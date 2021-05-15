from PySide2.QtWidgets import *



from ui.sectorquery import Ui_sector


class secQuery(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_sector()
        self.ui.setupUi(self)
