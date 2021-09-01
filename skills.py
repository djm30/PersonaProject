from elements import Element


class Skill:

    def __init__(self, name, cost, damage, element: Element, multi_target):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.element = element
        self.multi_target = multi_target

    # No need for getters and setters, will not be changing after initializtion

    def __repr__(self):
        s = ""
        s += f"Name: {self.name}\n"
        s += f"Cost: {self.cost} \t Damage: {self.damage}\n"
        s += f"Element: {self.element.value}\t Muli Target: {self.multi_target}"
        return s
