stick = {
    "name": "Палка",
    "damage": 5,
}

sword = {
    "name": "Меч",
    "damage": 10,
    "bonus_against": "hell",
    "bonus_damage": 5
}

player = {
    "run": False,
    "jump": True,
    "jump_speed": 0,
    "width": 50,
    "height": 80,
    "x": 100,
    "y": 370,
    "speed": 200,
    "state": "idle",
    "direction": "right",
    "name": "George",
    "character_type": "player",
    "hp": 100,
    "max_hp": 100,
    "weapon": stick,
    "blocking": False,
    "attack_cooldown": 0.5,
    "alive": True
}

imp = {
    "run": False,
    "jump": True,
    "jump_speed": 0,
    "width": 50,
    "height": 80,
    "x": 400,
    "y": 370,
    "speed": 200,
    "state": "idle",
    "direction": "right",
    "name": "Imp",
    "character_type": "hell",
    "hp": 50,
    "max_hp": 50,
    "damage": 5,
    "blocking": False,
    "attack_cooldown": 0.5,
    "alive": True
}

wolf = {
    "name": "Wolf",
    "enemy_type": "beast",
    "hp": 50,
    "max_hp": 50,
    "damage": 5,
    "blocking": False
}

def show_character(character):
    title = "=" * 3 + character["name"] + "=" * 3
    print(title)
    if "weapon" in character:
        weapon = character["weapon"]
        print("Здоровье:", character["hp"], "/", character["max_hp"])
        print("Оружие:", weapon["name"])
        print("Урон:", weapon["damage"])
    else:
        print("Здоровье:", character["hp"], "/", character["max_hp"])
        print("Урон:", character["damage"])
    print("=" * (len(title)))

def print_result(attacker, defender, damage):
    print("=" * 7, "Атака", "=" * 7)
    print(attacker["name"], "атаковал", defender["name"])
    print("нанесено:", damage, "урона")
    print("здоровье", defender["name"], ":", defender["hp"], "/", defender["max_hp"])
    print("=" * 21)

def block(character):
    if input() == "1":
        character["blocking"] = True

def calculate_damage(attacker, defender):
    if "weapon" in attacker:
        weapon = attacker["weapon"]
        if "bonus_against" in weapon and "bonus_damage" in weapon:
            bonus_against = weapon["bonus_against"]
            enemy_type = defender["enemy_type"]
            if bonus_against == enemy_type:
                damage = weapon["damage"] + weapon["bonus_damage"]
            else:
                damage = weapon["damage"]
        else:
            damage = weapon["damage"]
    else:
        damage = attacker["damage"]
    return damage

def attack(attacker, defender):
    damage = calculate_damage(attacker, defender)
    defender["hp"] -= damage
    if defender["hp"] < 0:
        defender["hp"] = 0
    print_result(attacker, defender, damage)

def battle(attacker, defender):
    while attacker["hp"] > 0 and defender["hp"] > 0:
        attack(attacker, defender)
        if defender["hp"] > 0:
            attack(defender, attacker)
    if attacker["hp"] <= 0:
        print("=" * 2, defender["name"], "Победил в битве!", "=" * 2)
        show_character(defender)
    if defender["hp"] <= 0:
        print("=" * 2, attacker["name"], "Победил в битве!", "=" * 2)
        show_character(attacker)