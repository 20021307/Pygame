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
yellow = (255, 255, 0)
grey = (128, 128, 128)


# fps
FPS = 60

# images
space_ship = pygame.image.load("res/space_ship.png")
enemy_ship = pygame.image.load("res/enemy_ship.png")
background = pygame.image.load("res/background.png")
bullet_img = pygame.image.load("res/bullet.png")
enemy_bullet_img = pygame.image.load("res/enemy_bullet.png")
toolbar_img = pygame.image.load("res/toolbar_template.png")
energy_graphic = pygame.image.load("res/energy_graphic.png")
intro_background = pygame.image.load("res/intro_background.png")
logo = pygame.image.load("res/logo.png")

#font
toolbar_font = pygame.font.Font("bold.ttf", 15)
menu_font = pygame.font.Font("bold.ttf", 25)
build_font = pygame.font.Font("bold.ttf", 10)


class MainWindow(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.intro_screen()

    def Main(self):
        global space_ship_new_coord, bullet_x, bullet_new_coord, enemy_ship_new_coord, bullet_length, bullet_new_array,\
            en_bullet_len
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
        enemy_ships = 2
        enemy_killed = 0
        enemy_ship = EnemyShip(10, 10, ship_width, ship_width, first_ship_coord, enemy_killed)
        enemy_ship_mov_speed = 0.5

        # health and energy
        energy = 100
        health = 200

        energy_toolbar = 190
        health_toolbar = 190

        bullet_array = []
        en_bullet_array = []
        enemy_mana = 100

        bullet_new_array = []
        bullet_lenght = 0

        enemy_bullet = EnemyBullet(bullet_width, bullet_height)

        enemy_ship.addShip(enemy_ships)
        enemy_add_num = 20

        toolbar = Toolbar()

        while loop:
            cur_fps = int(clock.get_fps())
            pygame.display.set_caption("Space Game 0.2 -- StrozeR " + str(cur_fps) + " FPS")
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
                        if energy >= 40:
                            bullet_array = bullet.addBullet(int(space_ship_new_coord[0]), int(space_ship_new_coord[1]))
                            bullet_lenght = len(bullet_array)
                            energy -= 40
                            energy_toolbar -= 90

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

            toolbar.drawEnergy(energy_toolbar)
            toolbar.drawHealth(health_toolbar, health)

            space_ship.draw()
            space_ship_new_coord = space_ship.move(space_ship_dx, space_ship_dy)

            bullet.draw()
            bullet.move(bullet_dy)

            enemy_bullet.draw()
            enemy_bullet.move(bullet_dy)

            enemy_ship_array = enemy_ship.move(enemy_ship_mov_speed)
            enemy_ship.draw()

            if enemy_killed == enemy_add_num:
                enemy_ship_mov_speed += 0.5
                enemy_ship.addShip(1)
                enemy_ships += 1
                enemy_add_num += 20



            try:
                if enemy_ships >= 1:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[0][0]-25 < bullet_array[x][0] < enemy_ship_array[0][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[0][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[0] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1

            except:
                pass

            try:
                if enemy_ships >= 2:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[1][0]-25 < bullet_array[x][0] < enemy_ship_array[1][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[1][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[1] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1

            except:
                pass

            try:
                if enemy_ships >= 3:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[2][0]-25 < bullet_array[x][0] < enemy_ship_array[2][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[2][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[2] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1
            except:
                pass

            try:
                if enemy_ships >= 4:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[3][0]-25 < bullet_array[x][0] < enemy_ship_array[3][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[3][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[3] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1
            except:
                pass

            try:
                if enemy_ships >= 5:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[4][0]-25 < bullet_array[x][0] < enemy_ship_array[4][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[4][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[4] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1
            except:
                pass

            try:
                if enemy_ships >= 6:
                    for x in range(bullet_lenght):
                        if enemy_ship_array[5][0]-25 < bullet_array[x][0] < enemy_ship_array[5][0] + ship_width:
                            if bullet_array[x][1] < enemy_ship_array[5][1] + ship_height:
                                del bullet_array[x]
                                enemy_ship_array[5] = [random.randint(0, WIDTH*SCALE-ship_width),
                                                       random.randint(-100, 0)]
                                enemy_killed += 1

            except:
                pass

            for enemy_passed in enemy_ship_array:
                if enemy_passed[1] >= HEIGHT*SCALE:
                    health -= 20
                    enemy_passed[0] = random.randint(0, WIDTH*SCALE-ship_width)
                    enemy_passed[1] = random.randint(-100, 0)
                    health_toolbar -= 20

            if energy < 100:
                energy += 1
                energy_toolbar += 3
            if energy >= 100:
                energy = 100

            if energy_toolbar >= 190:
                energy_toolbar = 190

            if health <= 0:
                health = 0
                health_toolbar = 0
                print("game over")

            if enemy_ships > 6:
                enemy_ships = 6

            if enemy_mana >= 60:
                random_ship = random.randint(0, enemy_ships-1)
                en_bullet_array = enemy_bullet.addBullet(enemy_ship_array[random_ship][0],
                                                         enemy_ship_array[random_ship][1])
                en_bullet_len = len(en_bullet_array)
                enemy_mana -= 40

            enemy_mana += 0.3
            if enemy_mana >= 100:
                enemy_mana = 100

            try:
                for x in range(en_bullet_len):
                    if space_ship_new_coord[0] <= en_bullet_array[x][0] < space_ship_new_coord[0] + ship_width:
                        if space_ship_new_coord[1] <= en_bullet_array[x][1] <= space_ship_new_coord[1]+ship_height:
                            health -= 40
                            health_toolbar -= 40
                            del en_bullet_array[x]

            except:
                pass
            BuildNumber()
            pygame.display.update()
            clock.tick(FPS)

    def intro_screen(self):
        intro = True

        location = 0

        play_color = white
        instruct_color = white
        quit_color = white

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        location -= 1
                    elif event.key == pygame.K_DOWN:
                        location += 1

                    if event.key == pygame.K_RETURN:
                        if location == 0:
                            self.Main()
                            intro = False
                        elif location == 1:
                            pass
                            # self.instruction()
                        elif location == 2:
                            pygame.quit()
                            quit()


            screen.blit(intro_background, [0, 0])
            screen.blit(logo, [WIDTH * SCALE / 2 - int(400 / 2), HEIGHT * SCALE / 4 - 100])

            if location == 0:
                play_color = grey
                instruct_color = white
                quit_color = white
            elif location == 1:
                play_color = white
                instruct_color = grey
                quit_color = white
            elif location == 2:
                play_color = white
                instruct_color = white
                quit_color = grey

            if location <= -1:
                location = 2
            if location >= 3:
                location = 0



            play_label = menu_font.render("Play", 1, play_color)
            instruction_label = menu_font.render("Instructions - WIP", 1, instruct_color)
            quit_label = menu_font.render("Quit", 1, quit_color)



            # draw labels

            screen.blit(play_label, [WIDTH * SCALE / 2 - 50, 200])
            screen.blit(instruction_label, [WIDTH * SCALE / 2 - 120, 300])
            screen.blit(quit_label, [WIDTH * SCALE / 2 - 50, 400])

            BuildNumber()
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
    def __init__(self, x, y, width, height, first_ship, killed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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

    def addShip(self, ships):
        for addenemy in range(ships):
            self.enemy_ship_array.append([random.randint(0, WIDTH*SCALE-50), random.randint(-100, 0)])

        return self.enemy_ship_array
        

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


class EnemyBullet(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.en_bullet_array = []

    def addBullet(self, x, y):
        self.en_bullet_array.append([x, y])

        return self.en_bullet_array

    def draw(self):
        for enemy_bullet in self.en_bullet_array:
            screen.blit(enemy_bullet_img, enemy_bullet)

    def move(self, dy):
        for move in self.en_bullet_array:
            move[1] -= dy



class Toolbar(object):
    def __init__(self):
        pass

    def drawEnergy(self, width):
        screen.blit(toolbar_img, [25, 25])
        pygame.draw.rect(screen, yellow, (30, 30, width, 30))
        screen.blit(energy_graphic, [40, 30])


    def drawHealth(self, width, hp):
        hp_surface = toolbar_font.render(str(hp), 1, white)
        screen.blit(toolbar_img, [25, 70])
        pygame.draw.rect(screen, red, (30, 75, width, 30))
        screen.blit(hp_surface, [105, 85])

    def drawScore(self):
        pass


class BuildNumber(object):
    def __init__(self):
        self.show()

    def show(self):
        build_surface = build_font.render("Release 0.2", 1, white)
        screen.blit(build_surface, [WIDTH*SCALE - 100, HEIGHT*SCALE - 40])


MainWindow(WIDTH*SCALE, HEIGHT*SCALE)