# -*- coding: utf-8 -*-
from PySide2 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("GUI")

class CombineImage(QtWidgets.QLabel):
    def __init__(self, srcImagePath=None, dstImagePath=None, parent=None):
        super(CombineImage, self).__init__(parent)
        
        srcImage = QtGui.QImage(srcImagePath)
        dstImage = QtGui.QImage(dstImagePath)
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
        
app =  QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle(u"图片叠加")
window.setWindowFlags(QtCore.Qt.Window)
window.resize(500, 400)
layout = QtWidgets.QHBoxLayout(window)
# 放入圖片，第一張為底層，第二張是上層圖片
layout.addWidget(CombineImage(r"GUI/Empty_Health_Bar.png", r"GUI/Solid_Health_Bar.png"))
window.show()
sys.exit(app.exec_())
