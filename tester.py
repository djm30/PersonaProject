from elements import resistances, Element
import persona as p
from skills import Skill

r_list = []

for element in resistances:
    r_list.append(resistances[element][1])

Agi = Skill("Agi", 11, 64, Element.FIRE, True)
Karmen = p.Persona("karmen", 180, 63, False, r_list, [Agi])

print(Karmen)

Fucker = p.Persona("Fucker", 160, 20, False, r_list, [Agi])
Fucker.resistances[2] = resistances["fire"][0]
print(Fucker)

p.damage_model(Agi, [Fucker])


print(Fucker)
