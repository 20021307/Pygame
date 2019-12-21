import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import webbrowser

pygame.init()

font = pygame.font.Font('OpenSans-Regular.ttf', 30)
font1 = pygame.font.Font('OpenSans-Regular.ttf', 20)
font2 = pygame.font.Font('OpenSans-Regular.ttf', 30)
font3 = pygame.font.Font('OpenSans-Regular.ttf', 15)

# konstante
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
red_bright = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
gold = (255, 176, 31)
green_bright = (0, 255, 0)
WIDTH = 1000
HEIGHT = 480


pygame.display.set_caption("Vislice")
display = pygame.display.set_mode((WIDTH, HEIGHT))

crka_a = font.render('A', True, (0, 0, 0))
crka_b = font.render('B', True, (0, 0, 0))
crka_c = font.render('C', True, (0, 0, 0))
crka_d = font.render('D', True, (0, 0, 0))
crka_e = font.render('E', True, (0, 0, 0))
crka_f = font.render('F', True, (0, 0, 0))
crka_g = font.render('G', True, (0, 0, 0))
crka_h = font.render('H', True, (0, 0, 0))
crka_i = font.render('I', True, (0, 0, 0))
crka_j = font.render('J', True, (0, 0, 0))
crka_k = font.render('K', True, (0, 0, 0))
crka_l = font.render('L', True, (0, 0, 0))
crka_m = font.render('M', True, (0, 0, 0))
crka_n = font.render('N', True, (0, 0, 0))
crka_o = font.render('O', True, (0, 0, 0))
crka_p = font.render('P', True, (0, 0, 0))
crka_r = font.render('R', True, (0, 0, 0))
crka_s = font.render('S', True, (0, 0, 0))
crka_s_ = font.render('Š', True, (0, 0, 0))
crka_t = font.render('T', True, (0, 0, 0))
crka_u = font.render('U', True, (0, 0, 0))
crka_v = font.render('V', True, (0, 0, 0))
crka_z = font.render('Z', True, (0, 0, 0))
crka_z_ = font.render('Ž', True, (0, 0, 0))

uporabljene = font1.render("Uporabljene črke:", True, blue)
preostalo = font1.render("Preostalih preizkusov: ", True, red)
naslov = font3.render("Vislice", True, black)

gesla = ["slemi", "eeprom", "periferija", "strežnik", "modem"]
geslo = random.choice(gesla)
bes_uporabljene = []
runda = []

img1 = pygame.image.load('img/1.png')
img2 = pygame.image.load('img/2.png')
img3 = pygame.transform.flip(pygame.image.load('img/3.png'), True, False)
img4 = pygame.transform.flip(pygame.image.load('img/4.png'), True, False)
img5 = pygame.transform.flip(pygame.image.load('img/5.png'), True, False)
img6 = pygame.transform.flip(pygame.image.load('img/6.png'), True, False)
img7 = pygame.transform.flip(pygame.image.load('img/7.png'), True, False)
img8 = pygame.transform.flip(pygame.image.load('img/8.png'), True, False)
img9 = pygame.transform.flip(pygame.image.load('img/9.png'), True, False)
img10 = pygame.transform.flip(pygame.image.load('img/10.png'), True, False)


