from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QLabel, QMessageBox, QCheckBox
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
        self.label1 = self.findChild(QLabel, "label")
        self.label2 = self.findChild(QLabel, "label_2")

        self.current_file = QtGui.QPixmap('res/icon.jpg')
        pixmap = QtGui.QPixmap(self.current_file)
        self.label1.setPixmap(pixmap)
        self.label1.setMinimumSize(1, 1)
        self.file_list = None
        self.file_counter = None

        self.directoryButton = self.findChild(QPushButton, "pushButton")
        self.nextButton2 = self.findChild(QPushButton, "pushButton_2")
        self.prevButton3 = self.findChild(QPushButton, "pushButton_3")
        self.Button4 = self.findChild(QPushButton, "pushButton_4")
        self.checkBox = self.findChild(QCheckBox, "checkBox")

        if self.file_list is None:
            self.nextButton2.setVisible(False)
            self.prevButton3.setVisible(False)
            self.Button4.setVisible(False)
            self.checkBox.setVisible(False)

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
        self.label1.setPixmap(pixmap)
        self.nextButton2.setVisible(True)
        self.prevButton3.setVisible(True)
        self.Button4.setVisible(True)
        self.checkBox.setVisible(True)

    def ChekedBox(self, checked):
        if checked:
            print()




    def NextImage(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter + 1)]
            self.image_counter += 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.label1.setPixmap(pixmap)
        except :
            pass

    def PreviosImage(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter - 1)]
            self.image_counter -= 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.label1.setPixmap(pixmap)
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