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
    MS = 100/MS
    MS = round(MS, 0)
    MS = int(MS)

    return MS

def Target():#隨機選擇對手
            import random
            target = random.randint(1, 3)
            return target

def Time(time, Move):#計時器
            while time != Move:
                time += 1
            print("Move",Move)
            return time

#戰鬥開始，代入敵我雙方戰鬥值。
def BattleStart():
    #前置作業，讀取雙方戰鬥值
    import json
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        Hero = json.load(charT) #讀取我方英雄資料，寫入Hero
    
    with open('database\MonsterData.json', mode = 'r', encoding = 'utf-8') as MonsT:
        Enemy = json.load(MonsT) #讀取敵方怪物資料，寫入Enemy

    #前置作業，速度值處理
    #將速度值整理成行動列表(Dict格式)，準備載入序列。
    MoveSeq = {}
    MoveSeqB = {}
    MoveSeqR = {}
    for sn in range(1, 4):
        sn = str(sn)
        MoveSeq["Hspp" + sn] = Hero["spp" + sn]
        MoveSeqB["BHspp" + sn] = Hero["Bspp" + sn]
        MoveSeqR["HsppR" + sn] = Hero["sppR" + sn]
        MoveSeq["Espp" + sn] = Enemy["spp" + sn]
        MoveSeqB["BEspp" + sn] = Enemy["Bspp" + sn]

    #print(MoveSeqR)#測試
    #把基本速度值(Bspp)、速度值(spp)和low速度值(sppR)相加，得到最終速度值。
    MoveSeqF = {}
    MoveSeqF2 = {}
    for HorE in ["Hspp", "Espp"]:
        for sn in range(1, 4):
            sn = str(sn)
            if HorE == "Hspp":
                MSBK = "BHspp" + sn
                MSK = "Hspp" + sn
                MSRK = "HsppR" + sn
                MSBV = MoveSeqB[MSBK]
                MSV = MoveSeq[MSK]
                MSRV = MoveSeqR[MSRK]
            elif HorE == "Espp":
                MSBK = "BEspp" + sn
                MSK = "Espp" + sn
                MSBV = MoveSeqB[MSBK]
                MSV = MoveSeq[MSK]
                MSRV = 0

            #速度值擲骰與加總
            MS = MoveDice(MSV, MSRV, MSBV)               
            MoveSeqF[HorE + sn] = MS
            MoveSeqF2["B" + HorE + sn] = MSBV
            MoveSeqF2[HorE + "R" + sn] = MSRV
    
    #戰鬥開始
    time = 0
    BattleOver = False
    while BattleOver == False:
        #決定下一個行動單位
        #獲取現在行動單位的數據
        #將行動列表載入序列(元素是Tuple的List格式)
        MoveSeqTuple = sorted(MoveSeqF.items(), key = lambda item:item[1])

        MSmin = MoveSeqTuple[0]
        Move = MSmin[1]
        MSminK = MSmin[0]
        Time(time, Move)#計時器

        #取出最先開始行動的鍵值，#決定下一個行動單位。
        #依照最先行動的鍵值來代入戰鬥單位的數據
        CombatUnitVal = {}
        if "H" == MSminK[0]:
            CombatUnitVal["seq"] = "H" + MSminK[4]
            CombatUnitVal["name"] = Hero["name" + MSminK[4]] 
            CombatUnitVal["HP"] = Hero["HP" + MSminK[4]] 
            CombatUnitVal["att"] = Hero["att" + MSminK[4]]
            CombatUnitVal["attR"] = Hero["attR" + MSminK[4]] 
            CombatUnitVal["hit"] = Hero["Fhit" + MSminK[4]] 
            CombatUnitVal["AhitR"] = Hero["AhitR" + MSminK[4]] 
            CombatUnitVal["IhitR"] = Hero["IhitR" + MSminK[4]] 
            CombatUnitVal["dodgeDO"] = Hero["dodgeDO" + MSminK[4]]
            CombatUnitVal["dodgeDOR"] = Hero["dodgeDOR" + MSminK[4]]
            #計算我方現在行動單位的下次行動值
            MS = MoveDice(MSmin[1], MoveSeqF2["HsppR" + MSminK[4]], MoveSeqF2["BHspp" + MSminK[4]]) 

        elif "E" == MSminK[0]:
            CombatUnitVal["seq"] = "E" + MSminK[4]
            CombatUnitVal["name"] = Enemy["name" + MSminK[4]] 
            CombatUnitVal["HP"] = Enemy["HP" + MSminK[4]] 
            CombatUnitVal["att"] = Enemy["att" + MSminK[4]] 
            CombatUnitVal["hit"] = Enemy["hit" + MSminK[4]] 
            CombatUnitVal["dodgeDO"] = Enemy["dodgeDO" + MSminK[4]] 
            #計算敵人現在行動單位的下次行動值
            MS = MoveDice(MSmin[1], MoveSeqF2["EsppR" + MSminK[4]], MoveSeqF2["BEspp" + MSminK[4]])
        #將下次行動值與現在行動值相加後放入排序
        MS = Move + MS
        MoveSeqF[MSminK] = MS

        #開始互動
        sn = Target()#隨機選擇對手
        sn = str(sn)
        DDO = 0
        if "H" == MSminK[0]:
            HP = Enemy["HP" + sn]
            dodgeDO = Enemy["dodgeDO" + sn]
            for n in range(dodgeDO):
                DDO += D24(12)
            attR = D24(CombatUnitVal["attR"])
            hitR = D24(CombatUnitVal["AhitR"]) + D24(CombatUnitVal["IhitR"])
        elif "E" == MSminK[0]:
            HP = Hero["HP" + sn]
            dodgeDO = Hero["dodgeDO" + sn]
            for n in range(dodgeDO):
                DDO += D24(12)
            dodgeDOR = Hero["dodgeDOR" + sn]
            DDO += D24(dodgeDOR)
            attR = 0
            hitR = 0
        Fhit = CombatUnitVal["hit"] + hitR
        
        FDO = DDO - Fhit
        if FDO <= 0:#消除減傷的負數
            FDO = 0
        HP -= CombatUnitVal["att"] + attR - FDO

        if "H" == MSminK[0]:
            Enemy["HP" + sn] = HP
            if 0 >= Enemy["HP1"]:
                if 0 >= Enemy["HP2"]:
                    if 0 >= Enemy["HP3"]:
                        BattleOver = True
                        print("Hero win!")
        elif "E" == MSminK[0]:
            Hero["HP" + sn] = HP
            if 0 >= Hero["HP1"]:
                if 0 >= Hero["HP2"]:
                    if 0 >= Hero["HP3"]:
                        BattleOver = True
                        print("Enemy win!")
    return