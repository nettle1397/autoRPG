# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QLabel, QApplication, QMainWindow
from Test_UI_5 import *

class UI(QMainWindow, QLabel, Ui_Form):
    def __init__(self, parent= None):
        # QMainWindow.__init__(self, parent)
        super(UI, self).__init__(parent)
        # self.ui= Ui_Form()
        self.setupUi(self)
        self.setCentralWidget(self.widget)#讓副視窗綁定中心視窗
        
        srcImage = QtGui.QImage("GUI/Empty_Health_Bar.png")
        dstImage = QtGui.QImage("GUI/Solid_Health_Bar.png")
        resultImage = QtGui.QImage(
                        srcImage.width(),
                        srcImage.height(),
                        QtGui.QImage.Format_ARGB32_Premultiplied
                        )
        painter = QtGui.QPainter(resultImage)
        painter.fillRect(resultImage.rect(), QtCore.Qt.transparent)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
        painter.drawImage(0, 0, srcImage)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceOver)
        painter.drawImage(0, 0, dstImage)
        painter.end()
        self.setPixmap(QtGui.QPixmap.fromImage(resultImage))

if __name__== "__main__":
    app= QApplication()
    MUI= UI()
    MUI.show()
    app.exec_()