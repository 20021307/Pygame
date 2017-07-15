import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Reaction Game")

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dred = (139, 0, 0)
dgreen = (0, 139, 0)
dblue = (0, 0, 139)
white = (255, 255, 255)
black = (0, 0, 0)

#fonts
small_font = pygame.font.Font("bold.ttf", 15)
med_font = pygame.font.Font("bold.ttf", 25)
big_font = pygame.font.Font("bold.ttf", 35)
ex_small_font = pygame.font.Font("bold.ttf", 13)

#global booleans
instruct = False
pause = False

#sounds
missed_sound = pygame.mixer.Sound("missed.wav")
succes_sound = pygame.mixer.Sound("success.wav")

def text_objects(text, color, size="small"):
    global textSurface
    if size == "small":
        textSurface = small_font.render(text, True, color)
    if size == "medium":
        textSurface = med_font.render(text, True, color)
    if size == "large":
        textSurface = big_font.render(text, True, color)
    if size == "ex_small":
        textSurface = ex_small_font.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(WIDTH / 2), int(HEIGHT / 2) + y_displace)
    screen.blit(textSurf, textRect)


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    global difficulty, instruct, pause
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "play":
                MainGame()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "instructions":
                instruct = True
                Instructions()
            if action == "instruct_exit":
                instruct = False
            if action == "resume":
                pause = False
            if action == "menu":
                IntroScreen()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def IntroScreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            screen.fill(white)

            message_to_screen("Reaction Game", black, -200, "large")

            button("Play", 100, 250, 100, 75, dgreen, green, "play")
            button("Instructions", 325, 250, 150, 75, dblue, blue, "instructions")
            button("Exit", WIDTH-200, 250, 100, 75, dred, red, "quit")
            message_to_screen("made by 20021307 / Strozer", black, -150)

            pygame.display.update()
            clock.tick(FPS)


def drawBlock(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))


def drawBlocks(x, y, width, height):
    pygame.draw.rect(screen, red, (x, y-40, width, height))


def MainGame():
    global pause
    game = True
    firstBlock_w = 225
    firstBlock_h = 40
    firstBlock_x = WIDTH / 2 - firstBlock_w / 2
    firstBlock_y = 525
    block_w = 225
    block_h = 40
    changing_block_x = WIDTH / 2 - firstBlock_w / 2
    changing_block_y = 525
    changing_block_dx = 0
    move_right = True
    speed = 5
    score = 0
    tries = 5

    while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if changing_block_x >= firstBlock_x-15 and changing_block_x+block_w <= firstBlock_x+block_w+15:
                            firstBlock_h += 40
                            firstBlock_y -= 40
                            changing_block_y -= 40
                            speed += 1
                            score += 1
                            pygame.mixer.Sound.play(succes_sound)
                            time.sleep(0.5)
                        else:
                            tries -= 1
                            pygame.mixer.Sound.play(missed_sound)
                            time.sleep(0.5)
                    if event.key == pygame.K_ESCAPE:
                        pause = True
                        Pause()
            changing_block_x += changing_block_dx

            screen.fill(white)

            if changing_block_x+firstBlock_w > WIDTH:
                move_right = False
            elif changing_block_x < 0:
                move_right = True

            if move_right:
                changing_block_dx = speed
            elif not move_right:
                changing_block_dx = -speed

            if score%13 == 0:
                firstBlock_h = 40
                firstBlock_y = 525
                changing_block_y = 525
                tries = 5

            if tries == 0:
                gameOver(score)

            if tries <= 2:
                tries_color = red
            else:
                tries_color = black

            drawBlock(firstBlock_x, firstBlock_y, firstBlock_w, firstBlock_h, black)
            drawBlocks(changing_block_x, changing_block_y, block_w, block_h)
            score_label = med_font.render("Score: " + str(score), 1, black)
            tries_label = med_font.render("Tries left: " + str(tries), 1, tries_color)
            screen.blit(tries_label, [WIDTH-225, 75])
            screen.blit(score_label, [25, 75])
            pygame.display.update()
            clock.tick(FPS)


def gameOver(score):
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        message_to_screen("Game Over!", black, -200, "large")
        message_to_screen("Your score: " + str(score), red, -100, "medium")

        button("Try Again", 110, 300, 110, 75, dgreen, green, "play")
        button("Menu", 335, 300, 110, 75, dblue, blue, "menu")
        button("Exit", WIDTH-210, 300, 110, 75, dred, red, "quit")

        pygame.display.update()

def Instructions():
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        message_to_screen("Instructions", blue, -200, "large")
        button("Menu", 25, 25, 50, 50, dred, red, "instruct_exit")
        message_to_screen("The platform goes from the right to the left and vice versa.", black, -100)
        message_to_screen("Using the spacebar try to center the platform to the block that is in the middle.", black, -50, "ex_small")
        message_to_screen("The left label is your score, while the right represents your tries.", black)
        message_to_screen("The objective is to stack the block the highest you can.", black, 50)
        message_to_screen("Each successful placement the speed gets faster.", black, 100)
        message_to_screen("Press ESC key to pause the game.", black, 150)


        pygame.display.update()

def Pause():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)

        message_to_screen("Paused", green, -200, "large")
        button("Resume", 350, 250, 100, 75, dgreen, green, "resume")

        pygame.display.update()


IntroScreen()