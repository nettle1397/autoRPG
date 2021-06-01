#角色的資料讀取、運算及寫入。
import json

#角色的數值
def character(sn, val):
    #讀取資料
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取charT資料，寫入char
    
    char[sn] = val

    with open('database\CharacterData.json', mode = 'w', encoding = 'utf-8') as charT:
        json.dump(char, charT)#把char的資料寫入charT
    
    return 

#載入能力值，將能力值轉換成戰鬥數值。
def ChangeChardata():
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取資料，寫入char
    
        #製造英雄序號
    for sn in range(1, 4):
        sn = str(sn)

        #取出能力值
        HP = char["con" + sn]
        name = char["name" + sn]
        stre = char["stre" + sn]
        agi = char["agi" + sn]
        inte = char["inte" + sn]

        #計算戰鬥值   
        #閃避減傷值為減少對方攻擊力，命中值為減少對方閃避減傷值。所有機率用1顆24面骰來運作(D24系統)。
        att = stre // 2 #將力量轉換為攻擊力，每點為一點傷害(damage)。
        attR = stre % 2 #攻擊力的餘數為可能損失的部分(low攻擊力)，餘1為1顆1/2(12/24)的dice，骰成功增加1點攻擊力。
        spp = agi // 3  #將敏捷轉換成速度值，每1點速度值表示1顆機率為1/2(12/24)的dice。
        Bspp = agi / 3 #基本速度值，為固定值不須擲骰，包含小數。
        sppR = agi % 3 #速度值的餘數為更低機率的速度值(low速度值)，餘1為1顆1/6(4/24)的dice，餘2為1顆1/3(8/24)的dice。
        Ahit = agi // 4 #將敏捷轉換為敏捷命中值，每1點命中值表示1顆機率為1/2(12/24)的dice。
        AhitR = agi % 4 #敏捷命中值的餘數為更低機率的命中值(low敏捷命中值)，餘1為1顆1/8(3/24)的dice，餘2為1顆1/4(6/24)的dice，餘3為1顆3/8(9/24)的dice。
        dodgeDO = agi // 2 #將敏捷轉換為閃避減傷值，每1點閃避值表示1顆機率為1/2(12/24)的dice。
        dodgeDOR = agi % 2 #閃避減傷值的餘數為更低機率的閃避減傷值(low閃避減傷值)，餘1為1顆1/4(6/24)的dice。
        Ihit = inte // 6 #將智力轉換成智力命中值，每1點命中值表示1顆機率為1/2(12/24)的dice。
        IhitR = inte % 6 #智力命中值的餘數為更低機率的命中(low智力命中值)，餘1為1顆1/12(2/24)的dice，餘2為1顆1/6(4/24)的dice，餘3為1顆1/4(6/24)的dice，餘4為1顆1/3(8/24)的dice，餘5為1顆5/12(10/24)的dice。

        #將戰鬥值寫入char
        char["HP" + sn] = HP
        char["att" + sn] = att
        char["attR" + sn] = attR
        char["spp" + sn] = spp
        char["Bspp" + sn] = Bspp
        char["sppR" + sn] = sppR
        char["Fhit" + sn] = Ahit + Ihit
        char["AhitR" + sn] = AhitR
        char["IhitR" + sn] = IhitR
        char["dodgeDO" + sn] = dodgeDO
        char["dodgeDOR" + sn] = dodgeDOR

        with open('database\CharacterData.json', mode = 'w', encoding = 'utf-8') as charT:
            json.dump(char, charT)#把char的資料寫入charT
    
    return

