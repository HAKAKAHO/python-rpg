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
    "weapon": sword,
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
    "ai_state": "idle",
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

