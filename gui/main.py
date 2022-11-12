from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic, QtGui

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)
        self.setWindowIcon(QtGui.QIcon('res/icon.jpg'))

        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        self.button.clicked.connect(self.clicker)

        self.show()

    def clicker(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File")
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Ошибка открытия файла", "Cannot load %s." % fileName)
                return
        self.label.setPixmap(QPixmap.fromImage(image))
        self.scaleFactor = 1.0

def main():
    app = QApplication([])
    window = UI()
    app.exec_()

if __name__ == "__main__":
    main()