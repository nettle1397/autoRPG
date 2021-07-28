import random
import json
from os import path

def D24(DiceNumerator):#D24系統，參數是分子，決定機率高低
    import random
    Dice = random.randint(1,24)#創造一顆1到24點的骰子，並擲骰。

    #擲骰結果，與分子做比對，分子數以下表示成功，否則失敗。
    if Dice <= DiceNumerator:
        result = True
    else:
        result = False

    return result

def Time(time, Move):#速度值計時器
    move = Move // 1
    while time != move:
        time += 1
    return time

def movevalue(combat_val):
    move_value = 0
    for i in range(combat_val.Speed):
        move_value += D24(12)

    if combat_val.SpeedRemainder == 1:
        move_value += D24(4)
    elif combat_val.SpeedRemainder == 2:
        move_value += D24(8) 

    move_value += combat_val.BasicSpeed
    if move_value > 0:
        move_value =  round(1000 / move_value, 2)

    combat_val.move_value += move_value

    return {combat_val.move_unit:combat_val.move_value}

def Target(unit_set):#隨機選擇對手
    battle_start = BattleStart()
    unit_list = list(unit_set)
    target = random.choice(unit_list)
    
    return target

def damage_calculation(damage_data): # 結算傷害，參數函式，包含計算傷害的數值。
    Impairment = damage_data.Hit - damage_data.Impairment
    if Impairment < 0:
        Impairment = 0
    damage_data.HP -= (damage_data.Attack - Impairment)
    return damage_data.HP

class CharacterData:
    def __init__(self):
        database = path.join(path.dirname(__file__), "database")
        with open(path.join(database, "CharacterData.json"), mode = 'r', encoding = 'utf-8') as charD:
            self.char = json.load(charD) #讀取所有單位資料，寫入char
        super().__init__()

class UnitGroup:
    def __init__(self):
        database = path.join(path.dirname(__file__), "database")
        with open(path.join(database, "Group.json"), mode = 'r', encoding = 'utf-8') as Group:
            G = json.load(Group)
        self.group = list(G.items()) # 英雄和敵人的隊伍群組
        super().__init__()

class HeroCombatVal(CharacterData):
    def __init__(self, SerialNumber, unit, move_unit):
        super().__init__()
        self.name = self.char["Hero"][SerialNumber][unit][0]["Ability"][0]["name"]
        self.race = self.char["Hero"][SerialNumber][unit][0]["Ability"][1]["race"]
        self.HP = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][0]["HP"]
        self.Attack = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][1]["Attack"]
        self.AttackRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][2]["AttackRemainder"]
        self.Speed = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][3]["Speed"]
        self.BasicSpeed = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][4]["BasicSpeed"]
        self.SpeedRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][5]["SpeedRemainder"]
        self.FinalHit = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][6]["FinalHit"]
        self.AgiHitRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][7]["AgiHitRemainder"]
        self.InteHitRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][8]["InteHitRemainder"]
        self.AgiImpairment = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][9]["AgiImpairment"]
        self.AgiImpairmentRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][10]["AgiImpairmentRemainder"]
        self.ConImpairment = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][11]["ConImpairment"]
        self.ConImpairmentRemainder = self.char["Hero"][SerialNumber][unit][1]["CombatVal"][12]["ConImpairmentRemainder"]
        self.Impairment = 0
        self.move_unit = move_unit
        self.move_value = 0
        self.first_move = False
        self.hero_target = False
        self.enemy_target = False

class EnemyCombatVal(CharacterData):
    def __init__(self, SerialNumber, unit, move_unit):
        super().__init__()
        self.name = self.char["Enemy"][SerialNumber][unit][0]["name"]
        self.race = self.char["Enemy"][SerialNumber][unit][1]["race"]
        self.HP = self.char["Enemy"][SerialNumber][unit][2]["HP"]
        self.Attack = self.char["Enemy"][SerialNumber][unit][3]["Attack"]
        self.Speed = self.char["Enemy"][SerialNumber][unit][4]["Speed"]
        self.BasicSpeed = self.char["Enemy"][SerialNumber][unit][5]["BasicSpeed"]
        self.FinalHit = self.char["Enemy"][SerialNumber][unit][6]["Hit"]
        self.Impairment = self.char["Enemy"][SerialNumber][unit][7]["Impairment"]
        self.AttackRemainder = 0
        self.AgiHitRemainder = 0
        self.InteHitRemainder = 0
        self.AgiImpairment = 0
        self.AgiImpairmentRemainder = 0
        self.ConImpairment = 0
        self.ConImpairmentRemainder = 0
        self.SpeedRemainder = 0
        self.move_unit = move_unit
        self.move_value = 0
        self.first_move = False
        self.hero_target = False
        self.enemy_target = False

