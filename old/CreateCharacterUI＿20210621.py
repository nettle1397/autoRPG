from tkinter import *
import json
import database.Control as cont

# class CreateCharacterUI:
#     def __init__(self):
#         self.__CCUI = QUiLoader().load("GUI\CreatrCharacterUI.ui")

def strelower():
    global streAP
    global avaAP
    if avaAP< 3:
        if avaAP> 0 and streAP> 6:
            avaAP+= 1
            streAP-= 1
        elif streAP> 6:
            avaAP+= 1
            streAP-= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    streVal.config(text= streAP)
    
def streHoist():
    global streAP
    global avaAP
    if avaAP> 0:
        if avaAP<= 3:
            avaAP-= 1
            streAP+= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    streVal.config(text= streAP)

agiAP= 6    
def agilower():
    global agiAP
    global avaAP
    if avaAP< 3:
        if avaAP> 0 and agiAP> 6:
            avaAP+= 1
            agiAP-= 1
        elif agiAP> 6:
            avaAP+= 1
            agiAP-= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    agiVal.config(text= agiAP)

def agiHoist():
    global agiAP
    global avaAP
    if avaAP> 0:
        if avaAP<= 3:
            avaAP-= 1
            agiAP+= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    agiVal.config(text= agiAP)

inteAP= 6
def intelower():
    global inteAP
    global avaAP
    if avaAP< 3:
        if avaAP> 0 and inteAP> 6:
            avaAP+= 1
            inteAP-= 1
        elif inteAP> 6:
            avaAP+= 1
            inteAP-= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    inteVal.config(text= inteAP)

def inteHoist():
    global inteAP
    global avaAP
    if avaAP> 0:
        if avaAP<= 3:
            avaAP-= 1
            inteAP+= 1
    APLa.config(text= "目前有"+ str(avaAP)+ "點可以加點")
    inteVal.config(text= inteAP)

Herosn= 1
def wordability():
    global Herosn
    global streAP
    global agiAP
    global inteAP
    for X in range(4):
        if X== 0:
            dksn= 0
            DataKey= "name"
            val= nameVal.get()
            cont.character(Herosn, dksn, DataKey, val)
        elif X== 1:
            dksn= 3
            DataKey= "stre"
            val= streAP
            cont.character(Herosn, dksn, DataKey, val)
        elif X== 2:
            dksn= 4
            DataKey= "agi"
            val= agiAP
            cont.character(Herosn, dksn, DataKey, val)
        elif X== 3:
            dksn= 5
            DataKey= "inte"
            val= inteAP
            cont.character(Herosn, dksn, DataKey, val)
    cont.ChangeChardata(Herosn)

def NextHero():#顯示下一位英雄
    global Herosn
    wordability()
    for widget in root.winfo_children():#逐一將控件代入widget變數
        widget.destroy()
    Herosn+= 1
    CreateCharacter()

def ShowAbility():#建立完三位英雄後，在下一頁列出三位英雄能力值。
    global Herosn
    wordability()
    for widget in root.winfo_children():#逐一將控件代入widget變數
        widget.destroy()
    AbilityList()
  
root= Tk()
root.title("自走冒險")
root.geometry("720x480")

