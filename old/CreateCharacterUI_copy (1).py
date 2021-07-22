from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import sys
sys.path.append("database")
import json
import database.Control as cont

class CreateCharacterUI:    
    AVA_AP= 3
    def __init__(self):
        self.CCUI = QUiLoader().load("GUI/CreatrCharacterUI2.ui")
        self.atre_ap= 6    
        self.agi_ap= 6
        self.inte_ap= 6
        self.con_ap= 6
        self.wis_ap= 6
        self.CCUI.strelowerBu_2.clicked.connect(self.strelower)
        self.CCUI.streHoistBu_2.clicked.connect(self.streHoist)
        self.CCUI.strelowerBu_2.clicked.connect(self.agilower)
        self.CCUI.streHoistBu_2.clicked.connect(self.agiHoist)
        self.CCUI.strelowerBu_2.clicked.connect(self.intelower)
        self.CCUI.streHoistBu_2.clicked.connect(self.inteHoist)
        self.CCUI.strelowerBu_2.clicked.connect(self.conlower)
        self.CCUI.streHoistBu_2.clicked.connect(self.conHoist)
        self.CCUI.strelowerBu_2.clicked.connect(self.wislower)
        self.CCUI.streHoistBu_2.clicked.connect(self.wisHoist)

    def strelower(self):
        if self.AVA_AP< 3:
            if self.AVA_AP> 0 and self.atre_ap> 6:
                self.AVA_AP+= 1
                self.atre_ap-= 1
            elif self.atre_ap> 6:
                self.AVA_AP+= 1
                self.atre_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.atre_ap))
    
    def streHoist(self):
        if self.AVA_AP> 0:
            if self.AVA_AP<= 3:
                self.AVA_AP-= 1
                self.atre_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.atre_ap))

    def agilower(self):
        if self.AVA_AP< 3:
            if self.AVA_AP> 0 and self.agi_ap> 6:
                self.AVA_AP+= 1
                self.agi_ap-= 1
            elif self.agi_ap> 6:
                self.AVA_AP+= 1
                self.agi_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.agi_ap))

    def agiHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.agi_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.agi_ap))
    
    def intelower(self):
        if self.AVA_AP< 3:
            if self.AVA_AP> 0 and self.inte_ap> 6:
                self.AVA_AP+= 1
                self.inte_ap-= 1
        elif self.inte_ap> 6:
            self.AVA_AP+= 1
            self.inte_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.inte_ap))

    def inteHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.inte_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.streVal_2.setText(str(self.inte_ap))
        
    def conlower(self):
        if self.AVA_AP> 0 and self.con_ap> 6:
            self.AVA_AP+= 1
            self.con_ap-= 1
        elif self.con_ap> 6:
            self.AVA_AP+= 1


    Herosn= 1
    def wordability(self):
        global Herosn
        global atre_ap
        global agi_ap
        global inte_ap
        for X in range(4):
            if X== 0:
                dksn= 0
                DataKey= "name"
                val= nameVal.get()
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 1:
                dksn= 3
                DataKey= "stre"
                val= atre_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 2:
                dksn= 4
                DataKey= "agi"
                val= agi_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 3:
                dksn= 5
                DataKey= "inte"
                val= inte_ap
                cont.character(Herosn, dksn, DataKey, val)
        cont.ChangeChardata(Herosn)

    def NextHero(self):#顯示下一位英雄
        global Herosn
        wordability()
        for widget in root.winfo_children():#逐一將控件代入widget變數
            widget.destroy()
        Herosn+= 1
        CreateCharacter()

if __name__== "__main__":
    app= QApplication()
    MUI= CreateCharacterUI()
    MUI.CCUI.show()
    app.exec_()
    # def ShowAbility():#建立完三位英雄後，在下一頁列出三位英雄能力值。
    #     global Herosn
    #     wordability()
    #     for widget in root.winfo_children():#逐一將控件代入widget變數
    #         widget.destroy()
    #     AbilityList()
  

# def CreateCharacter():
#     global APLa
#     global nameVal
#     global streVal
#     global agiVal
#     global inteVal
#     global AVA_AP
#     global atre_ap
#     global agi_ap
#     global inte_ap
#     AVA_AP= 3
#     atre_ap= 6
#     agi_ap= 6
#     inte_ap=6
#     if Herosn== 1:
#         Hero= Label(root, text= "第一位英雄", bg= "lightyellow", width= 10)
#     elif Herosn== 2:
#         Hero= Label(root, text= "第二位英雄", bg= "lightyellow", width= 10)
#     elif Herosn== 3:
#         Hero= Label(root, text= "第三位英雄", bg= "lightyellow", width= 10)

