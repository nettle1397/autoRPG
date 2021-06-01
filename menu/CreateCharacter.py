#載入創建人物選單的模組
import database.Control as cont
#取名字
def name(sn):
    name = input('請輸入英雄名稱： ')
    cont.character(sn, name)
    return name

#設定能力值
def Ability(sn):
    #判斷要輸入的能力值
    AP = "no"
    while AP == "no":
        if sn == "stre1" or sn == "stre2" or sn == "stre3": 
            AP = input('請輸入力量（6~9）： ')
        if sn == "agi1" or sn == "agi2" or sn == "agi3": 
            AP = input('請輸入敏捷（6~9）： ')
        elif sn == "inte1" or sn == "inte2" or sn == "inte3": 
            AP = input('請輸入智力（6~9）： ')
        AP = int(AP)

        #判斷輸入值是否在範圍內
        APmin = 6
        APmax = 9
        if AP < APmin:
            print('數值低於6')
            AP = "no"
        elif AP > APmax:
            print('數值高於9')
            AP = "no"

    cont.character(sn, AP) #寫入能力值

    return AP

#設定人物的表單
def CreatCharacter():
    #第一位
    print("創造第一位英雄")
    print("第一位英雄的名字是：" + name("name1"))
    print("第一位英雄的力量是：" + str(Ability("stre1")))
    print("第一位英雄的敏捷是：" + str(Ability("agi1")))
    print("第一位英雄的智力是：" + str(Ability("inte1")))

    print("創造第二位英雄")
    print("第二位英雄的名字是：" + name("name2"))
    print("第二位英雄的力量是：" + str(Ability("stre2")))
    print("第二位英雄的敏捷是：" + str(Ability("agi2")))
    print("第二位英雄的智力是：" + str(Ability("inte2")))

    #第三位
    print("創造第三位英雄")
    print("第三位英雄的名字是：" + name("name3"))
    print("第三位英雄的力量是：" + str(Ability("stre3")))
    print("第三位英雄的敏捷是：" + str(Ability("agi3")))
    print("第三位英雄的智力是：" + str(Ability("inte3")))

    return