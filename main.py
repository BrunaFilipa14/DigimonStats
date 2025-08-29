#PyQt5 GUI

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QRadioButton, QButtonGroup)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digimon")
        # setGeometry(x, y, width, height)
        self.setGeometry(700, 120, 600, 800)
        self.setWindowIcon(QIcon("digimon.jpg"))

        #radio buttons
        self.button_level = QRadioButton("Levels", self)
        self.button_attribute = QRadioButton("Attributes", self)
        self.button_type = QRadioButton("Types", self)
        self.button_fields = QRadioButton("Fields", self)
        self.button_all_stats = QRadioButton("Show All", self)



        self.initUI()


    def initUI(self):
        #to be able to use the layout managers
        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)

        # title
        label = QLabel("This is a Digimon Selecter", self)

        # image
        label_picture = QLabel(self)

        label.setFont(QFont("Arial", 20))
        label.setGeometry(90, 10, 450, 50)
        label.setStyleSheet("color: hsl(20, 98%, 48%);"
                                 "font-weight: bold;")
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        label_picture.setGeometry(0, 0, 300, 200)

        pixmap = QPixmap("digimon.jpg")
        label_picture.setPixmap(pixmap)
        label_picture.setScaledContents(True)
        label_picture.setGeometry((self.width() - label_picture.width()) // 2, 70, label_picture.width(),
                                       label_picture.height())
        #label_picture.setAlignment(Qt.AlignCenter)

        #grid = QGridLayout()
        #grid.addWidget(label, 0, 1)
        #grid.addWidget(label_picture, 1, 1)
        #central_widget.setLayout(grid)

        #radio buttons
        self.button_level.setGeometry(label_picture.x(), label_picture.y(), )
        self.button_attribute = QRadioButton("Attributes", self)
        self.button_type = QRadioButton("Types", self)
        self.button_fields = QRadioButton("Fields", self)
        self.button_all_stats = QRadioButton("Show All", self)



def main():
    #sys.argv so that the command line can be used, otherwise just pass []
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()