#     CCTitle= Label(root, text= "創造三位偉大的英雄", bg= "lightyellow", width= 20)
#     APLa= Label(root, text= "目前有"+ str(AVA_AP)+ "點可以加點", bg= "lightyellow", width= 20)
#     nameLa= Label(root, text= "名稱")
#     nameVal= Entry(root)#輸入英雄名稱
#     streLa= Label(root, text= "力量")
#     strelowerBu= Button(root, text= "<", command= strelower)
#     streVal= Label(root, text= atre_ap, width= 5)
#     streHoistBu= Button(root, text= ">", command= streHoist)
#     agiLa= Label(root, text= "敏捷")
#     agilowerBu= Button(root, text= "<", command= agilower)
#     agiVal= Label(root, text= agi_ap, width= 5)
#     agiHoistBu= Button(root, text= ">", command= agiHoist)
#     inteLa= Label(root, text= "智力")
#     intelowerBu= Button(root, text= "<", command= intelower)
#     inteVal= Label(root, text= inte_ap, width= 5)
#     inteHoistBu= Button(root, text= ">", command= inteHoist)
#     if Herosn== 3:#第三位英雄的下一頁是列出三位英雄能力值
#         next_= Button(root, text= "下一頁", command=ShowAbility)
#     else:
#         next_= Button(root, text= "下一頁", command=NextHero)

#     CCTitle.grid(row= 0, column= 1)
#     Hero.grid(row= 1, column= 0)
#     APLa.grid(row= 1, column= 1)
#     nameLa.grid(row= 2, column= 0)
#     nameVal.grid(row= 2, column= 1)
#     streLa.grid(row= 3, column= 0)
#     strelowerBu.grid(row= 3, column= 1)
#     streVal.grid(row= 3, column= 2)
#     streHoistBu.grid(row= 3, column= 3)
#     agiLa.grid(row= 4, column= 0)
#     agilowerBu.grid(row= 4, column= 1)
#     agiVal.grid(row= 4, column= 2)
#     agiHoistBu.grid(row= 4, column= 3)
#     inteLa.grid(row= 5, column= 0)
#     intelowerBu.grid(row= 5, column= 1)
#     inteVal.grid(row= 5, column= 2)
#     inteHoistBu.grid(row= 5, column= 3)
#     next_.grid(row= 6, column= 0)

#     root.mainloop()

# def AbilityList():
#     with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
#         char = json.load(charT) #讀取資料，寫入char

#     for sn in range(1, 4):
#         name= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][0]["name"]
#         stre= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][3]["stre"]
#         agi= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][4]["agi"]
#         inte= char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][5]["inte"]
#         if sn== 1:
#             name1= name
#             stre1= str(stre)
#             agi1= str(agi)
#             inte1= str(inte)
#         elif sn== 2:
#             name2= name
#             stre2= str(stre)
#             agi2= str(agi)
#             inte2= str(inte)
#         elif sn== 3:
#             name3= name
#             stre3= str(stre)
#             agi3= str(agi)
#             inte3= str(inte)

#     AbiTitle= Label(root, text= "英雄能力值", bg= "lightyellow", width= 20)
#     Hero1= Label(root, text="第一位英雄名稱："+ name1, bg= "lightyellow", width= 20)
#     stre1= Label(root, text="力量："+ stre1, bg= "lightyellow", width= 20)
#     agi1= Label(root, text="敏捷："+ agi1, bg= "lightyellow", width= 20)
#     inte1= Label(root, text="智力："+ inte1, bg= "lightyellow", width= 20)
#     Hero2= Label(root, text="第二位英雄名稱："+ name, bg= "lightyellow", width= 20)
#     stre2= Label(root, text="力量："+ stre2, bg= "lightyellow", width= 20)
#     agi2= Label(root, text="敏捷："+ agi2, bg= "lightyellow", width= 20)
#     inte2= Label(root, text="智力："+ inte2, bg= "lightyellow", width= 20)
#     Hero3= Label(root, text="第三位英雄名稱："+ name, bg= "lightyellow", width= 20)
#     stre3= Label(root, text="力量："+ stre3, bg= "lightyellow", width= 20)
#     agi3= Label(root, text="敏捷："+ agi3, bg= "lightyellow", width= 20)
#     inte3= Label(root, text="智力："+ inte3, bg= "lightyellow", width= 20)

#     AbiTitle.grid(row= 0, column= 1)
#     Hero1.grid(row= 1, column= 0)
#     stre1.grid(row= 2, column= 0)
#     agi1.grid(row= 3, column= 0)
#     inte1.grid(row= 4, column= 0)
#     Hero2.grid(row= 1, column= 1)
#     stre2.grid(row= 2, column= 1)
#     agi2.grid(row= 3, column= 1)
#     inte2.grid(row= 4, column= 1)
#     Hero3.grid(row= 1, column= 2)
#     stre3.grid(row= 2, column= 2)
#     agi3.grid(row= 3, column= 2)
#     inte3.grid(row= 4, column= 2)

#     root.mainloop()