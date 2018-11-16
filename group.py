# ws5xa
# rel7dqj

"""

Our project was inspired by Space Invaders. The key to progressing
score and levels is by collecting coins and avoiding the enemies.
The following characteristics of our game will meet the four
required criteria

Enemies: many enemies will be introduced in an infinite scrolling
feature. The enemies will be randomized in size and location. If
the sprite contacts an enemy, it will push it towards the bottom
of the screen. If the sprite gets to the bottom of the screen, the
game will end.

Collectibles: Coins will randomly appear for the sprite to collect
Once a certain amount of coins are gathered, the sprite can progress
to the next level.

Timer: A timer will countdown until it wither gets to the end, or the
sprite progresses to the next level

Multiple levels: The sprite can progress through multiple levels.

"""
changes i made


import pygame
import gamebox
import random

WIDTH_WINDOW = 800
HEIGHT_WINDOW = 600
camera = gamebox.Camera(WIDTH_WINDOW, HEIGHT_WINDOW)  # size of window
character = gamebox.from_color(camera.x, camera.y, "green", 30, 30)
speed = 20  # higher number, faster gamebox moves
# Enable only one of the following four BOUNDS_ACTIONs
BOUNDS_ACTION = "wrap"                            # If set to wrap exit one side, enter opposite side


direction_x = 1  # flip flops between 1 & -1 determining direction
direction_y = 1

coins = [gamebox.from_color(300, 450, "yellow", 12, 12)]
time = 9000
score = 0




# character.yspeed = 0
# Create a list of walls
walls = [
    gamebox.from_color(50, 250, "black", 20, 20),
    gamebox.from_color(150, 150, "black", 20, 20),
    gamebox.from_color(300, 25, "black", 20, 20),
    gamebox.from_color(450, 150, "black", 20, 20),
    gamebox.from_color(600, 25, "black", 20, 20),
    gamebox.from_color(750, 25, "black", 20, 20),
]
counter = 0

def tick(keys):
    global direction_x
    global direction_y
    global speed
    global counter
    global HEIGHT_WINDOW
    global time
    global score

    # decrease timer per call of tick
    time -= 1

    # calculate timer
    seconds = str(int((time / ticks_per_second))).zfill(3)



    # Use pygame key definitions to detect user keyboard input.  Parameter keys can
    # have more than one key.
    # if the decision statements below are converted into if elif, only one key is
    # detected each tick, even though multiple keys are pressed
    if pygame.K_RIGHT in keys:
        character.x += speed * direction_x  # add constant value to .x moves at constant speed
    if pygame.K_LEFT in keys:
        character.x -= speed * direction_x  # same for subtract
    if pygame.K_UP in keys:
        character.y -= speed * direction_y  # same for y
    if pygame.K_DOWN in keys:
        character.y += speed * direction_y

    if BOUNDS_ACTION == "wrap":
        # Determine bounds contact and if so, wrap
        if character.x >= WIDTH_WINDOW:
            character.x = 0                     # wrap
        elif character.x < 0:
            character.x = WIDTH_WINDOW

    camera.clear("red")

    camera.draw(character)
    # character.yspeed += 1  # character accelerated falling if not riding platform, character is global
    # character.y = character.y + character.yspeed
    #     # makes the screen scroll adding negative to camera makes camera move up,
        # whole scene appears to move down

    camera.y -= 7
    HEIGHT_WINDOW += 5

    # make random walls appear every time the counter hits a particular number
    # notice how I use the random.randint to vary the width of the platform
    # also I add in the camera.y to the y position because the screen keeps moving

    counter += 1

    if counter % 20 == 0:
        new_wall = gamebox.from_color(random.randint(0, 150), - 300,
                                      "black", random.randint(30, 50), 30)
        walls.append(new_wall)  # wall list continues to grow
        new_wall = gamebox.from_color(random.randint(150, 300), camera.y - 300,
                                      "black", random.randint(30, 50), 30)
        walls.append(new_wall)  # wall list continues to grow
        new_wall = gamebox.from_color(random.randint(300, 400), camera.y - 300,
                                      "black", random.randint(30, 50), 30)
        walls.append(new_wall)  # wall list continues to grow
        new_wall = gamebox.from_color(random.randint(400, 600), camera.y - 300,
                                      "black", random.randint(30, 50), 30)
        walls.append(new_wall)  # wall list continues to grow
        new_wall = gamebox.from_color(random.randint(500, 800), camera.y - 300,
                                      "black", random.randint(30, 50), 30)
        walls.append(new_wall)  # wall list continues to grow

    if time % 10 == 0:
        coin_x = gamebox.from_color(random.randint(0, 800), camera.y - 300, "yellow", 12, 12)
        coins.append(coin_x)
        coin_y = gamebox.from_color(random.randint(0, 800), camera.y - 300, "yellow", 12, 12)
        coins.append(coin_y)



    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -20  # change yspeed accelerates
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)

    # write timer and score to screen
    time_box = gamebox.from_text(650, camera.top + 30, "Time Remaining: " + seconds,  24, "black")
    score_box = gamebox.from_text(75, camera.top + 30, "Score: " + str(score),  24, "black")
    camera.draw(time_box)
    camera.draw(score_box)



    camera.display()

    if character.y == camera.bottom:
        exit()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
