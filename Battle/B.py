import json
def speed(SerialNumber, unit):
    with open('database\CharacterData.json', mode = 'r', encoding = 'utf-8') as charT:
        char = json.load(charT) #讀取所有單位資料資料，寫入char

        MoveSequence = {}
        MoveSequenceBasic = {}
        MoveSequenceRemainder = {}

        MoveSequence["HeroSpeed" + str(SerialNumber)] = char["Hero"][SerialNumber][unit][1]["CombatVal"][3]["Speed"]
        MoveSequenceBasic["BasicHerospeed" + str(SerialNumber)] = char["Hero"][SerialNumber][unit][1]["CombatVal"][4]["BasicSpeed"]
        MoveSequenceRemainder["HeroSpeedRemainder" + str(SerialNumber)] = char["Hero"][SerialNumber][unit][1]["CombatVal"][5]["SpeedRemainder"]

        