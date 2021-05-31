from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

from network import Ui_web


class webui(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_web()
        self.ui.setupUi(self)
        self.put()

    def put(self):
        self.ui.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load("network.png")
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(1000, 770))    #自己设定尺寸
        self.ui.graphicsView.scene_img.addItem(self.imgShowItem)
        self.ui.graphicsView.setScene(self.ui.graphicsView.scene_img)
        #self.ui.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow))) # 图像自适应大小