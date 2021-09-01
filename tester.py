from elements import resistances, Element
import persona as p
from skills import Skill

r_list = []

for element in resistances:
    r_list.append(resistances[element][1])

Agi = Skill("Agi", 11, 64, Element.FIRE, True)
Karmen = p.Persona("karmen", 180, 63, False, r_list, [Agi])

print(Karmen)
