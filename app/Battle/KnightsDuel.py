from app.Fighter.Knight import Knight


class KnightsDuel:

    @staticmethod
    def clash(unit1: Knight, unit2: Knight) -> None:
        unit1.hp -= unit2.power - unit1.protection
        unit2.hp -= unit1.power - unit2.protection

        if unit1.hp < 0:
            unit1.hp = 0

        if unit2.hp < 0:
            unit2.hp = 0
