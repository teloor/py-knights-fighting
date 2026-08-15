from app.Fighter.armour import Armour
from app.Fighter.potion import Potion
from app.Fighter.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp

        self.protection = 0

        self.armour = []

        for piece in armour:
            self.armour.append(Armour(name=piece.get("name"),
                                      protection=piece.get("protection")
                                      ))
        self.weapon = Weapon(weapon)

        self.potion = None
        if potion:
            self.potion = Potion(name=potion.get("name"),
                                 effect=potion.get("effect"))

    def use_armour(self) -> None:
        for piece in self.armour:
            self.protection += piece.protection

    def use_potion(self) -> None:
        if self.potion:
            hp = self.potion.effect.get("hp")
            power = self.potion.effect.get("power")
            protection = self.potion.effect.get("protection")

            if hp is not None:
                self.hp += hp

            if power is not None:
                self.power += power

            if protection is not None:
                self.protection += protection

    def use_weapon(self) -> None:
        self.power += self.weapon.power

    def ready_up(self) -> None:
        self.use_armour()
        self.use_weapon()
        self.use_potion()
