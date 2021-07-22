import sys
sys.path.append("database")
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import json
import Control as cont

class CreateCharacterUI:    
    def __init__(self):
        self.CCUI = QUiLoader().load("GUI/CreatrCharacterUI2.ui")
        self.AVA_AP= 3
        self.atre_ap= 6    
        self.agi_ap= 6
        self.inte_ap= 6
        self.con_ap= 6
        self.wis_ap= 6
        self.CCUI.nameVal_2.textChanged.connect(self.nameVal)
        self.CCUI.strelowerBu_2.clicked.connect(self.strelower)
        self.CCUI.streHoistBu_2.clicked.connect(self.streHoist)
        self.CCUI.agilowerBu_2.clicked.connect(self.agilower)
        self.CCUI.agiHoistBu_2.clicked.connect(self.agiHoist)
        self.CCUI.intelowerBu_2.clicked.connect(self.intelower)
        self.CCUI.inteHoistBu_2.clicked.connect(self.inteHoist)
        self.CCUI.conlowerBu_2.clicked.connect(self.conlower)
        self.CCUI.conHoistBu_2.clicked.connect(self.conHoist)
        self.CCUI.wislowerBu_2.clicked.connect(self.wislower)
        self.CCUI.wisHoistBu_2.clicked.connect(self.wisHoist)
        self.CCUI.nextpage.clicked.connect(self.NextPage)

    def nameVal(self, text):
        self.nameval= text

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
        self.CCUI.agiVal_2.setText(str(self.agi_ap))

    def agiHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.agi_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.agiVal_2.setText(str(self.agi_ap))
    
    def intelower(self):
        if self.AVA_AP< 3:
            if self.AVA_AP> 0 and self.inte_ap> 6:
                self.AVA_AP+= 1
                self.inte_ap-= 1
            elif self.inte_ap> 6:
                self.AVA_AP+= 1
                self.inte_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.inteVal_2.setText(str(self.inte_ap))

    def inteHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.inte_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.inteVal_2.setText(str(self.inte_ap))
        
    def conlower(self):
        if self.AVA_AP> 0 and self.con_ap> 6:
            self.AVA_AP+= 1
            self.con_ap-= 1
        elif self.con_ap> 6:
            self.AVA_AP+= 1
            self.con_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.conVal_2.setText(str(self.con_ap))

    def conHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.con_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.conVal_2.setText(str(self.con_ap))

    def wislower(self):
        if self.AVA_AP> 0 and self.wis_ap> 6:
            self.AVA_AP+= 1
            self.wis_ap-= 1
        elif self.wis_ap> 6:
            self.AVA_AP+= 1
            self.wis_ap-= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.wisVal_2.setText(str(self.wis_ap))

    def wisHoist(self):
        if self.AVA_AP> 0:
            self.AVA_AP-= 1
            self.wis_ap+= 1
        self.CCUI.APLa_2.setText(str(self.AVA_AP))
        self.CCUI.wisVal_2.setText(str(self.wis_ap))

    def wordability(self):
        Herosn= 1
        for X in range(6):
            if X== 0:
                dksn= 0
                DataKey= "name"
                val= self.nameval
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 1:
                dksn= 3
                DataKey= "stre"
                val= self.atre_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 2:
                dksn= 4
                DataKey= "agi"
                val= self.agi_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 3:
                dksn= 5
                DataKey= "inte"
                val= self.inte_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 4:
                dksn= 5
                DataKey= "con"
                val= self.con_ap
                cont.character(Herosn, dksn, DataKey, val)
            elif X== 5:
                dksn= 5
                DataKey= "wis"
                val= self.wis_ap
                cont.character(Herosn, dksn, DataKey, val)
        cont.ChangeChardata(Herosn)

    def NextPage(self):#顯示下一頁
        if self.AVA_AP== 0:
            if self.nameval!= None:
                self.wordability()
                qapp= QApplication.instance()
                qapp.quit()
            else:
                QMessageBox.about(self.CCUI, "自走冒險", "名稱不能空白。")
        else:
            QMessageBox.about(self.CCUI, "自走冒險", "英雄的能力點未使用完。")

if __name__== "__main__":
    app= QApplication()
    MUI= CreateCharacterUI()
    MUI.CCUI.show()
    app.exec_()
    