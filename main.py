#PyQt5 GUI

import sys
from unittest import case

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QRadioButton, QLineEdit, QPushButton, QStatusBar)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import api
from api import get_digimon_info


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digimon")
        # setGeometry(x, y, width, height)
        self.setGeometry(700, 120, 600, 800)
        self.setWindowIcon(QIcon("digimon.jpg"))

        # input box
        self.line_edit = QLineEdit(self)
        #submit button
        self.submit_button = QPushButton("Submit", self)

        #radio buttons
        self.button_level = QRadioButton("Levels", self)
        self.button_attribute = QRadioButton("Attributes", self)
        self.button_type = QRadioButton("Types", self)
        self.button_fields = QRadioButton("Fields", self)
        self.button_all_stats = QRadioButton("Show All", self)

        #label with stats
        self.stats_label = QLabel(self)
        #warning
        self.warning_label = QLabel(self)


        self.initUI()


    def initUI(self):
        # title
        label = QLabel("This is a Digimon Selecter", self)

        label.setFont(QFont("Arial", 20))
        label.setGeometry(90, 10, 450, 50)
        label.setStyleSheet("color: hsl(20, 98%, 48%);"
                                 "font-weight: bold;")
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # image
        label_picture = QLabel(self)
        label_picture.setGeometry(0, 0, 300, 200)

        pixmap = QPixmap("digimon.jpg")
        label_picture.setPixmap(pixmap)

        label_picture.setScaledContents(True)
        label_picture.setGeometry((self.width() - label_picture.width()) // 2, 70, label_picture.width(),
                                       label_picture.height())
        #label_picture.setAlignment(Qt.AlignCenter)


        # input box
        self.line_edit.setGeometry(label_picture.x(), label_picture.y() + 250, 200, 50)
        self.line_edit.setStyleSheet("font-size: 20px;")
        self.line_edit.setPlaceholderText("Enter the Digimon")
        # submit button
        self.submit_button.setGeometry(self.line_edit.x() + 200, label_picture.y() + 250, 100, 50)
        self.submit_button.setStyleSheet("font-size: 20px;")

        self.submit_button.clicked.connect(self.submit)


        #stats label
        self.stats_label.setGeometry(50, self.button_fields.y() + 550, 400, 200)
        #warning label
        self.warning_label.setGeometry(label_picture.x(), self.line_edit.y() - 50, 350, 50)
        self.warning_label.setStyleSheet("font-size: 20px; color: red;")

        #radio buttons
        self.button_level.setGeometry(label_picture.x(), label_picture.y() + 300, 100, 50)
        self.button_attribute.setGeometry(self.button_level.x() + 100, self.button_level.y(), 100, 50)
        self.button_type.setGeometry(self.button_attribute.x() + 100, self.button_attribute.y(), 100, 50)

        self.button_fields.setGeometry(self.button_level.x(), self.button_type.y() + 50, 100, 50)
        self.button_all_stats.setGeometry(self.button_attribute.x(), self.button_fields.y(), 100, 50)

        # self.button_level.setGeometry(label_picture.x(), label_picture.y() + 300, 200, 50)
        # self.button_attribute.setGeometry(label_picture.x(), self.button_level.y(), 200, 50)
        # self.button_type.setGeometry(label_picture.x(), self.button_attribute.y(), 200, 50)
        # self.button_fields.setGeometry(label_picture.x(), self.button_type.y() + 50, 200, 50)
        # self.button_all_stats.setGeometry(label_picture.x(), self.button_fields.y(), 200, 50)


        # to be able to use the layout managers
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        #
        # v_box = QVBoxLayout()
        #
        # title = QGridLayout()
        # title.addWidget(label, 0, 1)
        # title.addWidget(label_picture, 1, 1)
        #
        # labels = QHBoxLayout()
        # labels.addWidget(self.line_edit)
        # labels.addWidget(self.submit_button)
        #
        # radio_buttons = QGridLayout()
        # radio_buttons.addWidget(self.button_level, 0, 0)
        # radio_buttons.addWidget(self.button_attribute, 0, 1)
        # radio_buttons.addWidget(self.button_type, 0, 2)
        # radio_buttons.addWidget(self.button_fields, 1, 0)
        # radio_buttons.addWidget(self.button_all_stats, 1, 2)
        #
        # v_box.addLayout(title)
        # v_box.addLayout(labels)
        # v_box.addLayout(radio_buttons)
        # central_widget.setLayout(v_box)

        #so that there is always data showing
        self.button_all_stats.setChecked(True)

        self.button_level.toggled.connect(self.radio_button_changed)
        self.button_attribute.toggled.connect(self.radio_button_changed)
        self.button_type.toggled.connect(self.radio_button_changed)
        self.button_fields.toggled.connect(self.radio_button_changed)
        self.button_all_stats.toggled.connect(self.radio_button_changed)

    def submit(self):
        self.stats_label.setText("")
        digimon = self.line_edit.text()
        if self.button_level.isChecked():
            self.get_digimon(digimon, self.button_level)
        elif self.button_attribute.isChecked():
            self.get_digimon(digimon, self.button_attribute)
        elif self.button_type.isChecked():
            self.get_digimon(digimon, self.button_type)
        elif self.button_fields.isChecked():
            self.get_digimon(digimon, self.button_fields)
        elif self.button_all_stats.isChecked():
            self.get_digimon(digimon, self.button_all_stats)
        else:
            self.warning_label.setText("Please select an option!")


    def radio_button_changed(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            digimon = self.line_edit.text()
            if digimon != "":
                self.stats_label.setText("")
                self.get_digimon(digimon, radio_button)

    def get_digimon(self, digimon, radio_button):
        self.warning_label.setText("")

        if digimon:
            digimon_info = get_digimon_info(digimon)
            if digimon_info:
                match radio_button:
                    case self.button_level:
                        text = "Levels:\n"
                        for level in digimon_info["levels"]:
                            text += level["level"] + "\n"
                        self.stats_label.setStyleSheet("color:blue; font-size: 20px;")
                        self.stats_label.setText(text)
                    case self.button_attribute:
                        text = "Attributes:\n"
                        for attribute in digimon_info["attributes"]:
                            text += attribute["attribute"] + "\n"
                        self.stats_label.setStyleSheet("color:red; font-size: 20px;")
                        self.stats_label.setText(text)
                    case self.button_type:
                        text = "Types:\n"
                        for type in digimon_info["types"]:
                            text += type["type"] + "\n"
                        self.stats_label.setStyleSheet("color:green; font-size: 20px;")
                        self.stats_label.setText(text)
                    case self.button_fields:
                        text = "Fields:\n"
                        for field in digimon_info["fields"]:
                            text += field["field"] + "\n"
                        self.stats_label.setStyleSheet("color:orange; font-size: 20px;")
                        self.stats_label.setText(text)
                    case self.button_all_stats:
                        text = "Levels:\n"
                        for level in digimon_info["levels"]:
                            text += level["level"] + " | "
                        text += "\nAttributes:\n"
                        for attribute in digimon_info["attributes"]:
                            text += attribute["attribute"] + " | "
                        text += "\nTypes:\n"
                        for type in digimon_info["types"]:
                            text += type["type"] + " | "
                        text += "\nFields:\n"
                        for field in digimon_info["fields"]:
                            text += field["field"] + " | "
                        self.stats_label.setStyleSheet("color:black; font-size: 20px;")
                        self.stats_label.setText(text)
                    case _:
                        pass
            else:
                self.warning_label.setText("Please write a valid digimon!")
        else:
            self.warning_label.setText("Please write the name of a digimon!")


def main():
    #sys.argv so that the command line can be used, otherwise just pass []
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()