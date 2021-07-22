#新增python搜尋模組的路徑
import sys
sys.path.append("database")
sys.path.append("menu")
sys.path.append("Battle")
sys.path.append("GUI")

#呼叫PySide2相關工具
# from PySide2.QtCore import 
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from GUI.MainUI2 import Ui_root

#遊戲開始畫面
class MainUI(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self, parent)
        super().__init__()
        self.mainui= Ui_root()
        self.mainui.setupUi(self)

        self.mainui.Start.clicked.connect(self.__ConfrmStart)
        self.mainui.Close.clicked.connect(self.__ConfrmEnd)

    def __ConfrmStart(self):#在遊戲開始畫面，點選開始鈕切換到創角畫面。
        __qapp= QApplication.instance()#代入含有關閉視窗的工具包
        __qapp.quit()#關閉視窗

    def __ConfrmEnd(self):# 在遊戲開始畫面，點選結束鈕後的效果。
        __YorN= QMessageBox.question(self.mainui, "自走冒險", "確定要結束？")
        if __YorN == QMessageBox.Yes:
            __qapp= QApplication.instance()
            __qapp.quit()#關閉視窗
            exit()#結束程式

# if __name__ == '__main__':
app= QApplication()
MUI= MainUI()
MUI.show()
app.exec_()

# class CreateCharacter:
#     import json
#     import database.Control as cont

#創角畫面
# import GUI.CreateCharacterGUI as CCGUI
# CCGUI.CreateCharacter()#呼叫創角畫面
    
# import Battle.Battle as Battle
# Battle.BattleStart()
