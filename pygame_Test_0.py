import sys
sys.path.append("database")
sys.path.append("GUI")
sys.path.append("Battle")

import database.Control as DC

DC.character(0, 0, "name", "Hero01")
DC.character(0, 3, "stre", 9)
DC.character(0, 4, "agi", 6)
DC.character(0, 5, "inte", 6)
DC.character(0, 6, "wis", 6)
DC.character(0, 7, "con", 8)

DC.character(1, 0, "name", "Hero02")
DC.character(1, 3, "stre", 6)
DC.character(1, 4, "agi", 9)
DC.character(1, 5, "inte", 8)
DC.character(1, 6, "wis", 6)
DC.character(1, 7, "con", 6)

DC.character(2, 0, "name", "Hero01")
DC.character(2, 3, "stre", 7)
DC.character(2, 4, "agi", 7)
DC.character(2, 5, "inte", 7)
DC.character(2, 6, "wis", 7)
DC.character(2, 7, "con", 7)

DC.ChangeChardata(0)
DC.ChangeChardata(1)
DC.ChangeChardata(2)