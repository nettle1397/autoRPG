#載入創建人物選單的模組
import database.Character as charT
#取名字
def name(sn):
    name = input('請輸入英雄名稱： ')
    charT.character01(sn, name)
    return name

#設定能力值
def Ability(sn):
    #判斷要輸入的能力值
    AP = "no"
    while AP == "no":
        if sn == "stre01" or sn == "stre02" or sn == "stre03": 
            AP = input('請輸入力量（6~12）： ')
        if sn == "agi01" or sn == "agi02" or sn == "agi03": 
            AP = input('請輸入敏捷（6~12）： ')
        elif sn == "inte01" or sn == "inte02" or sn == "inte03": 
            AP = input('請輸入智力（6~12）： ')
        AP = int(AP)

        #判斷輸入值是否在範圍內
        APmin = 6
        APmax = 12
        if AP < APmin:
            print('數值低於6')
            AP = "no"
        elif AP > APmax:
            print('數值高於12')
            AP = "no"

    charT.character01(sn, AP) #寫入能力值

    return AP

#設定人物的表單
def CreatCharacter():
    #第一位
    print("創造第一位英雄")

    print("第一位英雄的名字是：" + name("name01"))

    print("第一位英雄的力量是：" + str(Ability("stre01")))

    #agi = "agi01"
    print("第一位英雄的敏捷是：" + str(Ability("agi01")))

    inte = "inte01"
    print("第一位英雄的智力是：" + str(Ability(inte)))

    print("創造第二位英雄")

    sn = "name02"
    print("第二位英雄的名字是：" + name(sn))

    sn = "stre02"
    print("第二位英雄的力量是：" + str(Ability(sn)))

    sn = "agi02"
    print("第二位英雄的敏捷是：" + str(Ability(sn)))

    sn = "inte02"
    print("第二位英雄的智力是：" + str(Ability(sn)))

    #第二位
    print("創造第三位英雄")

    sn = "name03"
    print("第三位英雄的名字是：" + name(sn))

    sn = "stre03"
    print("第三位英雄的力量是：" + str(Ability(sn)))

    sn = "agi03"
    print("第三位英雄的敏捷是：" + str(Ability(sn)))

    sn = "inte03"
    print("第三位英雄的智力是：" + str(Ability(sn)))

    return