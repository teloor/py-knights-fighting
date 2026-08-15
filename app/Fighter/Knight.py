from app.Fighter.armour import Armour
from app.Fighter.potion import Potion
from app.Fighter.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armours: list,
                 weapon: dict,
                 potion: dict
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp

        self.protection = 0

        self.armours = []

        for piece in armours:
            self.armours.append(Armour(name=piece.get("name"),
                                       protection=piece.get("protection")
                                       ))
        self.weapon = Weapon(weapon)

        self.potions = None
        if potion:
            self.potions = Potion(name=potion.get("name"),
                                  effect=potion.get("effect"))

    def use_armour(self) -> None:
        for piece in self.armours:
            self.protection += piece.protection

    def use_potions(self) -> None:
        if self.potions:
            hp = self.potions.effect.get("hp")
            power = self.potions.effect.get("power")
            protection = self.potions.effect.get("protection")

            if hp:
                self.hp += hp

            if power:
                self.power += power

            if protection:
                self.protection += protection

    def use_weapon(self) -> None:
        self.power += self.weapon.power
