def distance_to_player(character, distance):
    if distance <= 80:
        character["ai_state"] = "attacking"
    elif distance <= 200:
        character["ai_state"] = "chasing"
    else:
        character["ai_state"] = "idle"
        character["state"] = "idle"


def ai_chasing(character, player, dt):
    distance = (character["x"] + character["width"] / 2) - (player["x"] + player["width"] / 2)
    if character["alive"]:
        if character["ai_state"] == "chasing":
            if distance < 0:
                character["x"] += character["speed"] * dt
                character["direction"] = "right"
                if character["state"] != "air":
                    character["state"] = "move"
            if distance > 0:
                character["x"] -= character["speed"] * dt
                character["direction"] = "left"
                if character["state"] != "air":
                    character["state"] = "move"

def ai_attacking(character, player, calculate_damage, deal_damage):
    if character["alive"]:
        if character["ai_state"] == "attacking" and character["attack_cooldown"] <= 0:
            damage = calculate_damage(character, player)
            deal_damage(player, damage)
            character["attack_cooldown"] = 0.75