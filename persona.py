from elements import Element, resistances, ElementalResistance
from skills import Skill


class Persona:

    """Class representing a Persona
    name [string] : Persona name
    hp [float] : Persona hit points
    sp [float] : Persona stamina points
    guard [boolean] : Represents whether persona is currently guarding
    resistances [list : ElementResistance] : a list of all the resistances of a persona
    skills [list : Skill] : A list of all the skills of a persona
    """

    def __init__(self, name, hp, sp, guard, resistances, skills):
        self.name = name
        self.hp = hp
        self.sp = sp
        self.guard = guard
        self.resistances = resistances
        self.skills = skills

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def sp(self):
        return self._sp

    @sp.setter
    def sp(self, sp):
        self._sp = sp

    @property
    def guard(self):
        return self._guard

    @guard.setter
    def guard(self, guard):
        self._guard = guard

    @property
    def guard(self):
        return self._guard

    @guard.setter
    def guard(self, guard):
        self._guard = guard

    @property
    def resistances(self):
        return self._resistances

    @resistances.setter
    def resistances(self,  resistances):
        self._resistances = resistances

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self,  skills):
        self._skills = skills

    def __repr__(self):
        s = f"""
Name: {self.name}
HP: {self.hp}\t SP: {self.sp}
        """
        for skill in self._skills:
            s += "\t" + str(skill) + "\n"
        return s


def damage_model(skill, personas):
    """Caluclates damage done to a persona based on a skill that is attacking its

    Args:
        skill (Skill): skill that is being used to attack
        persona (list : Persona): persona that is being attacked
    """
    damages = []
    for persona in personas:
        damage = skill.damage
        for resistance in persona.resistances:
            if skill.element == resistance.element:
                damage *= resistance.resistance.value
                damages.append((damage, resistance.resistance))
        persona.hp(persona.hp - damage)
