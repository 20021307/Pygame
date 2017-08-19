import pygame
import random

pygame.init()

WIDTH = 200
HEIGHT = 150
SCALE = 4

screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
clock = pygame.time.Clock()


# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# fps
FPS = 60

# images
space_ship = pygame.image.load("res/space_ship.png")
enemy_ship = pygame.image.load("res/enemy_ship.png")
background = pygame.image.load("res/background.png")
bullet_img = pygame.image.load("res/bullet.png")


class MainWindow(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.Main()

    def Main(self):
        global space_ship_new_coord, bullet_x, bullet_new_coord, enemy_ship_new_coord, bullet_length, bullet_new_array
        loop = True

        ship_width = 50
        ship_height = 50
        space_ship_x = (WIDTH*SCALE) / 2 + 25
        space_ship_y = (HEIGHT*SCALE) - 100

        space_ship_dx = 0
        space_ship_dy = 0
        space_ship_mov_speed = 4
        space_ship = SpaceShip(space_ship_x, space_ship_y, ship_width, ship_height)

        bullet_dy = -4
        bullet_width = 25
        bullet_height = 25
        bullet = Bullets(bullet_width, bullet_height)

        first_ship_coord = [100, 10]
        enemy_ships = 6
        enemy_killed = 0
        enemy_ship = EnemyShip(10, 10, ship_width, ship_width, enemy_ships, first_ship_coord, enemy_killed)
        enemy_ship_mov_speed = 0.5

        bullet_array = []
        enemy_ship.addShip()
        bullet_new_array = []
        bullet_lenght = 0

        while loop:
            cur_fps = int(clock.get_fps())
            pygame.display.set_caption("Space Game 0.1 -- StrozeR " + str(cur_fps) + " FPS")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        space_ship_dx -= space_ship_mov_speed
                    elif event.key == pygame.K_RIGHT:
                        space_ship_dx += space_ship_mov_speed
                    elif event.key == pygame.K_UP:
                        space_ship_y -= space_ship_mov_speed
                    elif event.key == pygame.K_DOWN:
                        space_ship_y += space_ship_mov_speed
                    elif event.key == pygame.K_SPACE:
                        bullet_array = bullet.addBullet(int(space_ship_new_coord[0]), int(space_ship_new_coord[1]))
                        bullet_lenght = len(bullet_array)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        space_ship_dx = 0
                    elif event.key == pygame.K_RIGHT:
                        space_ship_dx = 0
                    elif event.key == pygame.K_UP:
                        space_ship_dy = 0
                    elif event.key == pygame.K_DOWN:
                        space_ship_dy = 0

            # main loop
            screen.blit(background, [0, 0])

            space_ship.draw()
            space_ship_new_coord = space_ship.move(space_ship_dx, space_ship_dy)

            bullet.draw()
            bullet.move(bullet_dy)

            enemy_ship_array = enemy_ship.move(enemy_ship_mov_speed)
            enemy_ship.draw()

            if enemy_ships > 6:
                enemy_ship = 6

            try:
                if enemy_ships >= 1:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[0][0]-25 < bullet_array[x][0] < enemy_ship_array[0][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[0][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[0] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]

            except:
                pass

            try:
                if enemy_ships >= 2:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[1][0]-25 < bullet_array[x][0] < enemy_ship_array[1][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[1][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[1] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]

            except:
                pass

            try:
                if enemy_ships >= 3:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[2][0]-25 < bullet_array[x][0] < enemy_ship_array[2][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[2][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[2] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]

            except:
                pass

            try:
                if enemy_ships >= 4:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[3][0]-25 < bullet_array[x][0] < enemy_ship_array[3][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[3][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[3] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]
            except:
                pass

            try:
                if enemy_ships >= 5:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[4][0]-25 < bullet_array[x][0] < enemy_ship_array[4][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[4][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[4] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]
            except:
                pass

            try:
                if enemy_ships >= 6:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[5][0]-25 < bullet_array[x][0] < enemy_ship_array[5][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[5][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[5] = [random.randint(0, WIDTH*SCALE-ship_width), random.randint(-100, 0)]

            except:
                pass

            pygame.display.update()
            clock.tick(FPS)


class SpaceShip(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        screen.blit(space_ship, [self.x, self.y])


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
        if self.x >= WIDTH*SCALE - 50:
            self.x = WIDTH*SCALE - 50
        if self.x <= 0:
            self.x = 0
        if self.y >= HEIGHT*SCALE - 50:
            self.y = HEIGHT*SCALE - 50
        if self.y <= 0:
            self.y = 0

        return self.x, self.y
 

class EnemyShip(object):
    def __init__(self, x, y, width, height, ships, first_ship, killed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.ships = ships
        self.first_ship = first_ship
        self.killed = killed
        self.enemy_ship_array = []
        

    def draw(self):
        for enemy in self.enemy_ship_array:
            screen.blit(enemy_ship, [enemy[0], enemy[1]])
            

    def move(self, dy):
        for move in self.enemy_ship_array:
            move[1] += dy

        return self.enemy_ship_array

    def addShip(self):
        x = self.first_ship[0] + 40
        for addenemy in range(self.ships):   
            self.enemy_ship_array.append([self.x+x, self.y-random.randint(100, 200)])
            x += 60


        

class Bullets(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bullet_array = []

    def addBullet(self, x, y):
        self.bullet_array.append([x, y])

        return self.bullet_array

    def draw(self):
        for bullet in self.bullet_array:
            screen.blit(bullet_img, bullet)

    def move(self, dy):
        global move
        move = 0
        for move in self.bullet_array:
            move[1] += dy

        return move


MainWindow(WIDTH*SCALE, HEIGHT*SCALE)