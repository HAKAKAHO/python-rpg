import pygame
import dicts
from dicts import player, stick, imp

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("My RPG")

running = True
screen_height = 450
screen_width = 800
normal_speed = 200
shift_speed = 400
gravity = 1200
ground_y = screen_height - player["height"]


def chek_distance(attacker, defender):
    distance = abs(attacker["x"] - defender["x"])
    return distance

def deal_damage(character, damage):
    character["hp"] -= damage
    if character["hp"] <= 0:
        character["hp"] = 0
        character["alive"] = False

def movement(keys, player, dt):
    if keys[pygame.K_LSHIFT] and player["run"] == False:
        player["speed"] = shift_speed
        player["run"] = True
    elif not keys[pygame.K_LSHIFT]:
        player["run"] = False
        player["speed"] = normal_speed
    if keys[pygame.K_SPACE] and player["jump"] == True:
        player["jump_speed"] = -500
        player["state"] = "air"
        player["jump"] = False
    if keys[pygame.K_d] and player["x"] < screen_width - player["width"]:
        player["x"] += player["speed"] * dt
        player["direction"] = "right"
        if player["state"] != "air":
            player["state"] = "move"
    if keys[pygame.K_a] and player["x"] > screen_width - screen_width:
        player["x"] -= player["speed"] * dt
        player["direction"] = "left"
        if player["state"] != "air":
            player["state"] = "move"
    if not keys[pygame.K_d] and not keys[pygame.K_a] and player["state"] != "air":
        player["state"] = "idle"

def gravitation(player, gravity, dt):
    player["y"] += player["jump_speed"] * dt
    player["jump_speed"] += gravity * dt
    if player["y"] >= ground_y:
        player["jump_speed"] = 0
        player["y"] = ground_y
        player["jump"] = True
        if player["state"] != "move":
            player["state"] = "idle"

def draw_character(screen, character):
    draw_width = character["width"]
    draw_x = character["x"]
    draw_y = character["y"]
    draw_height = character["height"]
    if character["character_type"] == "player":
        if character["state"] == "air":
            draw_height = character["height"] + (character["height"] / 4)
            draw_width = draw_width - (draw_width / 6)
            draw_y = draw_y - (character["height"] / 4)
            draw_x = (character["x"] + character["width"] / 2) - (draw_width / 2)
        if character["direction"] == "left" and character["state"] == "move":
            color = (40, 220,44)
        elif character["direction"] == "right" and character["state"] == "move":
            color = (0, 150,255)
        elif character["state"] == "air":
            color = (200, 50, 55)
        else:
            color = (0, 150, 0)
    else:
        color = (255, 0, 0)
    if not character["alive"]:
        draw_y = screen_height - character["width"]
        draw_width = character["height"]
        draw_height = character["width"]
        color = (20, 20, 20)
    pygame.draw.rect(
        screen,
        color,
        (draw_x, draw_y, draw_width, draw_height)
    )

def draw_hp(screen, character):
    if character["hp"] < character["max_hp"] / 2:
        color = (200, 0, 0)
    elif character["hp"] < character["max_hp"] * 0.75:
        color = (200, 200, 0)
    elif character["hp"] >= character["max_hp"] * 0.75:
        color = (0, 200, 0)
    hp_percent = character["hp"] / character["max_hp"]
    hp_height = 5
    hp_width = character["width"] / 1.5
    hp_x = (character["x"] + character["width"] / 2) - (hp_width / 2)
    hp_y = character["y"] - hp_height * 5
    pygame.draw.rect(
        screen,
        (20, 20, 20),
        (hp_x, hp_y, hp_width, hp_height)
    )
    pygame.draw.rect(
        screen,
        color,
        (hp_x, hp_y, hp_width * hp_percent, hp_height)
    )

def draw_enemy(screen, enemy):
    draw_width = enemy["width"]
    draw_x = enemy["x"]
    draw_y = enemy["y"]
    draw_height = enemy["height"]
    color = (255, 0, 0)
    if enemy["alive"] == False:
        draw_y = screen_height - enemy["width"]
        draw_width = enemy["height"]
        draw_height = enemy["width"]
        color = (20, 20, 20)
    pygame.draw.rect(
        screen,
        color,
        (draw_x, draw_y, draw_width, draw_height)
    )


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if chek_distance(player, imp) <= 80 and player["attack_cooldown"] <= 0:
                    deal_damage(imp, player["weapon"]["damage"])
                    player["attack_cooldown"] = 0.5

    keys = pygame.key.get_pressed()

    movement(keys, player, dt)

    gravitation(player, gravity, dt)

    screen.fill((30, 30, 30))

    draw_character(screen, player)
    draw_character(screen, imp)

    draw_hp(screen, player)
    draw_hp(screen, imp)
    if player["attack_cooldown"] > 0:
        player["attack_cooldown"] -= dt
        print(player["attack_cooldown"], end = "\r")
    if player["attack_cooldown"] < 0:
        player["attack_cooldown"] = 0

    pygame.display.update()

pygame.quit()
#получение урона атака блок