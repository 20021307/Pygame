import pygame, sys, random

pygame.init()

WIDTH = 500
HEIGHT = 500

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity project")

FPS = 60
clock = pygame.time.Clock()
#newton = f = m * a


class MainWindow(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.Main()

    def Main(self):
        loop = True

        b1 = Ball(2, blue)

        while loop:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

            b1.draw()

            pygame.display.update()
            clock.tick(FPS)


class Ball(object):
    def __init__(self, accell, color):
        self.prad = 4
        self.x = int((WIDTH / 3) + self.prad / 2)
        self.y = int((HEIGHT / 3) - self.prad / 2)
        self.mass = 0.1
        self.accell = accell
        self.color = color
        self.pdy = 0
        self.pdx = 0

    def draw(self):
        pos = self.laws()

        pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (int(pos[0]), int(pos[1])), self.prad)

    def laws(self):
        self.x += self.pdx
        self.y += self.pdy

        if self.y + int(self.prad / 2) >= 250:
            self.pdy -= self.accell * self.mass
        else:
            self.pdy += self.accell * self.mass

        if self.x + int(self.prad / 2) >= 250:
            self.pdx -= self.accell * self.mass
        else:
            self.pdx += self.accell * self.mass

        return self.x, self.y


MainWindow(WIDTH, HEIGHT)


