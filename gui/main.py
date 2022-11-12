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
        self.file_list = [str(path) for path in [*Path(str(folder)).glob('*.jpg')]]
        self.image_counter = 0
        self.file_counter = self.file_list[self.image_counter]
        pixmap = QtGui.QPixmap(self.file_counter)
        self.label.setPixmap(pixmap)


    def NextImage(self):
        try:
            self.image_counter += 1
            self.file_counter = self.file_list[self.image_counter]
            pixmap = QtGui.QPixmap(self.file_counter)
            self.label.setPixmap(pixmap)
        except :
            print(f' ')

    def PreviosImage(self):
        print(self.file_counter)


def main():
    window = UI()
    window.show()
    return window

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = main()
    app.exec_()