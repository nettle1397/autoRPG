#新增python搜尋模組的路徑
import sys
sys.path.append("database")
sys.path.append("menu")
sys.path.append("Battle")

#import Battle.Battle as Battle
#Battle.BattleStart()

#遊戲開始畫面
print("!!自走冒險!!")
game = True
while game == True:
    A = input("遊戲開始\n開始請輸入[Y]，或是結束請輸入[N]: ")
    while A != "Y" or A != "y":
        if A == "N" or A == "n":
            break
        elif  A == "Y" or A == "y":
            break
        A = input("遊戲開始\n開始請輸入[Y]，結束請輸入[N]: ")
    if A == "N" or A == "n":
            break

    #人物創建
    print("創造三位傑出的英雄")
    import menu.CreateCharacter as CChar
    CChar.CreatCharacter()#呼叫創建角色表單

    #將能力值轉換成戰鬥值並儲存
    import database.Control as Cont
    sn = 0
    while sn < 3:
        sn += 1
        Cont.ChangeChardata(sn)
    
    import Battle.Battle as Battle
    Battle.BattleStart()

    break