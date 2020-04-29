import pygame, random

pygame.init()


WIDTH = 640
HEIGHT = 480
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
rand_colors = []

# generate random colors
for x in range(15):
    rand_colors.append((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
display = pygame.display.set_mode((WIDTH, HEIGHT))
face = pygame.image.load("img/me.png")
razor = pygame.image.load("img/razor.png")

# music
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
bg_music = pygame.mixer.music.load("music/bg.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)


class MainGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.main()

    def main(self):
        loop = True
        component = Component()
        razor = Razor()
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            mouse_pos = pygame.mouse.get_pos()
            razor_pos = razor.get_pos()

            display.fill(white)
            component.draw()
            razor.draw()

            if razor_pos[0] < mouse_pos[0] < razor_pos[0]+20 and razor_pos[1] < mouse_pos[1] < razor_pos[1]+50:
                if pygame.mouse.get_pressed()[0]:
                    razor.set_pos(mouse_pos[0]-10, mouse_pos[1]-25)

            component.get_raz_pos(razor_pos)

            pygame.display.update()


class Razor:
    def __init__(self):
        self.x = 620
        self.y = 10
        self.width = 10
        self.height = 50

    def draw(self):
        display.blit(razor, (self.x, self.y))

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class Component:
    def __init__(self):
        self.width = 231
        self.height = 376
        self.x = int(WIDTH / 2) - int(self.width/2)
        self.y = 50
        self.hair = Hair()

    def draw(self):
        display.blit(face, (self.x, self.y))
        self.hair.draw()

    def get_raz_pos(self, razer_pos):
        self.hair.check(razer_pos)


class Hair:
    def __init__(self, color=black):
        self.width = 5
        self.height = 5
        self.hair_coord = []
        self.intensity = 500
        self.color = color
        # this for statements are too large need to compress them somehow, or make it better.
        for x in range(self.intensity+1000):
            rand_x = random.randint(281, 354)
            rand_y = random.randint(300, 424)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity):
            rand_x = random.randint(226, 280)
            rand_y = random.randint(300, 336)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(235, 280)
            rand_y = random.randint(337, 354)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(242, 280)
            rand_y = random.randint(354, 378)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(256, 280)
            rand_y = random.randint(378, 401)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-350):
            rand_x = random.randint(264, 280)
            rand_y = random.randint(400, 418)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity):
            rand_x = random.randint(354, 406)
            rand_y = random.randint(300, 336)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(354, 400)
            rand_y = random.randint(337, 354)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(354, 394)
            rand_y = random.randint(354, 378)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-250):
            rand_x = random.randint(354, 376)
            rand_y = random.randint(378, 401)
            self.hair_coord.append((rand_x, rand_y))
        for x in range(self.intensity-350):
            rand_x = random.randint(354, 363)
            rand_y = random.randint(400, 418)
            self.hair_coord.append((rand_x, rand_y))

    def draw(self):
        for x in self.hair_coord:
            pygame.draw.rect(display, self.color, (x[0], x[1], self.width, self.height))

    def check(self, razer_pos):
        x = razer_pos[0]
        y = razer_pos[1]
        for hair in self.hair_coord:
            if x+10 > hair[0] and x < hair[0]+self.width:
                if y+10 > hair[1] and y < hair[1]+self.height:
                    self.hair_coord.remove(hair)
        if len(self.hair_coord) <= 0:
            self.GameOver()

    def GameOver(self):
        self.__init__(random.choice(rand_colors))


MainGame(WIDTH, HEIGHT)
