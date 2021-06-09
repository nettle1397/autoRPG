#新增python搜尋模組的路徑
import sys
from tkinter.constants import FALSE
sys.path.append("database")
sys.path.append("menu")
sys.path.append("Battle")
sys.path.append("GUI")
import GUI.MainGUI as MGUI

#遊戲開始畫面
game = True
while game == True:
    # 呼叫主畫面
    MGUI.MainWindow()
    #人物創建
    print("創造三位傑出的英雄")
    import menu.CreateCharacter as CChar
    CChar.CreatCharacter()#呼叫創建角色表單

    #將能力值轉換成戰鬥值並儲存
    import database.Control as Cont
    Cont.ChangeChardata()
    
    import Battle.Battle as Battle
    Battle.BattleStart()

    break