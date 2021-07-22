# import sys
# sys.path.append("database")

import json
with open('database/CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
    char = json.load(charT)
unit= {}
for unit0 in char["Hero"]:
    unit.update(unit0)
print("unit", unit)

unit1= type(unit)
print("unit1", unit1)

unit2= unit.keys()
print("unit2", unit2)
for key_ in unit2:
    unit3= key_
    print("unit3", unit3)