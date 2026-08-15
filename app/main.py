from app.Fighter.Knight import Knight
from app.Battle.KnightsDuel import KnightsDuel


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}


def battle(knights_config: dict) -> dict:

    lancelot = Knight(
        name=knights_config.get("lancelot").get("name"),
        power=knights_config.get("lancelot").get("power"),
        hp=knights_config.get("lancelot").get("hp"),
        armours=knights_config.get("lancelot").get("armour"),
        weapon=knights_config.get("lancelot").get("weapon"),
        potion=knights_config.get("lancelot").get("potion")
    )

    lancelot.use_armour()
    lancelot.use_weapon()
    lancelot.use_potions()

    arthur = Knight(
        name=knights_config.get("arthur").get("name"),
        power=knights_config.get("arthur").get("power"),
        hp=knights_config.get("arthur").get("hp"),
        armours=knights_config.get("arthur").get("armour"),
        weapon=knights_config.get("arthur").get("weapon"),
        potion=knights_config.get("arthur").get("potion")
    )

    arthur.use_armour()
    arthur.use_weapon()
    arthur.use_potions()

    mordred = Knight(
        name=knights_config.get("mordred").get("name"),
        power=knights_config.get("mordred").get("power"),
        hp=knights_config.get("mordred").get("hp"),
        armours=knights_config.get("mordred").get("armour"),
        weapon=knights_config.get("mordred").get("weapon"),
        potion=knights_config.get("mordred").get("potion")
    )

    mordred.use_armour()
    mordred.use_weapon()
    mordred.use_potions()

    red_knight = Knight(
        name=knights_config.get("red_knight").get("name"),
        power=knights_config.get("red_knight").get("power"),
        hp=knights_config.get("red_knight").get("hp"),
        armours=knights_config.get("red_knight").get("armour"),
        weapon=knights_config.get("red_knight").get("weapon"),
        potion=knights_config.get("red_knight").get("potion")
    )

    red_knight.use_armour()
    red_knight.use_weapon()
    red_knight.use_potions()

    KnightsDuel.clash(lancelot, mordred)
    KnightsDuel.clash(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
