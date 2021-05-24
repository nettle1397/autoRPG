#角色的數值[名字, 力量, 敏捷, 智力]

#角色1的數值
def character01(sn, val):
    import json
    #讀取資料
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取資料寫入char
    
    char[sn] = val

    with open('database\CharacterData.json', mode = 'w', encoding = 'utf-8') as charT:
        json.dump(char, charT)
    
    return 

