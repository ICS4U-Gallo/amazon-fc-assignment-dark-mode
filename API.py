"""
Order of operations

1. Get order request from api
-- When receiving an order request I need to know,
    - Name
    - Address (Distance)
    - Product they ordered
2. Take item off shelf
3. Transfer item to packaging with all details
"""
import sys
import pickle
from temporary_database_reset import Item
from itertools import product
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#API

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.layoutUI()

    def layoutUI(self):
        self.setStyleSheet("background-color: brown;")

        self.principalLayout = QHBoxLayout(self)

        self.rightFrame = QFrame(self)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.rightFrame)
        self.gridLayout = QGridLayout()

        categories = QComboBox(self.rightFrame)
        categories.addItem("clothing")
        categories.addItem("electronics")
        categories.addItem("automotive")
        categories.addItem("home_kitchen")
        categories.addItem("sports")
        categories.addItem("tools")
        categories.addItem("toys_games")
        categories.activated[str].connect(self.changing_selection)
        self.gridLayout.addWidget(categories, 0, 0)

        self.verticalLayout.addLayout(self.gridLayout)
        self.principalLayout.addWidget(self.rightFrame)

        self.verticalLayoutR = QVBoxLayout()
        self.verticalLayoutR.setSpacing(0)
        self.exitFrame = QFrame(self)
        self.exitFrame.setStyleSheet("background-color: red;")
        self.exitFrame.setFrameShape(QFrame.StyledPanel)
        self.exitFrame.setFrameShadow(QFrame.Raised)
        self.exitverticalLayout = QVBoxLayout(self.exitFrame)
        self.exitBtn = QPushButton("Exit", self.exitFrame)
        self.exit_time()
        self.exitverticalLayout.addWidget(self.exitBtn)
        self.verticalLayoutR.addWidget(self.exitFrame)

        self.numpadFrame = QFrame(self)
        self.numpadFrame.setStyleSheet("background-color: black;")
        self.numpadFrame.setFrameShape(QFrame.StyledPanel)
        self.numpadFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.numpadFrame)
        spacerItem = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QVBoxLayout()
        spacerItem1 = QSpacerItem(20, 57, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)

        x = (0, 1, 2)

        self.coords = list(product(x, x))

        

        
        
        

        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.verticalLayoutR.addWidget(self.numpadFrame)

        self.adminFrame = QFrame(self)
        self.adminFrame.setStyleSheet("background-color: blue;")
        self.adminFrame.setFrameShape(QFrame.StyledPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.adminFrame)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.adminBtn = QPushButton("Send Order", self.adminFrame)
        self.horizontalLayout.addWidget(self.adminBtn)
        self.verticalLayoutR.addWidget(self.adminFrame)
        self.principalLayout.addLayout(self.verticalLayoutR)

    def changing_selection(self, select):
        with open("database_storage.pickle", "rb") as f:
            database = pickle.load(f)
        for data in database[select]:
            for i in self.coords:
                x, y = i
                fillerword = data.name
                print(data.name)
                button = QPushButton(self.numpadFrame)
                button.setFixedSize(60, 60)
                button.setText(fillerword)
                button.setStyleSheet("background-color: white;")
                self.gridLayout.addWidget(button, x, y)


    def exit_time(self):
        self.exitBtn.clicked.connect(QApplication.instance().quit)





#Taking items
"""
shelf.remove(item)
database.remove(item)
"""

#Transfer to packaging
def movetopackage():
    pass

#The Main Running thing so i don't have to deal with things
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())