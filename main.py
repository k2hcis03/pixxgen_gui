"""
2022-08-02
픽젠 GUI작업 시작
@K2H
"""
import sys

# from PySide6 import QtWidgets
# from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, QMessageBox, QWidget, QFontDialog
# from PySide6.QtGui import QPixmap, QIcon
# from PySide6.QtCore import Qt, QDir, QFileInfo
# from PySide6.QtUiTools import loadUiType
#
# ui, _ = loadUiType('./ui/main.ui')

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog, QMessageBox, QWidget, QFontDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QDir, QFileInfo
# from PyQt5.QtUiTools import loadUiType
from PyQt5 import uic

ui = uic.loadUiType("./ui/main.ui")[0]


class MainWindow(QMainWindow, ui):
    def __init__(self):
        super(MainWindow, self).__init__()
        # icon = QIcon("./asserts/bell.png")
        # self.setWindowTitle('AVG Antivirus Free')
        self.collimator_rotate = 1
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setWindowIcon(icon)
        self.setupUi(self)
        self.pushButton_select_colimator.clicked.connect(self.chang_collimator)

    def chang_collimator(self):
        self.collimator_rotate += 1
        self.collimator_rotate %= 5

        if self.collimator_rotate == 0:
            self.collimator_rotate = 1

        collimator_border = f'QPushButton{{border: none;}}'
        collimator_choice = f'QPushButton{{background-image: url(:/images/m_collimator{self.collimator_rotate}_down.png)}}'
        self.pushButton_10.setStyleSheet(collimator_border + collimator_choice)


def main():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print('Exiting')


if __name__ == '__main__':
    main()