class BattleStart(UnitGroup):
    def __init__(self):
        super().__init__()
        unit_data_base = self.group # 建立群組資料庫
        hero_unit_0 = list(unit_data_base[0][1][0].items()) # 抓取英雄的鍵與序號
        hero_unit_1 = list(unit_data_base[0][1][1].items())
        hero_unit_2 = list(unit_data_base[0][1][2].items())
        #建立角色物件
        self.hero_0 = HeroCombatVal(
                                hero_unit_0[0][1], # 角色在群組資料庫(CharacterData.json)裡的序號
                                hero_unit_0[0][0], # 角色在群組資料庫(CharacterData.json)裡的鍵
                                "hero_0" # 識別名稱
                                )
        self.hero_1 = HeroCombatVal(
                                hero_unit_1[0][1],
                                hero_unit_1[0][0],
                                "hero_1"
                                )
        self.hero_2 = HeroCombatVal(
                                hero_unit_2[0][1],
                                hero_unit_2[0][0],
                                "hero_2"
                                )

        enemy_unit_0 = list(unit_data_base[3][1][0]["0"][0].items())
        enemy_unit_1 = list(unit_data_base[3][1][1]["1"][0].items())
        enemy_unit_2 = list(unit_data_base[3][1][2]["2"][0].items())
        enemy_unit_3 = list(unit_data_base[3][1][3]["3"][0].items())
        enemy_unit_4 = list(unit_data_base[3][1][4]["4"][0].items())
        self.enemy_0 = EnemyCombatVal(
                                enemy_unit_0[0][1],
                                enemy_unit_0[0][0],
                                "enemy_0"
                                )
        self.enemy_1 = EnemyCombatVal(
                                enemy_unit_1[0][1],
                                enemy_unit_1[0][0],
                                "enemy_1"
                                )
        self.enemy_2 = EnemyCombatVal(
                                enemy_unit_2[0][1],
                                enemy_unit_2[0][0],
                                "enemy_2"
                                )
        self.enemy_3 = EnemyCombatVal(
                                enemy_unit_3[0][1],
                                enemy_unit_3[0][0],
                                "enemy_3"
                                )
        self.enemy_4 = EnemyCombatVal(
                                enemy_unit_4[0][1],
                                enemy_unit_4[0][0],
                                "enemy_4"
                                )
        self.move_dict = {}
        self.hero_set = {}
        self.enemy_set = {}
        self.First_move = "n"

    def move_sequence(self): # 戰鬥開始
        if self.First_move[0] == "hero_0" or len(self.move_dict) == 0: # 若行動序列(move_dict)是空的，放入此角色的行動值，或是如果此角色上回合行動，計算新的行動值。
            self.move_dict.update(movevalue(self.hero_0))
            self.first_move_unit = self.hero_0
            self.hero_set.add("hero_0") # 寫入選擇對手時的選項
            opponent = 1 # 先手單位的對手，0表示對手是玩家，1表示對手是敵人
        if self.First_move[0] == "hero_1" or len(self.move_dict) == 1:
            self.move_dict.update(movevalue(self.hero_1))
            self.first_move_unit = self.hero_1
            self.hero_set.add("hero_1")
            opponent = 1
        if self.First_move[0] == "hero_2" or len(self.move_dict) == 2:
            self.move_dict.update(movevalue(self.hero_2))
            self.first_move_unit = self.hero_2
            self.hero_set.add("hero_2")
            opponent = 1
        if self.First_move[0] == "enemy_0" or len(self.move_dict) == 3:
            self.move_dict.update(movevalue(self.enemy_0))
            self.first_move_unit = self.enemy_0
            self.enemy_set.add("enemy_0")
            opponent = 0
        if self.First_move[0] == "enemy_1" or len(self.move_dict) == 4:
            if self.enemy_1.move_unit != "no_unit": # 若是no_unit，表示沒有生成敵人，則不放入行動值。
                self.move_dict.update(movevalue(self.enemy_1))
                self.first_move_unit = self.enemy_1
                self.enemy_set.add("enemy_1")
                opponent = 0
        if self.First_move[0] == "enemy_2" or len(self.move_dict) == 5:
            if self.enemy_2.move_unit == "no_unit":
                pass
            else:
                self.move_dict.update(movevalue(self.enemy_2))
                self.first_move_unit = self.enemy_2
                self.enemy_set.add("enemy_2")
                opponent = 0
        if self.First_move[0] == "enemy_3" or len(self.move_dict) == 6:
            if self.enemy_3.move_unit == "no_unit":
                pass
            else:
                self.move_dict.update(movevalue(self.enemy_3))
                self.first_move_unit = self.enemy_3
                self.enemy_set.add("enemy_3")
                opponent = 0
        if self.First_move[0] == "enemy_4" or len(self.move_dict) == 7:
            if self.enemy_4.move_unit == "no_unit":
                pass
            else:
                self.move_dict.update(movevalue(self.enemy_4))
                self.first_move_unit = self.enemy_4
                self.enemy_set.add("enemy_4")
                opponent = 0
        
        move_tuple = sorted(list(self.move_dict.items()), key = lambda item:item[1]) # 將行動值排序
        self.First_move = move_tuple[0] # 取出先手單位
        if opponent:
            self.unit_set = self.enemy_set
        else:
            self.unit_set = self.hero_set

    def close_an_account(self):
        self.target = Target(self.unit_set)
        Attack = self.first_move_unit.Attack + D24(self.first_move_unit.AttackRemainder)
        Hit = D24(self.first_move_unit.FinalHit) + D24(self.first_move_unit.AgiHitRemainder) + D24(self.first_move_unit.inteHitRemainder)
        switch = True
        while switch == True:
            if self.hero_0.enemy_target == True: # 結算完傷害或是其他行動後，將結果返回先手或目標單位。
                self.hero_0.enemy_target = False
                self.hero_0.HP = HP
                switch = False
            elif "hero_0" == self.target: # 導入目標單位屬性
                self.hero_0.enemy_target = True
                HP = self.hero_0.HP
                switch = False
                Impairment = D24(self.hero_0.AgiImpairment) + D24(self.hero_0.AgiImpairmentRemainder) + D24(self.hero_0.ConImpairment) + D24(self.hero_0.ConImpairmentRemainder)
            
            if self.hero_1.enemy_target == True:
                self.hero_1.enemy_target = False
                self.hero_1.HP = HP
                switch = False
            elif "hero_1" == self.target:
                self.hero_1.enemy_target = True
                HP = self.hero_1.HP
                Impairment = D24(self.hero_1.AgiImpairment) + D24(self.hero_1.AgiImpairmentRemainder) + D24(self.hero_1.ConImpairment) + D24(self.hero_1.ConImpairmentRemainder)
            
            if self.hero_2.enemy_target == True:
                self.hero_2.enemy_target = False
                self.hero_2.HP = HP
                switch = False
            elif "hero_2" == self.target:
                self.hero_2.enemy_target = True
                HP = self.hero_2.HP
                Impairment = D24(self.hero_2.AgiImpairment) + D24(self.hero_2.AgiImpairmentRemainder) + D24(self.hero_2.ConImpairment) + D24(self.hero_2.ConImpairmentRemainder)
            
            if self.enemy_0.enemy_target == True:
                self.enemy_0.enemy_target = False
                self.enemy_0.HP = HP
                switch = False
            elif "enemy_0" == self.target:
                self.enemy_0.hero_target = True
                HP = self.enemy_0.HP
                Impairment = D24(self.enemy_0.AgiImpairment) + D24(self.enemy_0.AgiImpairmentRemainder) + D24(self.enemy_0.ConImpairment) + D24(self.enemy_0.ConImpairmentRemainder)
            
            if self.enemy_1.enemy_target == True:
                self.enemy_1.enemy_target = False
                self.enemy_1.HP = HP
                switch = False
            elif "enemy_1" == self.target:
                if self.enemy_1.move_unit == "no_unit":
                    pass
                else:
                    self.enemy_1.hero_target = True
                    HP = self.enemy_0.HP
                Impairment = D24(self.enemy_1.AgiImpairment) + D24(self.enemy_1.AgiImpairmentRemainder) + D24(self.enemy_1.ConImpairment) + D24(self.enemy_1.ConImpairmentRemainder)
            
            if self.enemy_2.enemy_target == True:
                self.enemy_2.enemy_target = False
                self.enemy_2.HP = HP
                switch = False
            elif "enemy_2" == self.target:
                if self.enemy_2.move_unit == "no_unit":
                    pass
                else:
                    self.enemy_2.hero_target = True
                    HP = self.enemy_0.HP
                Impairment = D24(self.enemy_2.AgiImpairment) + D24(self.enemy_2.AgiImpairmentRemainder) + D24(self.enemy_2.ConImpairment) + D24(self.enemy_2.ConImpairmentRemainder)
            
            if self.enemy_3.enemy_target == True:
                self.enemy_3.enemy_target = False
                self.enemy_3.HP = HP
                switch = False
            elif "enemy_3" == self.target:
                if self.enemy_3.move_unit == "no_unit":
                    pass
                else:
                    self.enemy_3.hero_target = True
                    HP = self.enemy_0.HP
                Impairment = D24(self.enemy_3.AgiImpairment) + D24(self.enemy_3.AgiImpairmentRemainder) + D24(self.enemy_3.ConImpairment) + D24(self.enemy_3.ConImpairmentRemainder)
            
            if self.enemy_4.enemy_target == True:
                self.enemy_4.enemy_target = False
                self.enemy_4.HP = HP
                switch = False
            elif "enemy_4" == self.target:
                if self.enemy_4.move_unit == "no_unit":
                    pass
                else:
                    self.enemy_4.hero_target = True
                    HP = self.enemy_0.HP
                Impairment = D24(self.enemy_4.AgiImpairment) + D24(self.enemy_4.AgiImpairmentRemainder) + D24(self.enemy_4.ConImpairment) + D24(self.enemy_4.ConImpairmentRemainder)
            
            def damage_data(Attack, Hit, HP, Impairment): # 將傷害計算所需要的數值打包成函式
                Attack
                Hit
                HP
                Impairment

            HP = damage_calculation(damage_data(Attack, Hit, HP, Impairment))