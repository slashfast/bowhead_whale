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

        self.directoryButton.clicked.connect(self.OpenFile)
        self.nextButton2.clicked.connect(self.NextImage)
        self.prevButton3.clicked.connect(self.PreviosImage)

    def OpenFile(self):
        options = QFileDialog.Options()
        folder = QFileDialog.getExistingDirectory(self)
        print(str(folder))
        self.file_list = [str(path) for path in [*Path(str(folder)).glob('*')]]
        # self.file_list = [*Path(str(folder)).glob('*')]
        print(self.file_list)
        # self.file_counter = 0
        # self.current_file = self.file_list[self.file_counter]
        # pixmap = QtGui.QPixmap(self.current_file)
        # pixmap = pixmap.scaled(self.width(), self.height())
        # self.label.setPixmap(pixmap)


    def NextImage(self):
        if self.file_counter is not None:
            self.file_counter += 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)

    def PreviosImage(self):
        if self.file_counter is not None:
            self.file_counter -= 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)


def main():
    window = UI()
    window.show()
    return window

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = main()
    app.exec_()