class MainWINDOW:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.main()
        self.runda = 1

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(display, ic, (x, y, w, h))

        smallText = pygame.font.Font("OpenSans-Regular.ttf", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        display.blit(textSurf, textRect)

    def zmaga(self, geslo):
        global runda
        loop1 = True
        runda.append(1)
        zmaga = font2.render("Čestitam, vaše geslo je: " + geslo, True, gold)
        while loop1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        self.restart()

            display.blit(zmaga, (350, 50))
            while geslo in bes_uporabljene != "slemi":
                geslo = random.choice(gesla)

            if len(runda) < 2:
                self.button("Nadaljuj", 400, 350, 100, 50, green, green_bright, self.restart)
            if len(runda) >= 2:
                self.button("Konec", 525, 350, 100, 50, red, red_bright, self.koncaj)

            pygame.display.update()

    def restart(self):
        self.main()

    def koncaj(self):
        url = 'http://eucilnica.sc-celje.si/escaperoom'
        webbrowser.get('windows-default').open(url)
        pygame.quit()
        quit()

    def main(self):
        global geslo, bes_uporabljene
        loop = True
        a, b, c, c_, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, s_, t, u, v, z, z_ = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
        narobe = 0
        poizkusi = 10
        while loop:
            if len(bes_uporabljene) >= 4:
                bes_uporabljene = []
            preostalo = font1.render("Preostalih napačnih poizkusov: " + str(poizkusi-narobe), True, red)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if 96 < event.key < 123 and event.key != 113 and event.key != 119 and event.key != 121 and event.key != 120 or event.key == 92 or event.key == 91:
                        if geslo.find(str(chr(event.key))) == -1 and event.key != 92:
                            narobe += 1
                        if event.key == pygame.K_a:
                            a = True
                        if event.key == pygame.K_b:
                            b = True
                        if event.key == pygame.K_c:
                            c = True
                        if event.key == 59:
                            c_ = True
                        if event.key == pygame.K_d:
                            d = True
                        if event.key == pygame.K_e:
                            e = True
                        if event.key == pygame.K_f:
                            f = True
                        if event.key == pygame.K_g:
                            g = True
                        if event.key == pygame.K_h:
                            h = True
                        if event.key == pygame.K_i:
                            i = True
                        if event.key == pygame.K_j:
                            j = True
                        if event.key == pygame.K_k:
                            k = True
                        if event.key == pygame.K_l:
                            l = True
                        if event.key == pygame.K_m:
                            m = True
                        if event.key == pygame.K_n:
                            n = True
                        if event.key == pygame.K_o:
                            o = True
                        if event.key == pygame.K_p:
                            p = True
                        if event.key == pygame.K_r:
                            r = True
                        if event.key == pygame.K_s:
                            s = True
                        if event.key == event.key == 91:
                            s_ = True
                        if event.key == pygame.K_t:
                            t = True
                        if event.key == pygame.K_u:
                            u = True
                        if event.key == pygame.K_v:
                            v = True
                        if event.key == pygame.K_z:
                            z = True
                        if event.key == 92:
                            z_ = True

            display.fill(white)
            display.blit(uporabljene, (25, 250))
            display.blit(preostalo, (10, 50))
            display.blit(naslov, (self.w-65, self.h-30))

            if narobe >= 0:
                display.blit(pygame.transform.scale(img1, (350, 270)), (650, 100))
            if narobe >= 1:
                display.blit(pygame.transform.scale(img2, (350, 270)), (650, 100))
            if narobe >= 2:
                display.blit(pygame.transform.scale(img3, (350, 270)), (560, 100))
            if narobe >= 3:
                display.blit(pygame.transform.scale(img4, (350, 270)), (560, 100))
            if narobe >= 4:
                display.blit(pygame.transform.scale(img5, (350, 270)), (560, 100))
            if narobe >= 5:
                display.blit(pygame.transform.scale(img6, (350, 270)), (560, 100))
            if narobe >= 6:
                display.blit(pygame.transform.scale(img7, (350, 270)), (560, 100))
            if narobe >= 7:
                display.blit(pygame.transform.scale(img8, (350, 270)), (560, 100))
            if narobe >= 8:
                display.blit(pygame.transform.scale(img9, (350, 270)), (560, 100))
            if narobe >= 9:
                display.blit(pygame.transform.scale(img10, (350, 270)), (560, 100))

            if geslo == "slemi":
                pygame.draw.line(display, black, (140, 190), (180, 190), 3)
                pygame.draw.line(display, black, (190, 190), (230, 190), 3)
                pygame.draw.line(display, black, (240, 190), (280, 190), 3)
                pygame.draw.line(display, black, (290, 190), (330, 190), 3)
                pygame.draw.line(display, black, (340, 190), (380, 190), 3)
                if narobe != 10:
                    if s and l and e and m and i:
                        bes_uporabljene.append("slemi")
                        while geslo in bes_uporabljene != "slemi":
                            geslo = random.choice(gesla)
                        self.zmaga("slemi")
                    if s:
                        display.blit(crka_s, (150, 150))
                    if l:
                        display.blit(crka_l, (200, 150))
                    if e:
                        display.blit(crka_e, (250, 150))
                    if m:
                        display.blit(crka_m, (300, 150))
                    if i:
                        display.blit(crka_i, (350, 150))
                    # ostale
                    if a: display.blit(crka_a, (50, 300))
                    if b: display.blit(crka_b, (80, 300))
                    if c: display.blit(crka_c, (110, 300))
                    if d: display.blit(crka_d, (140, 300))
                    if f: display.blit(crka_f, (200, 300))
                    if g: display.blit(crka_g, (230, 300))
                    if h: display.blit(crka_h, (260, 300))
                    if j: display.blit(crka_j, (310, 300))
                    if k: display.blit(crka_k, (80, 350))
                    if n: display.blit(crka_n, (170, 350))
                    if o: display.blit(crka_o, (200, 350))
                    if p: display.blit(crka_p, (230, 350))
                    if r: display.blit(crka_r, (260, 350))
                    if s_: display.blit(crka_s_, (110, 400))
                    if t: display.blit(crka_t, (140, 400))
                    if u: display.blit(crka_u, (170, 400))
                    if v: display.blit(crka_v, (200, 400))
                    if z: display.blit(crka_z, (230, 400))
                    if z_: display.blit(crka_z_, (260, 400))
                else:
                    loop = False
                    bes_uporabljene.append("slemi")
                    while geslo in bes_uporabljene != "slemi":
                        geslo = random.choice(gesla)
                    self.restart()

            if geslo == "eeprom":
                pygame.draw.line(display, black, (140, 190), (180, 190), 3)
                pygame.draw.line(display, black, (190, 190), (230, 190), 3)
                pygame.draw.line(display, black, (240, 190), (280, 190), 3)
                pygame.draw.line(display, black, (290, 190), (330, 190), 3)
                pygame.draw.line(display, black, (340, 190), (380, 190), 3)
                pygame.draw.line(display, black, (390, 190), (430, 190), 3)
                if narobe != 10:
                    if e and p and r and o and m:
                        bes_uporabljene.append("eeprom")
                        while geslo in bes_uporabljene != "eeprom":
                            geslo = random.choice(gesla)
                        self.zmaga("eeprom")
                    if e:
                        display.blit(crka_e, (150, 150))
                        display.blit(crka_e, (200, 150))
                    if p:
                        display.blit(crka_p, (250, 150))
                    if r:
                        display.blit(crka_r, (300, 150))
                    if o:
                        display.blit(crka_o, (350, 150))
                    if m:
                        display.blit(crka_m, (400, 150))
                    # ostale
                    if a: display.blit(crka_a, (50, 300))
                    if b: display.blit(crka_b, (80, 300))
                    if c: display.blit(crka_c, (110, 300))
                    if d: display.blit(crka_d, (140, 300))
                    if f: display.blit(crka_f, (200, 300))
                    if g: display.blit(crka_g, (230, 300))
                    if h: display.blit(crka_h, (260, 300))
                    if i: display.blit(crka_i, (290, 300))
                    if j: display.blit(crka_j, (310, 300))
                    if k: display.blit(crka_k, (80, 350))
                    if l: display.blit(crka_l, (110, 350))
                    if n: display.blit(crka_n, (170, 350))
                    if s: display.blit(crka_s, (290, 350))
                    if s_: display.blit(crka_s_, (110, 400))
                    if t: display.blit(crka_t, (140, 400))
                    if u: display.blit(crka_u, (170, 400))
                    if v: display.blit(crka_v, (200, 400))
                    if z: display.blit(crka_z, (230, 400))
                    if z_: display.blit(crka_z_, (260, 400))
                else:
                    loop = False
                    bes_uporabljene.append("eeprom")
                    while geslo in bes_uporabljene != "eeprom":
                        geslo = random.choice(gesla)
                    self.restart()

            if geslo == "periferija":
                pygame.draw.line(display, black, (140, 190), (180, 190), 3)
                pygame.draw.line(display, black, (190, 190), (230, 190), 3)
                pygame.draw.line(display, black, (240, 190), (280, 190), 3)
                pygame.draw.line(display, black, (290, 190), (330, 190), 3)
                pygame.draw.line(display, black, (340, 190), (380, 190), 3)
                pygame.draw.line(display, black, (390, 190), (430, 190), 3)
                pygame.draw.line(display, black, (440, 190), (480, 190), 3)
                pygame.draw.line(display, black, (490, 190), (530, 190), 3)
                pygame.draw.line(display, black, (540, 190), (580, 190), 3)
                pygame.draw.line(display, black, (590, 190), (630, 190), 3)

                if narobe != 10:
                    if p and e and r and i and f and j and a:
                        bes_uporabljene.append("periferija")
                        while geslo in bes_uporabljene != "periferija":
                            geslo = random.choice(gesla)
                        self.zmaga("periferija")
                    if p:
                        display.blit(crka_p, (150, 150))
                    if e:
                        display.blit(crka_e, (200, 150))
                        display.blit(crka_e, (400, 150))
                    if r:
                        display.blit(crka_r, (250, 150))
                        display.blit(crka_r, (450, 150))
                    if i:
                        display.blit(crka_i, (300, 150))
                        display.blit(crka_i, (500, 150))
                    if f:
                        display.blit(crka_f, (350, 150))
                    if j:
                        display.blit(crka_j, (550, 150))
                    if a:
                        display.blit(crka_a, (600, 150))
                    # ostale
                    if b: display.blit(crka_b, (80, 300))
                    if c: display.blit(crka_c, (110, 300))
                    if d: display.blit(crka_d, (140, 300))
                    if g: display.blit(crka_g, (230, 300))
                    if h: display.blit(crka_h, (260, 300))
                    if k: display.blit(crka_k, (80, 350))
                    if l: display.blit(crka_l, (110, 350))
                    if m: display.blit(crka_m, (140, 350))
                    if n: display.blit(crka_n, (170, 350))
                    if o: display.blit(crka_o, (200, 350))
                    if s: display.blit(crka_s, (290, 350))
                    if s_: display.blit(crka_s_, (110, 400))
                    if t: display.blit(crka_t, (140, 400))
                    if u: display.blit(crka_u, (170, 400))
                    if v: display.blit(crka_v, (200, 400))
                    if z: display.blit(crka_z, (230, 400))
                    if z_: display.blit(crka_z_, (260, 400))
                else:
                    loop = False
                    bes_uporabljene.append("periferija")
                    while geslo in bes_uporabljene != "periferija":
                        geslo = random.choice(gesla)
                    self.restart()

            if geslo == "strežnik":
                pygame.draw.line(display, black, (140, 190), (180, 190), 3)
                pygame.draw.line(display, black, (190, 190), (230, 190), 3)
                pygame.draw.line(display, black, (240, 190), (280, 190), 3)
                pygame.draw.line(display, black, (290, 190), (330, 190), 3)
                pygame.draw.line(display, black, (340, 190), (380, 190), 3)
                pygame.draw.line(display, black, (390, 190), (430, 190), 3)
                pygame.draw.line(display, black, (440, 190), (480, 190), 3)
                pygame.draw.line(display, black, (490, 190), (530, 190), 3)
                if narobe != 10:
                    if s and t and r and e and z_ and n and i and k:
                        bes_uporabljene.append("strežnik")
                        while geslo in bes_uporabljene != "strežnik":
                            geslo = random.choice(gesla)
                        self.zmaga("strežnik")
                    if s:
                        display.blit(crka_s, (150, 150))
                    if t:
                        display.blit(crka_t, (200, 150))
                    if r:
                        display.blit(crka_r, (250, 150))
                    if e:
                        display.blit(crka_e, (300, 150))
                    if z_:
                        display.blit(crka_z_, (350, 150))
                    if n:
                        display.blit(crka_n, (400, 150))
                    if i:
                        display.blit(crka_i, (450, 150))
                    if k:
                        display.blit(crka_k, (500, 150))
                    # ostale
                    if a: display.blit(crka_a, (50, 300))
                    if b: display.blit(crka_b, (80, 300))
                    if c: display.blit(crka_c, (110, 300))
                    if d: display.blit(crka_d, (140, 300))
                    if f: display.blit(crka_f, (200, 300))
                    if g: display.blit(crka_g, (230, 300))
                    if h: display.blit(crka_h, (260, 300))
                    if j: display.blit(crka_j, (310, 300))
                    if l: display.blit(crka_l, (110, 350))
                    if m: display.blit(crka_m, (140, 350))
                    if o: display.blit(crka_o, (200, 350))
                    if p: display.blit(crka_p, (230, 350))
                    if s_: display.blit(crka_s_, (110, 400))
                    if u: display.blit(crka_u, (170, 400))
                    if v: display.blit(crka_v, (200, 400))
                else:
                    loop = False
                    bes_uporabljene.append("strežnik")
                    while geslo in bes_uporabljene != "strežnik":
                        geslo = random.choice(gesla)
                    self.restart()

            if geslo == "modem":
                pygame.draw.line(display, black, (140, 190), (180, 190), 3)
                pygame.draw.line(display, black, (190, 190), (230, 190), 3)
                pygame.draw.line(display, black, (240, 190), (280, 190), 3)
                pygame.draw.line(display, black, (290, 190), (330, 190), 3)
                pygame.draw.line(display, black, (340, 190), (380, 190), 3)
                if narobe != 10:
                    if m and o and d and e and m:
                        bes_uporabljene.append("modem")
                        while geslo in bes_uporabljene != "modem":
                            geslo = random.choice(gesla)
                        self.zmaga("modem")
                    if m:
                        display.blit(crka_m, (150, 150))
                        display.blit(crka_m, (350, 150))
                    if o:
                        display.blit(crka_o, (200, 150))
                    if d:
                        display.blit(crka_d, (250, 150))
                    if e:
                        display.blit(crka_e, (300, 150))
                    # ostale
                    if a: display.blit(crka_a, (50, 300))
                    if b: display.blit(crka_b, (80, 300))
                    if c: display.blit(crka_c, (110, 300))
                    if f: display.blit(crka_f, (200, 300))
                    if g: display.blit(crka_g, (230, 300))
                    if h: display.blit(crka_h, (260, 300))
                    if i: display.blit(crka_i, (290, 300))
                    if j: display.blit(crka_j, (310, 300))
                    if k: display.blit(crka_k, (80, 350))
                    if l: display.blit(crka_l, (110, 350))
                    if n: display.blit(crka_n, (170, 350))
                    if p: display.blit(crka_p, (230, 350))
                    if r: display.blit(crka_r, (260, 350))
                    if s: display.blit(crka_s, (290, 350))
                    if s_: display.blit(crka_s_, (110, 400))
                    if t: display.blit(crka_t, (140, 400))
                    if u: display.blit(crka_u, (170, 400))
                    if v: display.blit(crka_v, (200, 400))
                    if z: display.blit(crka_z, (230, 400))
                    if z_: display.blit(crka_z_, (260, 400))
                else:
                    loop = False
                    bes_uporabljene.append("modem")
                    while geslo in bes_uporabljene != "modem":
                        geslo = random.choice(gesla)
                    self.restart()

            pygame.display.update()


MainWINDOW(WIDTH, HEIGHT)
