from tkinter import *
from tkinter import messagebox
window= Tk()
window.title("自走冒險")
window.geometry("720x480")

def ConfrmStart():# 在遊戲開始畫面，點選開始鈕後的效果。
    for widget in window.winfo_children():
        widget.destroy()

def ConfrmEnd():# 在遊戲開始畫面，點選結束鈕後的效果。
    YorN= messagebox.askokcancel("自走冒險", "確定要結束？")
    if YorN == True:
        window.destroy()# 關閉視窗
        exit()# 結束程式

def MainWindow():
    MainTitle= Label(window, text= "自走冒險", bg= "lightyellow", width= 15).pack()
    StartTitle= Label(window, text= "遊戲開始", bg= "lightyellow", width= 15).pack()
    Start= Button(window, text= "開始",command= ConfrmStart).pack()
    Close= Button(window, text= "結束",command= ConfrmEnd).pack()
    window.mainloop()
    return

def CreatCharacter():
    CCTitle= Label(window, text= "創造三位偉大的英雄", bg= "lightyellow", width= 15).grid(row= 0, column= 1)
    Hero1= Label(window, text= "第一位英雄：", bg= "lightyellow", width= 15).grid(row= 1, column= 0)
    name= Label(window, text= "名稱").grid(row= 2, column= 0)
    nameEn= Entry(window).grid(row= 2, column= 1)
    window.mainloop()
CreatCharacter()