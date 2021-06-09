'''
a = 10
b = 11
if type(a) == class('int'):
    print("y")
    print(type(a))
    print(type(b))
else:
    print("n")
'''
import json
with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
    char = json.load(charT) #讀取charT資料，寫入char

'''
print(char["Hero"][0]["Unit1"][0]["Ability"][2]["con"])
print(type(char["Hero"][0]["Unit1"][0]["Ability"][2]["con"]))

sn = 1
sn = int(sn)
print(type(sn))
print(type("sn"))
print(sn + 1)


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
print(Eunit)
'''


import random
target = random.randint(0, 3)
print(target)