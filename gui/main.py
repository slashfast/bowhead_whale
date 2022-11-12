from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QLabel, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from pathlib import Path
import os
import sys


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)
        self.setWindowIcon(QtGui.QIcon('res/icon.jpg'))

        self.current_file = QtGui.QPixmap('res/icon.jpg')
        pixmap = QtGui.QPixmap(self.current_file)
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1, 1)
        self.file_list = None
        self.file_counter = None

        self.directoryButton = self.findChild(QPushButton, "pushButton")
        self.nextButton2 = self.findChild(QPushButton, "pushButton_2")
        self.prevButton3 = self.findChild(QPushButton, "pushButton_3")

        self.directoryButton.clicked.connect(self.open_file)
        self.nextButton2.clicked.connect(self.next_image)
        self.prevButton3.clicked.connect(self.previous_image)

    def open_file(self):
        folder = QFileDialog.getExistingDirectory()
        self.file_list = [str(file) for file in [*Path(str(folder)).glob('**/*.jpg')]]
        self.image_counter = 0
        self.file_counter = self.file_list[self.image_counter]
        pixmap = QtGui.QPixmap(self.file_counter)
        self.label.setPixmap(pixmap)
        print(self.image_counter)
        print(self.file_list)

    def next_image(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter + 1)]
            print(Path(self.file_counter).name)
            self.image_counter += 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.label.setPixmap(pixmap)
            print()
        except:
            pass

    def previous_image(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter - 1)]
            print(Path(self.file_counter).name)
            self.image_counter -= 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.label.setPixmap(pixmap)
        except:
            pass


def main():
    window = UI()
    window.show()
    return window


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = main()
    app.exec_()
