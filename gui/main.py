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

        self.imagelabel = self.findChild(QLabel, "label")
        self.infolabel = self.findChild(QLabel, "label_2")
        self.filenamelabel = self.findChild(QLabel, "label_3")

        self.current_file = QtGui.QPixmap('res/icon.jpg')
        pixmap = QtGui.QPixmap(self.current_file)
        self.imagelabel.setPixmap(pixmap)
        self.imagelabel.setMinimumSize(1, 1)
        self.file_list = None
        self.file_counter = None

        self.directoryButton = self.findChild(QPushButton, "pushButton")
        self.nextButton2 = self.findChild(QPushButton, "pushButton_2")
        self.prevButton3 = self.findChild(QPushButton, "pushButton_3")
        self.Button4 = self.findChild(QPushButton, "pushButton_4")
        self.checkBox = self.findChild(QCheckBox, "checkBox")

        if self.file_list is None:
            self.nextButton2.setEnabled(False)
            self.prevButton3.setEnabled(False)
            self.Button4.setEnabled(False)
            self.filenamelabel.setEnabled(False)

        self.directoryButton.clicked.connect(self.OpenFile)
        self.nextButton2.clicked.connect(self.NextImage)
        self.prevButton3.clicked.connect(self.PreviosImage)

    def OpenFile(self):
        folder = QFileDialog.getExistingDirectory()
        self.file_list = [str(file) for file in [*Path(str(folder)).glob('**/*.jpg')]]
        self.image_counter = 0
        self.file_counter = self.file_list[self.image_counter]
        self.filenamelabel.setText(Path(self.file_counter).name)
        pixmap = QtGui.QPixmap(self.file_counter)
        self.imagelabel.setPixmap(pixmap)

        if self.checkBox.isChecked():
            self.infolabel.setText((Path(self.file_counter).name))
        else:
            self.infolabel.setText("")

        self.nextButton2.setEnabled(True)
        self.prevButton3.setEnabled(True)
        self.Button4.setEnabled(True)
        self.filenamelabel.setEnabled(True)

    def NextImage(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter + 1)]
            self.filenamelabel.setText(Path(self.file_counter).name)
            self.image_counter += 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.imagelabel.setPixmap(pixmap)

            if self.checkBox.isChecked():
                self.infolabel.setText((Path(self.file_counter).name))
            else:
                self.infolabel.setText("")
        except:
            pass

    def PreviosImage(self):
        try:
            self.file_counter = self.file_list[abs(self.image_counter - 1)]
            self.filenamelabel.setText(Path(self.file_counter).name)
            self.image_counter -= 1
            pixmap = QtGui.QPixmap(self.file_counter)
            self.imagelabel.setPixmap(pixmap)

            if self.checkBox.isChecked():
                self.infolabel.setText((Path(self.file_counter).name))
            else:
                self.infolabel.setText("")
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