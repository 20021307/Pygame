import pygame
import random
import time

pygame.init()

screen_width = 800
screen_height = 600

pygame.display.set_caption("Pong - Ping")
display = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

red = (255, 0, 0)
dark_red = (139, 0, 0)
green = (0, 255, 0)
dark_green = (0, 139, 50)
blue = (0, 0, 255)
dark_blue = (0, 0, 139)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
FPS = 60

small_font = pygame.font.Font("bold.ttf", 15)
med_font = pygame.font.Font("bold.ttf", 25)
big_font = pygame.font.Font("bold.ttf", 30)

control_game_w = 150
control_game_h = 30
p1_image = pygame.image.load("player_1_character.png")
p2_image = pygame.image.load("player_2_character.png")

difficulty = 0
config_exit = False
def draw_player(x, y, player):
    draw_this = " "
    if player == "player_1":
        draw_this = p1_image
    else:
        draw_this = p2_image
    display.blit(draw_this, [x, y])


def ball(x, y, color, rad):
    pygame.draw.circle(display, color, (int(x), y), rad)


def text_objects(text, color, size="small"):
    global textSurface
    if size == "small":
        textSurface = small_font.render(text, True, color)
    if size == "medium":
        textSurface = med_font.render(text, True, color)
    if size == "large":
        textSurface = big_font.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(screen_width / 2), int(screen_height / 2) + y_displace)
    display.blit(textSurf, textRect)


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    display.blit(textSurf, textRect)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    global difficulty, config_exit
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(display, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "play_single":
                MainScreenSinglePlayer()

            if action == "play_multi":
                MainScreen2Players()

            if action == "config":
                config_exit = False
                Configuration()

            if action == "change_dif":
                if difficulty == 3:
                    difficulty = 0
                else:
                    difficulty += 1
                time.sleep(0.7)
            if action == "config_exit":
                config_exit = True

            if action == "exit":
                pygame.quit()
                quit()


    else:
        pygame.draw.rect(display, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def MainScreen2Players():
    game = True
    p1_x = screen_width / 2 - control_game_w / 2
    p1_y = screen_height - control_game_h * 2
    p2_x = screen_width / 2 - control_game_w / 2
    p2_y = control_game_h
    ball_rad = 15
    ball_x = 393
    ball_y = 300
    ball_speed = 5

    gravity = False

    dp1_x = 0
    dp2_x = 0
    ball_move_x = 0
    ball_move_y = 0
    hit_counter = 0
    temp = 5

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dp1_x = -10
                elif event.key == pygame.K_RIGHT:
                    dp1_x = 10
                if event.key == pygame.K_a:
                    dp2_x = -10
                elif event.key == pygame.K_d:
                    dp2_x = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dp1_x = 0
                elif event.key == pygame.K_RIGHT:
                    dp1_x = 0
                if event.key == pygame.K_a:
                    dp2_x = 0
                elif event.key == pygame.K_d:
                    dp2_x = 0

        p1_x += dp1_x
        p2_x += dp2_x
        ball_y += ball_move_y
        ball_x += ball_move_x



        if p1_x > screen_width-control_game_w:
            p1_x = screen_width-control_game_w
        elif p1_x < 0:
            p1_x = 0

        if p2_x > screen_width-control_game_w:
            p2_x = screen_width-control_game_w
        elif p2_x < 0:
            p2_x = 0

        if gravity == False:
            ball_move_y = -ball_speed
        if gravity:
            ball_move_y = ball_speed

        if ball_y <= p2_y+15:
            hit_counter += 1
        elif ball_y >= p1_y-15:
            hit_counter += 1

        if hit_counter == 15:
            ball_speed = temp + 3
        elif hit_counter == 30:
            ball_speed = temp + 6
        elif hit_counter == 42:
            ball_speed = temp + 9

        if ball_x <= 15:
            ball_move_x = ball_speed
        elif ball_x >= screen_width-15:
            ball_move_x = -ball_speed
        if ball_y >= p1_y+15:
            gameOver("mp", "player 2")
        elif ball_y <= p2_y-15:
            gameOver("mp", "player 1")
        #Platform 1 if stat.
        if ball_x >= p1_x and ball_x < p1_x+control_game_w and ball_y >= p1_y-15:
            gravity = False
        if ball_x >= p1_x+75 and ball_x < p1_x+control_game_w and ball_y >= p1_y-15:
            gravity = False
            ball_move_x = ball_speed
        if ball_x >= p1_x and ball_x < p1_x+75 and ball_y >= p1_y-15:
            gravity = False
            ball_move_x = -ball_speed


        #Platform 2 if stat.
        if ball_x >= p2_x and ball_x < p2_x+control_game_w and ball_y <= p2_y+15*3:
            gravity = True
        if ball_x >= p2_x+75 and ball_x < p2_x+control_game_w and ball_y <= p2_y*2+15:
            gravity = True
            ball_move_x = ball_speed
        if ball_x >= p2_x and ball_x < p2_x+75 and ball_y <= p2_y*2+15:
            gravity = True
            ball_move_x = -ball_speed


        display.fill(white)

        message_to_screen("Made by StrozeR", black, 100, "large")
        ball(ball_x, ball_y, black, ball_rad)
        draw_player(p1_x, p1_y, "player_1")
        draw_player(p2_x, p2_y, "player_2")
        pygame.display.update()
        clock.tick(FPS)

def MainScreenSinglePlayer():
    game = True
    global difficulty
    p1_x = screen_width / 2 - control_game_w / 2
    p1_y = screen_height - control_game_h * 2
    p2_x = screen_width / 2 - control_game_w / 2
    p2_y = control_game_h
    ball_rad = 15
    ball_x = 393
    ball_y = 400
    ball_speed = 5
    hit_counter = 0

    gravity = False

    dp1_x = 0
    dp2_x = 0
    ball_move_x = 0
    ball_move_y = 0
    temp = 5

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dp1_x = -10
                elif event.key == pygame.K_RIGHT:
                    dp1_x = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dp1_x = 0
                elif event.key == pygame.K_RIGHT:
                    dp1_x = 0

        p1_x += dp1_x
        p2_x += dp2_x
        ball_y += ball_move_y
        ball_x += ball_move_x
        if difficulty == 0:
            if ball_y > random.randint(25, 75) and ball_x > 500:
                dp2_x = 4
            if ball_y > random.randint(25, 75) and ball_x < 250:
                dp2_x = -4
        elif difficulty == 1:
            if ball_y > random.randint(70, 150) and ball_x > 450:
                dp2_x = 5
            if ball_y > random.randint(70, 150) and ball_x < 300:
                dp2_x = -5
        elif difficulty == 2:
            if ball_y > random.randint(150, 300) and ball_x > 450:
                dp2_x = 5
            if ball_y > random.randint(150, 300) and ball_x < 350:
                dp2_x = -5
        elif difficulty == 3:
            p2_x = ball_x - control_game_w / 2

        if p1_x > screen_width-control_game_w:
            p1_x = screen_width-control_game_w
        elif p1_x < 0:
            p1_x = 0

        if p2_x > screen_width-control_game_w:
            p2_x = screen_width-control_game_w
        elif p2_x < 0:
            p2_x = 0

        if gravity == False:
            ball_move_y = -ball_speed
        if gravity:
            ball_move_y = ball_speed

        if ball_y <= p2_y+15:
            hit_counter += 1
        elif ball_y >= p1_y-15:
            hit_counter += 1

        if hit_counter == 15:
            ball_speed = temp + 3
        elif hit_counter == 30:
            ball_speed = temp + 6
        elif hit_counter == 42:
            ball_speed = temp + 9

        if ball_x <= 15:
            ball_move_x = ball_speed
        elif ball_x >= screen_width-15:
            ball_move_x = -ball_speed
        if ball_y >= p1_y+15:
            gameOver("sp", "player 2")
        elif ball_y <= p2_y-15:
            gameOver("sp", "player 1")
        #Platform 1 if stat.
        if ball_x >= p1_x and ball_x < p1_x+control_game_w and ball_y >= p1_y-15:
            gravity = False
        if ball_x >= p1_x+75 and ball_x < p1_x+control_game_w and ball_y >= p1_y-15:
            gravity = False
            ball_move_x = ball_speed
        if ball_x >= p1_x and ball_x < p1_x+75 and ball_y >= p1_y-15:
            gravity = False
            ball_move_x = -ball_speed


        #Platform 2 if stat.
        if ball_x >= p2_x and ball_x < p2_x+control_game_w and ball_y <= p2_y+15*3:
            gravity = True


        display.fill(white)

        message_to_screen("Made by StrozeR", black, 100, "large")
        ball(ball_x, ball_y, black, ball_rad)
        draw_player(p1_x, p1_y, "player_1")
        draw_player(p2_x, p2_y, "player_2")
        pygame.display.update()
        clock.tick(FPS)

def IntroScreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        display.fill(white)

        message_to_screen("Pong - Ping", red, -250, "large")
        message_to_screen("made by StrozeR", black, -220, "small")

        button("Play Singleplayer", 200, 250, 200, 75, dark_green, green, "play_single")
        button("Play Multiplayer", 200, 375, 200, 75, dark_blue, blue, "play_multi")
        button("Configuration", 450, 300, 150, 100, dark_red, red, "config")

        pygame.display.update()
        clock.tick(FPS)

def Configuration():
    config = True
    label = " "
    dif_color = black
    while config:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)

        message_to_screen("Configuration", black, -200, "large")

        button("Change Difficulty", 300, 200, 200, 65, dark_green, green, "change_dif")
        if difficulty == 0:
            label = "Beginner"
            dif_color = blue
        elif difficulty == 1:
            label = "Medium"
            dif_color = green
        elif difficulty == 2:
            label = "Hard"
            dif_color = orange
        elif difficulty == 3:
            label = "Impossible"
            dif_color = red
        message_to_screen(label, dif_color, 20, "medium")
        button("Back", 25, 25, 75, 50, dark_red, red, "config_exit")
        if config_exit == True:
            config = False
        pygame.display.update()
        clock.tick(FPS)

def gameOver(mode, winner):
    over = True
    string = " "
    if mode == "sp":
        string = "play_single"
    elif mode == "mp":
        string = "play_multi"
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(white)

        message_to_screen("Game Over! " + winner + " won", black, 0, "large")
        button("Play Again!", 150, 100, 150, 75, dark_green, green, string)
        button("Exit", 550, 100, 100, 75, dark_red, red, "exit")

        pygame.display.update()
        clock.tick(FPS)

IntroScreen()