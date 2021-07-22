from tkinter import *
from tkinter import messagebox
root= Tk()
root.title("自走冒險")
root.geometry("720x480")

def ConfrmStart():#在遊戲開始畫面，點選開始鈕切換到創角畫面。
    root.destroy()#關閉視窗

def ConfrmEnd():# 在遊戲開始畫面，點選結束鈕後的效果。
    YorN= messagebox.askokcancel("自走冒險", "確定要結束？")
    if YorN == True:
        root.destroy()#關閉視窗
        exit()#結束程式

def Mainroot():
    MainTitle= Label(root, text= "自走冒險", bg= "lightyellow", width= 15).pack()
    StartTitle= Label(root, text= "遊戲開始", bg= "lightyellow", width= 15).pack()
    Start= Button(root, text= "開始", command= ConfrmStart).pack()
    Close= Button(root, text= "結束", command= ConfrmEnd).pack()
    root.mainloop()
    return

# Mainroot()