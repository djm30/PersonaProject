from persona import Persona
from skills import Skill
from elements import Element, resistances

Cleave = Skill("Cleave", 20, 30, Element.PHYSICAL, False)
Snap = Skill("Snap", 22, 30, Element.GUN, False)

Agi = Skill("Agi", 4, 24, Element.FIRE, False)
Bufu = Skill("Bufu", 4, 24, Element.ICE, False)
Garu = Skill("Garu", 6, 24, Element.WIND, False)
Zio = Skill("Zio", 4, 24, Element.ELECTRIC, False)

# 0 : Weak  1 : Std  2 : Strong  3 : Null

"""
Pixie,
Jack Frost,
Jack O' Lantern,
Zorro

"""

personas = {}

JackLantern = Persona("JackLantern", 140.0, 24.0,
                      [resistances["physical"][1],
                       resistances["gun"][1],
                          resistances["fire"][3],
                          resistances["ice"][0],
                          resistances["wind"][0],
                          resistances["electric"][1],
                          resistances["nuke"][1],
                          resistances["psi"][1],
                          resistances["bless"][1],
                          resistances["curse"][1]],
                      [Agi])


Pixie = Persona("Pixie", 140.0, 24.0,
                [resistances["physical"][1],
                 resistances["gun"][0],
                 resistances["fire"][1],
                 resistances["ice"][0],
                 resistances["wind"][1],
                 resistances["electric"][2],
                 resistances["nuke"][1],
                 resistances["psi"][1],
                 resistances["bless"][2],
                 resistances["curse"][0]],
                [Zio])

JackFrost = Persona("Jack Frost", 140.0, 24.0,
                    [resistances["physical"][1],
                     resistances["gun"][1],
                     resistances["fire"][0],
                     resistances["ice"][3],
                     resistances["wind"][1],
                     resistances["electric"][1],
                     resistances["nuke"][1],
                     resistances["psi"][1],
                     resistances["bless"][1],
                     resistances["curse"][1]],
                    [Bufu])

Zorro = Persona("Zorro", 140.0, 24.0,
                [resistances["physical"][1],
                 resistances["gun"][1],
                 resistances["fire"][1],
                 resistances["ice"][1],
                 resistances["wind"][2],
                 resistances["electric"][0],
                 resistances["nuke"][1],
                 resistances["psi"][1],
                 resistances["bless"][1],
                 resistances["curse"][1]],
                [Garu])


personas[JackFrost.name] = JackFrost
personas[JackLantern.name] = JackLantern
personas[Pixie.name] = Pixie
personas[Zorro.name] = Zorro

if __name__ == '__main__':
    print(personas)
