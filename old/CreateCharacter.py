#載入創建人物選單的模組
import database.Control as cont
#取名字
def name(sn):
    name = input("請輸入英雄名稱： ")
    cont.character(sn, 0, "name", name)
    return name

#設定能力值
def Ability(sn, DataKey):
    #判斷要輸入的能力值
    AP = "no"
    while AP == "no":
        if DataKey == "stre": 
            AP = input('請輸入力量（6~9）： ')
            dksn = 3
        if DataKey == "agi": 
            AP = input('請輸入敏捷（6~9）： ')
            dksn = 4
        elif DataKey == "inte": 
            AP = input('請輸入智力（6~9）： ')
            dksn = 5
        AP = int(AP)

        #判斷輸入值是否在範圍內
        APmin = 6
        APmax = 9
        int_ = int(1)
        if AP < APmin:
            print("數值低於6")
            AP = "no"
        elif AP > APmax:
            print("數值高於9")
            AP = "no"
        elif type(AP) != type(int_):
            print("請輸入數值6~9")
            AP = "no"

    cont.character(sn , dksn, DataKey, AP) #寫入能力值

    return AP

#設定人物的表單
def CreatCharacter():
    #第一位
    print("創造第一位英雄")
    print("第一位英雄的名字是：" + name(1))
    avaAP = 3
    print("第一位英雄目前有",avaAP,"點可以加點")
    print("第一位英雄的力量是：" + str(Ability(1, "stre")))
    print("第一位英雄的敏捷是：" + str(Ability(1, "agi")))
    print("第一位英雄的智力是：" + str(Ability(1, "inte")))

    print("創造第二位英雄")
    print("第二位英雄的名字是：" + name(2))
    print("第二位英雄的力量是：" + str(Ability(2, "stre")))
    print("第二位英雄的敏捷是：" + str(Ability(2, "agi")))
    print("第二位英雄的智力是：" + str(Ability(2, "inte")))

    #第三位
    print("創造第三位英雄")
    print("第三位英雄的名字是：" + name(3))
    print("第三位英雄的力量是：" + str(Ability(3, "stre")))
    print("第三位英雄的敏捷是：" + str(Ability(3, "agi")))
    print("第三位英雄的智力是：" + str(Ability(3, "inte")))

    return