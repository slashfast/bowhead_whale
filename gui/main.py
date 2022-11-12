from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic, QtGui
import os
import sys

class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)

        self.SetupUI()
        self.SetupButtons()
        self.SetupButtonEvents()
        self.SetupLabels()

        self.show()

    def SetupUI(self):
        self.setWindowIcon(QtGui.QIcon('res/icon.jpg'))

    def SetupButtons(self):
        self.button = self.findChild(QPushButton, "pushButton")
        self.button_2 = self.findChild(QPushButton, "pushButton_2")

    def SetupButtonEvents(self):
        self.button.clicked.connect(self.OpenFile)
        #self.button_2.clicked.connect(self.RecFile)

    def SetupLabels(self):
        self.label = self.findChild(QLabel, "label")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_6 = self.findChild(QLabel, "label_6")


    def OpenFile(self):
        # Чтение файла
        fileName, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Ошибка открытия файла", "Cannot load %s." % fileName)
                return
        # Отображение изображения
        self.label.setPixmap(QPixmap.fromImage(image))
        self.scaleFactor = 1.0
        # Разблокировка кнопки
        self.label_3.setText(fileName)
        if self.label_3.text() != "":
            self.button_2.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())

