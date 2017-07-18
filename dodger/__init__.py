import pygame
import random

pygame.init()

WIDHT = 800
HEIGHT = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Dodger")

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dred = (139, 0, 0)
dgreen = (0, 139, 0)
dblue = (0, 0, 139)

# --
FPS = 60

small_font = pygame.font.Font("bold.ttf", 15)
med_font = pygame.font.Font("bold.ttf", 25)
big_font = pygame.font.Font("bold.ttf", 30)


# message_to_screen & text_objects
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
    textRect.center = (int(WIDHT / 2), int(HEIGHT / 2) + y_displace)
    screen.blit(textSurf, textRect)


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    screen.blit(textSurf, textRect)


class MainWindow(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def Main(self):
        loop = True

        # Player
        sprites = Sprites()
        pdx = 0
        pdy = 0
        speed = 5

        # Flying Blocks fb - flying block

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pdx -= speed
                    if event.key == pygame.K_RIGHT:
                        pdx += speed

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        pdx = 0
                    if event.key == pygame.K_RIGHT:
                        pdx = 0

            screen.fill(white)

            sprites.draw_blocks()
            sprites.draw_player()
            sprites.move_blocks()
            sprites.move_player(pdx, pdy)
            sprites.check_if_blocks()
            sprites.check_if_player()

            pygame.display.update()
            clock.tick(FPS)

    def introScreen(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            screen.fill(white)

            message_to_screen("Dodger", red, -200, "large")
            button("Play", 200, 200, 100, 75, dgreen, green, "play")
            button("Quit", WIDHT - 300, 200, 100, 75, dred, red, "quit")

            pygame.display.update()

    def gameOver(self):
        over = True
        while over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.rect(screen, white, (286, 84, 250, 40))
            message_to_screen("Game Over!", red, -200, "large")
            button("Quit", WIDHT / 2 - 50, HEIGHT / 2 + 40, 100, 80, dred, red, "quit")

            pygame.display.update()


class Sprites(object):
    # p
    p_w = 70
    p_h = 50
    p_x = WIDHT / 2 - p_w / 2
    p_y = HEIGHT - p_h * 2
    p_speed = 5
    p_color = red
    # fb
    fb_w = random.randint(160, 250)
    fb_h = random.randint(50, 150)
    fb_x = random.randint(0, WIDHT)
    fb_y = random.randint(-150, 0)
    fb_speed = 7
    fb_color = blue

    def __init__(self):
        self.p_x = Sprites.p_x
        self.p_y = Sprites.p_y
        self.p_w = Sprites.p_w
        self.p_h = Sprites.p_h
        self.p_speed = Sprites.p_speed
        self.p_color = red

        self.fb_x = Sprites.fb_x
        self.fb_y = Sprites.fb_y
        self.fb_w = Sprites.fb_w
        self.fb_h = Sprites.fb_h
        self.fb_speed = Sprites.fb_speed
        self.fb_color = blue

    def draw_player(self):
        pygame.draw.rect(screen, self.p_color, (self.p_x, self.p_y, self.p_w, self.p_h))

    def draw_blocks(self):
        pygame.draw.rect(screen, self.fb_color, (self.fb_x, self.fb_y, self.fb_w, self.fb_h))

    def move_player(self, dx, dy):
        self.p_x += dx
        self.p_y += dy

    def move_blocks(self):
        self.fb_y += self.fb_speed

    def check_if_player(self):
        if self.p_x < 0:
            self.p_x = 0
        elif self.p_x + self.p_w > WIDHT:
            self.p_x = WIDHT - self.p_w

        if self.p_x + self.p_w >= self.fb_x and self.p_x <= self.fb_x + self.fb_w:
            if self.fb_y + self.fb_h >= self.p_y and self.fb_y <= self.p_y+self.p_h:
                game.gameOver()

    def check_if_blocks(self):
        if self.fb_y > HEIGHT + self.p_w:
            self.fb_y = random.randint(-150, 0)
            self.fb_w = random.randint(160, 250)
            self.fb_h = random.randint(50, 150)
            self.fb_x = random.randint(0, WIDHT - 250)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "play":
                game.Main()
            if action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


game = MainWindow(WIDHT, HEIGHT)

game.introScreen()
