from tkinter import *

root= Tk()
root.title("自走冒險")
root.geometry("720x480")

def BattleScreen():
    EnemyLa1= Label(root, text="E1" , bg= "lightyellow", width= 20)
    EnemyLa2= Label(root, text="E1" , bg= "lightyellow", width= 20)
    EnemyLa3= Label(root, text="E1" , bg= "lightyellow", width= 20)
    EnemyLa4= Label(root, text="E1" , bg= "lightyellow", width= 20)
    EnemyLa5= Label(root, text="E1" , bg= "lightyellow", width= 20)
    Hero1= Label(root, text="E1" , bg= "lightyellow", width= 20)
    Hero2= Label(root, text="E1" , bg= "lightyellow", width= 20)
    Hero3= Label(root, text="E1" , bg= "lightyellow", width= 20)
    SystemBox=Text(root, height=10, width=70)
    SystemBox.pack()
    SystemBox.insert(END,"XDDDDD")

    root.mainloop()

BattleScreen()