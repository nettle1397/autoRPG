from PySide2.QtWidgets import QApplication, QMainWindow
from Test_3 import *

class UI(QMainWindow, Ui_Form):
    def __init__(self, parent= None):
        # QMainWindow.__init__(self, parent)
        super(UI, self).__init__(parent)
        # self.ui= Ui_Form()
        self.setupUi(self)
        self.setCentralWidget(self.widget)#讓副視窗綁定中心視窗
        # for i in range(self.verticalLayout.count()):
        #     self.verticalLayout.itemAt(i).widget().deleteLater()

if __name__== "__main__":
    app= QApplication()
    MUI= UI()
    MUI.show()
    app.exec_()