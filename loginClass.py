from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from ui.login import Ui_Form
from ui.sign import Ui_sign

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



class SignWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sign()
        self.ui.setupUi(self)