def CreateCharacter():
    global APLa
    global nameVal
    global streVal
    global agiVal
    global inteVal
    global avaAP
    global streAP
    global agiAP
    global inteAP
    avaAP= 3
    streAP= 6
    agiAP= 6
    inteAP=6
    if Herosn== 1:
        Hero= Label(root, text= "第一位英雄", bg= "lightyellow", width= 10)
    elif Herosn== 2:
        Hero= Label(root, text= "第二位英雄", bg= "lightyellow", width= 10)
    elif Herosn== 3:
        Hero= Label(root, text= "第三位英雄", bg= "lightyellow", width= 10)

    CCTitle= Label(root, text= "創造三位偉大的英雄", bg= "lightyellow", width= 20)
    APLa= Label(root, text= "目前有"+ str(avaAP)+ "點可以加點", bg= "lightyellow", width= 20)
    nameLa= Label(root, text= "名稱")
    nameVal= Entry(root)#輸入英雄名稱
    streLa= Label(root, text= "力量")
    strelowerBu= Button(root, text= "<", command= strelower)
    streVal= Label(root, text= streAP, width= 5)
    streHoistBu= Button(root, text= ">", command= streHoist)
    agiLa= Label(root, text= "敏捷")
    agilowerBu= Button(root, text= "<", command= agilower)
    agiVal= Label(root, text= agiAP, width= 5)
    agiHoistBu= Button(root, text= ">", command= agiHoist)
    inteLa= Label(root, text= "智力")
    intelowerBu= Button(root, text= "<", command= intelower)
    inteVal= Label(root, text= inteAP, width= 5)
    inteHoistBu= Button(root, text= ">", command= inteHoist)
    if Herosn== 3:#第三位英雄的下一頁是列出三位英雄能力值
        next_= Button(root, text= "下一頁", command=ShowAbility)
    else:
        next_= Button(root, text= "下一頁", command=NextHero)

    CCTitle.grid(row= 0, column= 1)
    Hero.grid(row= 1, column= 0)
    APLa.grid(row= 1, column= 1)
    nameLa.grid(row= 2, column= 0)
    nameVal.grid(row= 2, column= 1)
    streLa.grid(row= 3, column= 0)
    strelowerBu.grid(row= 3, column= 1)
    streVal.grid(row= 3, column= 2)
    streHoistBu.grid(row= 3, column= 3)
    agiLa.grid(row= 4, column= 0)
    agilowerBu.grid(row= 4, column= 1)
    agiVal.grid(row= 4, column= 2)
    agiHoistBu.grid(row= 4, column= 3)
    inteLa.grid(row= 5, column= 0)
    intelowerBu.grid(row= 5, column= 1)
    inteVal.grid(row= 5, column= 2)
    inteHoistBu.grid(row= 5, column= 3)
    next_.grid(row= 6, column= 0)

    root.mainloop()

def AbilityList():
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取資料，寫入char

    for sn in range(1, 4):
        name= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][0]["name"]
        stre= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][3]["stre"]
        agi= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][4]["agi"]
        inte= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][5]["inte"]
        if sn== 1:
            name1= name
            stre1= str(stre)
            agi1= str(agi)
            inte1= str(inte)
        elif sn== 2:
            name2= name
            stre2= str(stre)
            agi2= str(agi)
            inte2= str(inte)
        elif sn== 3:
            name3= name
            stre3= str(stre)
            agi3= str(agi)
            inte3= str(inte)

    AbiTitle= Label(root, text= "英雄能力值", bg= "lightyellow", width= 20)
    Hero1= Label(root, text="第一位英雄名稱："+ name1, bg= "lightyellow", width= 20)
    stre1= Label(root, text="力量："+ stre1, bg= "lightyellow", width= 20)
    agi1= Label(root, text="敏捷："+ agi1, bg= "lightyellow", width= 20)
    inte1= Label(root, text="智力："+ inte1, bg= "lightyellow", width= 20)
    Hero2= Label(root, text="第二位英雄名稱："+ name, bg= "lightyellow", width= 20)
    stre2= Label(root, text="力量："+ stre2, bg= "lightyellow", width= 20)
    agi2= Label(root, text="敏捷："+ agi2, bg= "lightyellow", width= 20)
    inte2= Label(root, text="智力："+ inte2, bg= "lightyellow", width= 20)
    Hero3= Label(root, text="第三位英雄名稱："+ name, bg= "lightyellow", width= 20)
    stre3= Label(root, text="力量："+ stre3, bg= "lightyellow", width= 20)
    agi3= Label(root, text="敏捷："+ agi3, bg= "lightyellow", width= 20)
    inte3= Label(root, text="智力："+ inte3, bg= "lightyellow", width= 20)

    AbiTitle.grid(row= 0, column= 1)
    Hero1.grid(row= 1, column= 0)
    stre1.grid(row= 2, column= 0)
    agi1.grid(row= 3, column= 0)
    inte1.grid(row= 4, column= 0)
    Hero2.grid(row= 1, column= 1)
    stre2.grid(row= 2, column= 1)
    agi2.grid(row= 3, column= 1)
    inte2.grid(row= 4, column= 1)
    Hero3.grid(row= 1, column= 2)
    stre3.grid(row= 2, column= 2)
    agi3.grid(row= 3, column= 2)
    inte3.grid(row= 4, column= 2)

    root.mainloop()