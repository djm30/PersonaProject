from enum import Enum


class Element(Enum):
    """Enum containing all different types of elements

    Args:
        Enum (Enum): built in Python enumeration
    """
    PHYSICAL = "physical"
    GUN = "gun"
    FIRE = "fire"
    ICE = "ice"
    ELECTRIC = "electric"
    WIND = "wind"
    PSI = "psi"
    NUKE = "nuke"
    BLESS = "bless"
    CURSE = "curse"


class Resistance(Enum):
    """Enum containing different resistance levels and their respective damage multipliers

    Args:
        Enum (Enum): built in Python enumeration
    """
    Weak = 1.5
    Std = 1
    Strong = 0.75
    Null = 0.0


class ElementalResistance:
    def __init__(self, element: Element, resistance: Resistance):
        self.element = element
        self.resistance = resistance

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, element: Element):
        if element not in Element:
            raise Exception
        self._element = element

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, resistance: Resistance):
        if resistance not in Resistance:
            raise Exception
        self._resistance = resistance

    def __repr__(self):
        return f"Element: {self.element}\tResistance: {self.resistance}"


# Dictionary containing all types of elemental resistances for all strentghes
# Each key is an element to a list of ElementalResistance objects for each strength for that element
resistances = {e.value: [ElementalResistance(
    e, r) for r in Resistance] for e in Element}
