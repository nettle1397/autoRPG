from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class MainUI:
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.mainui = QUiLoader().load("GUI/MainUI.ui")

        self.mainui.Start.clicked.connect(self.ConfrmStart)
        self.mainui.Close.clicked.connect(self.ConfrmEnd)

    def ConfrmStart(self):#在遊戲開始畫面，點選開始鈕切換到創角畫面。
        qapp= QApplication.instance()#代入含有關閉視窗的工具包
        qapp.quit()#關閉視窗

    def ConfrmEnd(self):# 在遊戲開始畫面，點選結束鈕後的效果。
        YorN= QMessageBox.question(self.mainui, "自走冒險", "確定要結束？")
        Y= QMessageBox.Yes
        if YorN == Y:
            qapp= QApplication.instance()
            qapp.quit()#關閉視窗
            exit()#結束程式


# Mainroot()