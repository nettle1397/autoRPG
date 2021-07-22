#角色的數值
def character(SerialNumber, DataKey_SerialNumber, DataKey, value):
    import json
    #讀取資料
    with open('database/CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取charT資料，寫入char
    
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][DataKey_SerialNumber][DataKey] = value

    with open('database/CharacterData.json', mode = 'w', encoding = 'utf-8') as charT:
        json.dump(char, charT, indent = 2, ensure_ascii = False)#把char的資料寫入charT

#載入能力值，將能力值轉換成戰鬥數值。
def ChangeChardata(SerialNumber):
    import json
    with open('database/CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取資料，寫入char

    #取出能力值
    HP= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][2]["HP"]
    stre= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][3]["stre"]
    agi= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][4]["agi"]
    inte= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][5]["inte"]
    wis= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][6]["wis"]
    con= char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][0]["Ability"][7]["con"]

    #計算戰鬥值   
    #閃避減傷值為減少對方攻擊力，命中值為減少對方閃避減傷值。所有機率用1顆24面骰來運作(D24系統)。
    Attack = stre // 2 #將力量轉換為攻擊力，每點為一點傷害(damage)。
    AttackRemainder = stre % 2 #攻擊力的餘數為可能損失的部分(low攻擊力)，餘1為1顆1/2(12/24)的dice，
                    #骰成功增加1點攻擊力。
    Speed = agi // 3  #將敏捷轉換成速度值，每1點速度值表示1顆機率為1/2(12/24)的dice。
    BasicSpeed = round(agi / 3, 1) #基本速度值，為固定值不須擲骰。
                                #包含小數點後一位。(為了降低角色速度值重複的機率。)
    SpeedRemainder = agi % 3 #速度值的餘數為更低機率的速度值(low速度值)，餘1為1顆1/6(4/24)的dice，
                    #餘2為1顆1/3(8/24)的dice。
    AgiHit = agi // 4 #將敏捷轉換為敏捷命中值，每1點命中值表示1顆機率為1/2(12/24)的dice。
    AgiHitRemainder = agi % 4 #敏捷命中值的餘數為更低機率的命中值(low敏捷命中值)，
                    #餘1為1顆1/8(3/24)的dice，餘2為1顆1/4(6/24)的dice，
                    #餘3為1顆3/8(9/24)的dice。
    AgiImpairment = agi // 3 #將敏捷轉換為敏捷閃避減傷值，每1點減傷值表示1顆機率為1/2(12/24)的dice。
    AgiImpairmentRemainder = agi % 3 #敏捷閃避減傷值的餘數為更低機率的閃避減傷值(low閃避減傷值)，
                        #餘1為1顆1/6(4/24)的dice，餘2為1顆1/3(8/24)的dice。
    InteHit = inte // 6 #將智力轉換成智力命中值，每1點命中值表示1顆機率為1/2(12/24)的dice。
    InteHitRemainder = inte % 6 #智力命中值的餘數為更低機率的命中(low智力命中值)，
                        #餘1為1顆1/12(2/24)的dice，餘2為1顆1/6(4/24)的dice，
                        # 餘3為1顆1/4(6/24)的dice，餘4為1顆1/3(8/24)的dice，
                        # 餘5為1顆5/12(10/24)的dice。
    ConImpairment = con // 3 #將體質轉換為體質防禦減傷值，每1點減傷值表示1顆機率為1/2(12/24)的dice。
    ConImpairmentRemainder = con % 3 #體質防禦減傷值的餘數為更低機率的防禦減傷值(low防禦減傷值)，
                        #餘1為1顆1/6(4/24)的dice，餘2為1顆1/3(8/24)的dice。

    #將戰鬥值寫入char
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][0]["HP"] = HP
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][1]["Attack"] = Attack
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][2]["AttackRemainder"] = AttackRemainder
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][3]["Speed"] = Speed
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][4]["BasicSpeed"] = BasicSpeed
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][5]["SpeedRemainder"] = SpeedRemainder
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][6]["FinalHit"] = AgiHit + InteHit
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][7]["AgiHitRemainder"] = AgiHitRemainder
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][8]["InteHitRemainder"] = InteHitRemainder
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][9]["AgiImpairment"] = AgiImpairment
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][10]["AgiImpairmentRemainder"] = AgiImpairmentRemainder
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][11]["ConImpairment"] =ConImpairment
    char["Hero"][SerialNumber]["Unit" + str(SerialNumber)][1]["CombatVal"][12]["ConImpairmentRemainder"] =ConImpairmentRemainder

    with open('database/CharacterData.json', mode = 'w', encoding = 'utf-8') as charT:
        json.dump(char, charT, indent = 2, ensure_ascii = False)#把char的資料寫入charT
