#戰鬥運算

def D24(DiceNumer):#D24系統，參數是分子，決定機率高低
    import random
    Dice = random.randint(1,24)#創造一顆1到24點的骰子
    
    #擲骰
    if Dice <= DiceNumer:
        result = True
    else:
        result = False

    return result

def MoveDice(V, RV, BV):#取得速度(行動)的隨機值
    MS = 0
    if V != 0:
        for cont in range(V):
            MS += D24(12)
    #low速度值擲骰
    if RV == 1:
        MS += D24(4)
    elif RV == 2:
        MS += D24(8) 
    
    MS += BV
    if MS > 0:
        MS = 100/MS
    MS = round(MS, 0)
    MS = int(MS)

    return MS

def Target():#隨機選擇對手
            import random
            target = random.randint(0, 2)
            return target

def Time(time, Move):#計時器
            while time != Move:
                time += 1
            return time

#戰鬥開始，代入敵我雙方戰鬥值。
def BattleStart():
    #前置作業，讀取雙方戰鬥值
    import json
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取所有單位資料資料，寫入char
    
    #前置作業，速度值處理
    #將速度值整理成行動列表(Dict格式)，準備載入序列。
    MoveSeq = {}
    MoveSeqB = {}
    MoveSeqR = {}
    for unit in ["Unit1", "Unit2", "Unit3"]:
        if unit == "Unit1":
            sn = 1
        elif unit == "Unit2":
            sn = 2
        elif unit == "Unit3":
            sn = 3
        
        MoveSeq["Hspp" + str(sn)] = char["Hero"][sn - 1][unit][1]["CombatVal"][3]["spp"]
        MoveSeqB["BHspp" + str(sn)] = char["Hero"][sn - 1][unit][1]["CombatVal"][4]["Bspp"]
        MoveSeqR["HsppR" + str(sn)] = char["Hero"][sn - 1][unit][1]["CombatVal"][5]["sppR"]
    Eunit = {}
    Eunit1 = {}
    Eunit2 = {}
    Eunit3 = {}
    Eunit4 = {}
    Eunit5 = {}
    Eunit1["Eunit1"] = char["Enemy"][0]["Unit1"]
    Eunit2["Eunit2"] = char["Enemy"][1]["Unit2"]
    Eunit3["Eunit3"] = char["Enemy"][2]["Unit3"]
    #Eunit4["Eunit4"] = char["Enemy"][3]["Unit4"]
    #Eunit5["Eunit5"] = char["Enemy"][4]["Unit5"]
    Eunit["Eunit"] = [Eunit1, Eunit2, Eunit3]#, Eunit4, Eunit5
    sn = 0
    for unit in [Eunit1, Eunit2, Eunit3, Eunit4, Eunit5]:
        if unit == Eunit4 or unit == Eunit5:
            break
        sn += 1
        for unitK in list(unit.keys()):
            MoveSeq["Espp" + str(sn)] = unit[unitK][4]["spp"]
            MoveSeqB["BEspp" + str(sn)] = unit[unitK][5]["Bspp"]

    #print(MoveSeqR)#測試
    #把基本速度值(Bspp)、速度值(spp)和low速度值(sppR)相加，得到最終速度值。
    MoveSeqF = {}
    MoveSeqF2 = {}
    for HorE in ["Hspp", "Espp"]:
        for sn in range(1, 4):
            if HorE == "Hspp":
                MSBK = "BHspp" + str(sn)
                MSK = "Hspp" + str(sn)
                MSRK = "HsppR" + str(sn)
                MSBV = MoveSeqB[MSBK]
                MSV = MoveSeq[MSK]
                MSRV = MoveSeqR[MSRK]
            elif HorE == "Espp":
                MSBK = "BEspp" + str(sn)
                MSK = "Espp" + str(sn)
                MSBV = MoveSeqB[MSBK]
                MSV = MoveSeq[MSK]
                MSRV = 0

            #速度值擲骰與加總
            MS = MoveDice(MSV, MSRV, MSBV)               
            MoveSeqF[HorE + str(sn)] = MS
            MoveSeqF2["B" + HorE + str(sn)] = MSBV
            MoveSeqF2[HorE + "R" + str(sn)] = MSRV
    
    #戰鬥開始
    time = 0
    BattleOver = False
    while BattleOver == False:
        #決定下一個行動單位
        #獲取現在行動單位的數據
        #將行動列表載入序列(元素是Tuple的List格式)
        MoveSeqTuple = sorted(list(MoveSeqF.items()), key = lambda item:item[1])
        MSmin = MoveSeqTuple[0]
        Move = MSmin[1]
        MSminK = MSmin[0]
        Time(time, Move)#計時器

        #取出最先開始行動的鍵值，#決定下一個行動單位。
        #依照最先行動的鍵值來代入戰鬥單位的數據
        CombatUnitVal = {}
        if "H" == MSminK[0]:
            sn = int(MSminK[4])
            CombatUnitVal["seq"] = "CombatHero" + str(sn)
            CombatUnitVal["name"] = char["Hero"][sn - 1]["Unit" + str(sn)][0]["Ability"][0]["name"] 
            CombatUnitVal["HP"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][0]["HP"]
            CombatUnitVal["att"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][1]["att"]
            CombatUnitVal["attR"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][2]["attR"]
            CombatUnitVal["hit"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][6]["Fhit"]
            CombatUnitVal["AhitR"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][7]["AhitR"]
            CombatUnitVal["IhitR"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][8]["IhitR"]
            CombatUnitVal["dodgeDO"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][9]["dodgeDO"]
            CombatUnitVal["dodgeDOR"] = char["Hero"][sn - 1]["Unit" + str(sn)][1]["CombatVal"][10]["dodgeDOR"]
            #計算我方現在行動單位的下次行動值
            MS = MoveDice(MSmin[1], MoveSeqF2["HsppR" + MSminK[4]], MoveSeqF2["BHspp" + MSminK[4]]) 

        elif "E" == MSminK[0]:
            sn = int(MSminK[4])
            CombatUnitVal["seq"] = "CombatEnemy" + str(sn)
            CombatUnitVal["name"] = Eunit["Eunit"][sn - 1]["Eunit" + str(sn)][0]["name"]
            CombatUnitVal["HP"] = Eunit["Eunit"][sn - 1]["Eunit" + str(sn)][2]["HP"] 
            CombatUnitVal["att"] = Eunit["Eunit"][sn - 1]["Eunit" + str(sn)][3]["att"] 
            CombatUnitVal["hit"] = Eunit["Eunit"][sn - 1]["Eunit" + str(sn)][6]["hit"] 
            CombatUnitVal["dodgeDO"] = Eunit["Eunit"][sn - 1]["Eunit" + str(sn)][7]["dodgeDO"] 
            #計算敵人現在行動單位的下次行動值
            MS = MoveDice(MSmin[1], MoveSeqF2["EsppR" + MSminK[4]], MoveSeqF2["BEspp" + MSminK[4]])
        #將下次行動值與現在行動值相加後放入排序
        MS = Move + MS
        MoveSeqF[MSminK] = MS

        #開始互動
        sn = Target()#隨機選擇對手
        DDO = 0
        if "H" == MSminK[0]:
            HP = Eunit["Eunit"][sn]["Eunit" + str(sn + 1)][2]["HP"]
            dodgeDO = Eunit["Eunit"][sn]["Eunit" + str(sn + 1)][7]["dodgeDO"]
            for n in range(dodgeDO):
                DDO += D24(12)
            attR = D24(CombatUnitVal["attR"])
            hitR = D24(CombatUnitVal["AhitR"]) + D24(CombatUnitVal["IhitR"])
        elif "E" == MSminK[0]:
            HP = CombatUnitVal["HP"] = char["Hero"][sn]["Unit" + str(sn + 1)][1]["CombatVal"][0]["HP"]
            dodgeDO = char["Hero"][sn]["Unit" + str(sn + 1)][1]["CombatVal"][9]["dodgeDO"]
            for n in range(dodgeDO):
                DDO += D24(12)
            dodgeDOR = char["Hero"][sn]["Unit" + str(sn + 1)][1]["CombatVal"][10]["dodgeDOR"]
            DDO += D24(dodgeDOR)
            attR = 0
            hitR = 0
        Fhit = CombatUnitVal["hit"] + hitR
        
        FDO = DDO - Fhit
        if FDO <= 0:#消除減傷的負數
            FDO = 0
        HP -= CombatUnitVal["att"] + attR - FDO

        if "H" == MSminK[0]:
            Eunit["Eunit"][sn]["Eunit" + str(sn + 1)][2]["HP"] = HP #把本回合攻擊目標剩餘血量寫回去
            #回合結束前判斷敵人是否全死亡
            if 0 >= Eunit["Eunit"][0]["Eunit1"][2]["HP"]:
                if 0 >= Eunit["Eunit"][1]["Eunit2"][2]["HP"]:
                    if 0 >= Eunit["Eunit"][2]["Eunit3"][2]["HP"]:
                        BattleOver = True
                        print("Hero win!")
        elif "E" == MSminK[0]:
            char["Hero"][sn]["Unit" + str(sn + 1)][1]["CombatVal"][0]["HP"] = HP #把本回合攻擊目標剩餘血量寫回去
            #回合結束前判斷英雄們是否全死亡
            if 0 >= char["Hero"][0]["Unit1"][1]["CombatVal"][0]["HP"]:
                if 0 >= char["Hero"][1]["Unit2"][1]["CombatVal"][0]["HP"]:
                    if 0 >= char["Hero"][2]["Unit3"][1]["CombatVal"][0]["HP"]:
                        BattleOver = True
                        print("Enemy win!")
    return
