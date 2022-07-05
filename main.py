
import pygame, time, random
from pygame.locals import *

pygame.font.init()
font = pygame.font.SysFont("PixelFont-7", 30)
def poczatek():
    quit = False
    while not quit:
        window.fill((0, 0, 0))
        image = pygame.image.load('images/napisy/pacman.png')
        window.blit(image, (64.5,100))
        image = pygame.image.load('images/napisy/start.png')
        window.blit(image, (204.5,230))
        image = pygame.image.load('images/napisy/zasady.png')
        window.blit(image, (187.5,300))
        image = pygame.image.load('images/napisy/ranking.png')
        window.blit(image, (182,370))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 204.5 and mouseX < 370.5 and mouseY > 230 and mouseY < 270:
                        poziomy(poziom)
                    if mouseX > 187.5 and mouseX < 387.5 and mouseY > 300 and mouseY < 340:
                        zasady()
                    if mouseX > 182 and mouseX < 393 and mouseY > 370 and mouseY < 410:
                        ranking()
                    
        
def poziomy(poziom):
    quit = False
    while not quit:
        window.fill((0, 0, 0))
        image = pygame.image.load('images/napisy/wybierz.png')
        window.blit(image, (87,100))
        image = pygame.image.load('images/napisy/latwy.png')
        window.blit(image, (202,230))
        image = pygame.image.load('images/napisy/sredni.png')
        window.blit(image, (210,300))
        image = pygame.image.load('images/napisy/trudny.png')
        window.blit(image, (187.5,370))
        image = pygame.image.load('images/napisy/glowna.png')
        window.blit(image, (400,450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 204.5 and mouseX < 370.5 and mouseY > 230 and mouseY < 270:
                        poziom = 1
                        plansza =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 3, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 3, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 3, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0],
                                 [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        hp = 3
                        pkt = 0
                        main(hp, pkt, plansza, poziom)
                        quit = True
                    if mouseX > 187.5 and mouseX < 387.5 and mouseY > 300 and mouseY < 340:
                        poziom = 2
                        plansza =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 3, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 3, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 3, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0],
                                 [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        hp = 1
                        pkt = 0
                        main(hp, pkt, plansza, poziom)
                        quit = True
                    if mouseX > 182 and mouseX < 393 and mouseY > 370 and mouseY < 410:
                        poziom = 3
                        plansza =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                                 [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                                 [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                        hp = 1
                        pkt = 0
                        main(hp, pkt, plansza, poziom)
                        quit = True
                    if mouseX > 400 and mouseX < 524 and mouseY > 450 and mouseY < 510:
                        quit = True
        
def zasady():
    quit = False
    while not quit:
        window.fill((0, 0, 0))
        image = pygame.image.load('images/napisy/zasady.png')
        window.blit(image, (187.5,50))
        image = pygame.image.load('images/napisy/glowna.png')
        window.blit(image, (400,450))
        text = font.render("- Celem gry jest zebranie z planszy wszystkich punktów", True, (255, 255, 255))
        window.blit(text, (10, 119))
        text = font.render("i owoców w jak najkrótszym czasie", True, (255, 255, 255))
        window.blit(text, (40, 149))
        text = font.render("- Po zdobyciu jednego z owoców, gracz dostaje", True, (255, 255, 255))
        window.blit(text, (10, 189))
        text = font.render("specjalny bonus trwający 10 sekund,", True, (255, 255, 255))
        window.blit(text, (40, 219))
        text = font.render("który pozwala na czasowe pozbycie się przeciwnika.", True, (255, 255, 255))
        window.blit(text, (40, 249))
        text = font.render("- Dostępne są trzy poziomy trudności:", True, (255, 255, 255))
        window.blit(text, (10, 289))
        text = font.render("łatwy - 3 życia, 4 owoce na planszy", True, (255, 255, 255))
        window.blit(text, (40, 319))
        text = font.render("średni - 1 życie, 4 owoce na planszy", True, (255, 255, 255))
        window.blit(text, (40, 349))
        text = font.render("trudny - 1 życie, brak owoców na planszy", True, (255, 255, 255))
        window.blit(text, (40, 379))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 400 and mouseX < 524 and mouseY > 450 and mouseY < 510:
                        quit = True

def ranking():
    quit = False
    pygame.display.init()
    while not quit:
        window.fill((0, 0, 0))
        image = pygame.image.load('images/napisy/ranking.png')
        window.blit(image, (182,100))
        image = pygame.image.load('images/napisy/glowna.png')
        window.blit(image, (400,450))
        filepath = "dane.txt"
        f = open(filepath, "r")
        tekst = f.read()
        tekst1 = tekst[0:23]
        tekst2 = tekst[24:47]
        tekst3 = tekst[48:71]
        r = 0
        for i in [tekst1, tekst2, tekst3]:
          text1 = font.render(i[6:23], True, (255, 255, 255))
          window.blit(text1, (50, 200 + (200 * r/2)))
          if i[0:1] == "1":
            a = "Łatwy"
          elif i[0:1] == "2":
            a = "Średni"
          elif i[0:1] == "3":
            a = "Trudny"
          text = font.render(a, True, (255, 255, 255))
          window.blit(text, (240, 200 + (200 * r/2)))
          czas = 1000 - int(i[1:4])
          czas1 = czas // 60
          text2 = font.render(str(czas1), True, (255, 255, 255))
          window.blit(text2, (340, 200 + (200 * r/2)))
          text4 = font.render(":", True, (255, 255, 255))
          window.blit(text4, (355, 200 + (200 * r/2)))
          czas2 = czas % 60
          text5 = font.render(str(czas2), True, (255, 255, 255))
          window.blit(text5, (365, 200 + (200 * r/2)))
          text3 = font.render(i[4:5], True, (255, 255, 255))
          window.blit(text3, (440, 200 + (200 * r/2)))
          r += 1
        f.close()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 400 and mouseX < 524 and mouseY > 450 and mouseY < 510:
                        quit = True

def koniec():
    quit = False
    while not quit:
        window.fill((0, 0, 0))
        image = pygame.image.load('images/napisy/przegrales.png')
        window.blit(image, (155,200))
        image = pygame.image.load('images/napisy/glowna.png')
        window.blit(image, (225.5,280))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 225.5 and mouseX < 349.5 and mouseY > 280 and mouseY < 340:
                        quit = True
            
        
def wygrana(t1):
    quit = False
    while not quit:
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
        text1 = str((t1//25) % 60)
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (520, 30))
        text = font.render(" : ", True, (255, 255, 255))
        window.blit(text, (505, 30))
        text1 = str(t1//25//60)
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (495, 30))
        
        image = pygame.image.load('images/napisy/wygrales.png')
        window.blit(image, (170,100))
        image = pygame.image.load('images/napisy/glowna.png')
        window.blit(image, (225.5,280))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouseX, mouseY = event.pos
                    if mouseX > 225.5 and mouseX < 349.5 and mouseY > 280 and mouseY < 340:
                        quit = True
        
def main(hp, pkt, plansza, poziom):
    quit = False
    speed = 0.1
    u, d, l, r, o, o1, o2, o3, t1 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    lista1 = ["left", "right"]
    lista2 = ["right", "up"]
    lista3 = ["left", "up"]
    e = random.choice(lista1)
    e1 = random.choice(lista2)
    e2 = random.choice(lista3)
    pole = 25
    x = 225
    y = 400
    x1 = 225
    y1 = 250
    x2 = 200
    y2 = 250
    x3 = 250
    y3 = 250
#grafiki gracza i wrogów
    player = [
        pygame.image.load('images/player/gracz.png').convert_alpha(),
        pygame.image.load('images/player/gracz.png').convert_alpha(),
        pygame.image.load('images/player/gracz1.png').convert_alpha(),
        pygame.image.load('images/player/gracz1.png').convert_alpha(),
        pygame.image.load('images/player/gracz2.png').convert_alpha(),
        pygame.image.load('images/player/gracz2.png').convert_alpha()]
    player1 = [
        pygame.image.load('images/player/gracz11.png').convert_alpha(),
        pygame.image.load('images/player/gracz11.png').convert_alpha(),
        pygame.image.load('images/player/gracz12.png').convert_alpha(),
        pygame.image.load('images/player/gracz12.png').convert_alpha(),
        pygame.image.load('images/player/gracz13.png').convert_alpha(),
        pygame.image.load('images/player/gracz13.png').convert_alpha()]
    player_frame = 0
    wrog1 = [
        pygame.image.load('images/wrog1/sprite_00.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_01.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_02.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_03.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_04.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_05.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_06.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_07.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_08.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_09.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_10.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_11.png').convert_alpha(),
        pygame.image.load('images/wrog1/sprite_12.png').convert_alpha(),]
    wrog1_frame = 0
    wrog2 = [
        pygame.image.load('images/wrog2/sprite_00.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_01.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_02.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_03.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_04.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_05.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_06.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_07.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_08.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_09.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_10.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_11.png').convert_alpha(),
        pygame.image.load('images/wrog2/sprite_12.png').convert_alpha(),]
    wrog2_frame = 0
    wrog3 = [
        pygame.image.load('images/wrog3/sprite_00.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_01.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_02.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_03.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_04.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_05.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_06.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_07.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_08.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_09.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_10.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_11.png').convert_alpha(),
        pygame.image.load('images/wrog3/sprite_12.png').convert_alpha(),]
    wrog3_frame = 0
#główna pętla
    while not quit:
        
#odświeżanie ekranu
        pygame.display.update() 
        clock.tick(25)            
        t1 += 1 #czas
        window.fill((0,0,0))
        image = pygame.image.load('images/plansza.png')
        window.blit(image, (0,0))
        for i in range(22):
            for j in range(19):
                if plansza[i][j] == 3:
                    image1 = pygame.image.load('images/owoc.png')
                    window.blit(image1, (j * pole, i * pole))
                if plansza[i][j] == 0:
                    image2 = pygame.image.load('images/pkt.png')
                    window.blit(image2, (j * pole, i * pole))
#tabelka
        pygame.font.init()
        font = pygame.font.SysFont("Pixel Font-7", 20)
#czas
        text1 = str((t1//25) % 60)
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (520, 30))
        text = font.render(" : ", True, (255, 255, 255))
        window.blit(text, (505, 30))
        text1 = str(t1//25//60)
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (495, 30))
#życie
        image = pygame.image.load('images/serce.png')
        window.blit(image, (481, 60))
        if hp >= 2:
            window.blit(image, (501, 60))
            if hp == 3:
                window.blit(image, (521, 60))
#zdobyte punkty
        image = pygame.image.load('images/pkt.png')
        window.blit(image, (487, 90))
        text1 = str(pkt)
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (520, 96))
#czas bonusu
        image = pygame.image.load('images/player/gracz12.png')
        window.blit(image, (485, 120))
        if o > 0:
            text1 = str((o//25)+1)
        if o == 0:
            text1 = "0"
        text = font.render(text1, True, (255, 255, 255))
        window.blit(text, (520, 126))
#obsługa klawiszy
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
        if keyspressed[ord("a")]:
            l = 2
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x <= (j + 1) * pole and x + pole > (j + 1) * pole and y == i * pole:
                            x -= pole * speed
                        if u == 2:
                            u = 1
                        if d == 2:
                            d = 1
                        if r == 2:
                            r = 1
                                
        if keyspressed[ord("d")]:
            r = 2
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x < j * pole and x + pole >= j * pole and y == i * pole:
                            x += pole * speed
                        if u == 2:
                            u = 1
                        if d == 2:
                            d = 1
                        if l == 2:
                            l = 1
        
        if keyspressed[ord("w")]:
            u = 2
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if y <= (i + 1) * pole and y + pole > (i + 1) * pole and x == j * pole:
                            y -= pole * speed
                        if l == 2:
                            l = 1
                        if d == 2:
                            d = 1
                        if r == 2:
                            r = 1
                            
        if keyspressed[ord("s")]:
            d = 2
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if y < i * pole and y >= (i - 1) * pole and x == j * pole:
                            y += pole * speed
                        if u == 2:
                            u = 1
                        if l == 2:
                            l = 1
                        if r == 2:
                            r = 1

#samoistnie
        if not keyspressed[ord("a")]:
            if l > 0:
                for i in range(22):
                    for j in range(19):
                        if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                            if x <= (j + 1) * pole and x + pole > (j + 1) * pole and y == i * pole:
                                x -= pole * speed
                                if u == 1:
                                    u = 0
                                if d == 1:
                                    d = 0
                                if r == 1:
                                    r = 0

        if not keyspressed[ord("d")]:
            if r > 0:
                for i in range(22):
                    for j in range(19):
                        if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                            if x <= j * pole and x + pole > j * pole and y == i * pole:
                                x += pole * speed
                                if u == 1:
                                    u = 0
                                if d == 1:
                                    d = 0
                                if l == 1:
                                    l = 0
                        elif plansza[i][j + 1] == 1:
                            if x < j * pole and x + pole > j * pole and y == i * pole:
                                x += pole * speed
                                if u == 1:
                                    u = 0
                                if d == 1:
                                    d = 0
                                if l == 1:
                                    l = 0
                                    
        if not keyspressed[ord("w")]:
            if u > 0:
                for i in range(22):
                    for j in range(19):
                        if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                            if y <= (i + 1) * pole and y + pole > (i + 1) * pole and x == j * pole:
                                y -= pole * speed
                                if l == 1:
                                    l = 0
                                if d == 1:
                                    d = 0
                                if r == 1:
                                    r = 0
                                    
        if not keyspressed[ord("s")]:
            if d > 0:
                for i in range(21):
                    for j in range(19):
                        if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                            if y <= i * pole and y + pole > i * pole and x == j * pole:
                                y += pole * speed
                                if u == 1:
                                    u = 0
                                if l == 1:
                                    l = 0
                                if r == 1:
                                    r = 0
                        elif plansza[i + 1][j] == 1:
                            if y < i * pole and y + pole > i * pole and x == j * pole:
                                y += pole * speed
                                if u == 1:
                                    u = 0
                                if l == 1:
                                    l = 0
                                if r == 1:
                                    r = 0
#portal
        if x == 0 and y == 250:
            x = 447.5
        if x == 450 and y == 250:
            x = 2.5
        if x1 == 0 and y1 == 250:
            x1 = 447.5
        if x1 == 450 and y1 == 250:
            x1 = 2.5
        if x2 == 0 and y2 == 250:
            x2 = 447.5
        if x2 == 450 and y2 == 250:
            x2 = 2.5
        if x3 == 0 and y3 == 250:
            x3 = 447.5
        if x3 == 450 and y3 == 250:
            x3 = 2.5 
#zbieranie punktów
        for i in range(22):
            for j in range(19):
                if plansza[i][j] == 0:
                    if ((x == (j + 0.5) * pole or x + pole == (j + 0.5) * pole) and y == i * pole) or (x == j * pole and (y == (i + 0.5) * pole or y + pole == (i + 0.5) * pole)):
                        plansza[i][j] = 2
                        pkt += 1
#owoce
        for i in range(22):
            for j in range(19):
                if plansza[i][j] == 3:
                    if ((x == (j + 0.5) * pole or x + pole == (j + 0.5) * pole) and y == i * pole) or (x == j * pole and (y == (i + 0.5) * pole or y + pole == (i + 0.5) * pole)):
                        plansza[i][j] = 2
                        o = 250
                        pkt += 1
        if o > 0:
            o -= 1
#przeciwnicy
        window.blit(wrog1[ wrog1_frame ], (x1,y1))
        wrog1_frame = (wrog1_frame + 1) % len(wrog1)
        s = 1
#ruch1
        if e == "left" and o1 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x1 <= (j + 1) * pole and x1 + pole > (j + 1) * pole and y1 == i * pole:
                            x1 -= pole * speed
                            s = 1
                    elif plansza[i][j] == 1:
                        if x1 < (j + 1) * pole and x1 + pole > (j + 1) * pole and y1 == i * pole:
                            x1 -= pole * speed
                            s = 1
        if e == "right" and o1 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x1 <= j * pole and x1 + pole > j * pole and y1 == i * pole:
                            x1 += pole * speed
                            s = 1
                    elif plansza[i][j] == 1:
                        if x1 < j * pole and x1 + pole > j * pole and y1 == i * pole:
                            x1 += pole * speed
                            s = 1
        if e == "up" and o1 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if y1 <= (i + 1) * pole and y1 + pole > (i + 1) * pole and x1 == j * pole:
                            y1 -= pole * speed
                            s = 1             
        if e == "down" and o1 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if y1 + pole > i * pole and y1 <= i * pole and x1 == j * pole:
                            y1 += pole * speed
                            s = 1
                    elif plansza[i + 1][j] == 1:
                        if y1 + pole > i * pole and y1 < i * pole and x1 == j * pole:
                            y1 += pole * speed
                            s = 1 
#skret1
        if e == "left" and s == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x1 == (j + 1) * pole and y1 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s = 0
                                e = "down"
                            if plansza[i + 1][j] == 1:
                                s = 0
                                e = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["left", "up"]
                            e = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["left", "down"]
                            e = random.choice(lista)
                        
        if e == "right" and s == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x1 + pole == j * pole and y1 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s = 0
                                e = "down"
                            if plansza[i + 1][j] == 1:
                                s = 0
                                e = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["right", "up"]
                            e = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["right", "down"]
                            e = random.choice(lista)
                        
        if e == "up" and s == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y1 == (i + 1) * pole and x1 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s = 0
                                e = "right"
                            if plansza[i][j + 1] == 1:
                                s = 0
                                e = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["left", "up"]
                            e = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["right", "up"]
                            e = random.choice(lista)
                            
                                    
        if e == "down" and s == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y1 + pole == i * pole and x1 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s = 0
                                e = "right"
                            if plansza[i][j + 1] == 1:
                                s = 0
                                e = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["left","down"]
                            e = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x1 == j * pole and y1 == i * pole:
                            s = 0
                            lista = ["right", "down"]
                            e = random.choice(lista)
#2. przeciwnik
        window.blit(wrog2[ wrog2_frame ], (x2,y2))
        wrog2_frame = (wrog2_frame + 1) % len(wrog2)
        s1 = 1
#ruch2
        if e1 == "left" and o2 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x2 <= (j + 1) * pole and x2 + pole > (j + 1) * pole and y2 == i * pole:
                            x2 -= pole * speed
                            s1 = 1
                    elif plansza[i][j] == 1:
                        if x2 < (j + 1) * pole and x2 + pole > (j + 1) * pole and y2 == i * pole:
                            x2 -= pole * speed
                            s1 = 1
        if e1 == "right" and o2 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x2 <= j * pole and x2 + pole > j * pole and y2 == i * pole:
                            x2 += pole * speed
                            s1 = 1
                    elif plansza[i][j] == 1:
                        if x2 < j * pole and x2 + pole > j * pole and y2 == i * pole:
                            x2 += pole * speed
                            s1 = 1
        if e1 == "up" and o2 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if y2 <= (i + 1) * pole and y2 + pole > (i + 1) * pole and x2 == j * pole:
                            y2 -= pole * speed
                            s1 = 1             
        if e1 == "down" and o2 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if y2 + pole > i * pole and y2 <= i * pole and x2 == j * pole:
                            y2 += pole * speed
                            s1 = 1
                    elif plansza[i + 1][j] == 1:
                        if y2 + pole > i * pole and y2 < i * pole and x2 == j * pole:
                            y2 += pole * speed
                            s1 = 1 
#skret2
        if e1 == "left" and s1 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x2 == (j + 1) * pole and y2 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s1 = 0
                                e1 = "down"
                            if plansza[i + 1][j] == 1:
                                s1 = 0
                                e1 = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["left", "up"]
                            e1 = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["left", "down"]
                            e1 = random.choice(lista)
                        
        if e1 == "right" and s1 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x2 + pole == j * pole and y2 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s1 = 0
                                e1 = "down"
                            if plansza[i + 1][j] == 1:
                                s1 = 0
                                e1 = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["right", "up"]
                            e1 = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["right", "down"]
                            e1 = random.choice(lista)
                        
        if e1 == "up" and s1 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y2 == (i + 1) * pole and x2 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s1 = 0
                                e1 = "right"
                            if plansza[i][j + 1] == 1:
                                s1 = 0
                                e1 = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["left", "up"]
                            e1 = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["right", "up"]
                            e1 = random.choice(lista)
                            
                                    
        if e1 == "down" and s1 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y2 + pole == i * pole and x2 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s1 = 0
                                e1 = "right"
                            if plansza[i][j + 1] == 1:
                                s1 = 0
                                e1 = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["left","down"]
                            e1 = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x2 == j * pole and y2 == i * pole:
                            s1 = 0
                            lista = ["right", "down"]
                            e1 = random.choice(lista)    
#3. przeciwnik
        window.blit(wrog3[ wrog3_frame ], (x3,y3))
        wrog3_frame = (wrog3_frame + 1) % len(wrog3)
        s2 = 1
#ruch3
        if e2 == "left" and o3 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x3 <= (j + 1) * pole and x3 + pole > (j + 1) * pole and y3 == i * pole:
                            x3 -= pole * speed
                            s2 = 1
                    elif plansza[i][j] == 1:
                        if x3 < (j + 1) * pole and x3 + pole > (j + 1) * pole and y3 == i * pole:
                            x3 -= pole * speed
                            s1 = 1
        if e2 == "right" and o3 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x3 < j * pole and x3 + pole > j * pole and y3 == i * pole:
                            x3 += pole * speed
                            s2 = 1
                    elif plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if x3 <= j * pole and x3 + pole > j * pole and y3 == i * pole:
                            x3 += pole * speed
                            s2 = 1

        if e2 == "up" and o3 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 0 or plansza[i][j] == 2 or plansza[i][j] == 3:
                        if y3 <= (i + 1) * pole and y3 + pole > (i + 1) * pole and x3 == j * pole:
                            y3 -= pole * speed
                            s2 = 1             
        if e2 == "down" and o3 == 0:
            for i in range(22):
                for j in range(19):
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if y3 + pole > i * pole and y3 <= i * pole and x3 == j * pole:
                            y3 += pole * speed
                            s2 = 1
                    elif plansza[i + 1][j] == 1:
                        if y3 + pole > i * pole and y3 < i * pole and x3 == j * pole:
                            y3 += pole * speed
                            s2 = 1 
#skret3
        if e2 == "left" and s2 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x3 == (j + 1) * pole and y3 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s2 = 0
                                e2 = "down"
                            if plansza[i + 1][j] == 1:
                                s2 = 0
                                e2 = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["left", "up"]
                            e2 = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["left", "down"]
                            e2 = random.choice(lista)
                        
        if e2 == "right" and s2 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if x3 + pole == j * pole and y3 == i * pole:
                            if plansza[i - 1][j] == 1:
                                s2 = 0
                                e2 = "down"
                            if plansza[i + 1][j] == 1:
                                s2 = 0
                                e2 = "up"
                    if plansza[i - 1][j] == 0 or plansza[i - 1][j] == 2 or plansza[i - 1][j] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["right", "up"]
                            e2 = random.choice(lista)                            
                    if plansza[i + 1][j] == 0 or plansza[i + 1][j] == 2 or plansza[i + 1][j] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["right", "down"]
                            e2 = random.choice(lista)
                        
        if e2 == "up" and s2 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y3 == (i + 1) * pole and x3 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s2 = 0
                                e2 = "right"
                            if plansza[i][j + 1] == 1:
                                s2 = 0
                                e2 = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["left", "up"]
                            e2 = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["right", "up"]
                            e2 = random.choice(lista)
                            
                                    
        if e2 == "down" and s2 == 1:
            for i in range(22):
                for j in range(19):
                    if plansza[i][j] == 1:
                        if y3 + pole == i * pole and x3 == j * pole:
                            if plansza[i][j - 1] == 1:
                                s2 = 0
                                e2 = "right"
                            if plansza[i][j + 1] == 1:
                                s2 = 0
                                e2 = "left"
                    if plansza[i][j - 1] == 0 or plansza[i][j - 1] == 2 or plansza[i][j - 1] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["left","down"]
                            e2 = random.choice(lista)                            
                    if plansza[i][j + 1] == 0 or plansza[i][j + 1] == 2 or plansza[i][j + 1] == 3:
                        if x3 == j * pole and y3 == i * pole:
                            s2 = 0
                            lista = ["right", "down"]
                            e2 = random.choice(lista)  
#życie
        if o == 0 and ((x + pole > x1 and x < x1 + pole and y + pole > y1 and y < y1 + pole) or (x + pole > x2 and x < x2 + pole and y + pole > y2 and y < y2 + pole) or (x + pole > x3 and x < x3 + pole and y + pole > y3 and y < y3 + pole)):
            hp -= 1
            x = 225
            y = 400
            u, d, l, r = 0, 0, 0, 0
        elif o > 0:
            if (x + pole > x1 and x < x1 + pole and y + pole > y1 and y < y1 + pole):
                x1 = 225
                y1 = 250
                o1 = 125
            if (x + pole > x2 and x < x2 + pole and y + pole > y2 and y < y2 + pole):
                x2 = 200
                y2 = 250
                o2 = 125
            if (x + pole > x3 and x < x3 + pole and y + pole > y3 and y < y3 + pole):
                x3 = 250
                y3 = 250
                o3 = 125
        if o1 > 0:
            o1 -= 1
        if o2 > 0:
            o2 -= 1
        if o3 > 0:
            o3 -= 1
#gracz
        if o == 0:
            window.blit(player[ player_frame ], (x,y))
            player_frame = (player_frame + 1) % len(player)
        elif o > 0:
            window.blit(player1[ player_frame ], (x,y))
            player_frame = (player_frame + 1) % len(player)
        if hp == 0:
            koniec()
            quit = True
        if pkt == 195:
            quit = True
    if hp > 0 and pkt == 195:
        filepath = "dane.txt"
        poziom1 = str(poziom)
        t2 = str(1000 - (t1//25))
        hp4 = str(hp)
        znak = (poziom1 + t2 + hp4)
        f = open(filepath, "r")
        tekst = f.read()
        tekst1 = tekst[0:23]
        tekst2 = tekst[24:47]
        tekst3 = tekst[48:71]
        if int(tekst[0:5]) <= int(znak):
            f.close()
            h = open(filepath, "w")
            h.write(poziom1)
            h.write(t2)
            h.write(hp4)
            h.write(" ")
            h.write(time.strftime("%x %X"))
            h.write("\n")
            h.write(tekst1)
            h.write("\n")
            h.write(tekst2)
            h.close()
        elif int(tekst[0:5]) > int(znak):
            if int(tekst[24:30]) <= int(znak):
                f.close()
                h = open(filepath, "w")
                h.write(tekst1)
                h.write("\n")
                h.write(poziom1)
                h.write(t2)
                h.write(hp4)
                h.write(" ")
                h.write(time.strftime("%x %X"))
                h.write("\n")
                h.write(tekst2)
                h.close()
            elif int(tekst[24:30]) > int(znak):
                if int(tekst[48:54]) <= int(znak):
                    f.close()
                    h = open(filepath, "w")
                    h.write(tekst1)
                    h.write("\n")
                    h.write(tekst2)
                    h.write("\n")
                    h.write(poziom1)
                    h.write(t2)
                    h.write(hp4)
                    h.write(" ")
                    h.write(time.strftime("%x %X"))
                    h.close()
                else:
                    f.close()
        quit1 = False
        while not quit1:
            window.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit1 = True
            font = pygame.font.SysFont("PixelFont-7", 50)
            text = font.render("Twój czas: ", True, (255, 255, 255))
            window.blit(text, (160, 180))
            text1 = str((t1//25) % 60)
            text = font.render(text1, True, (255, 255, 255))
            window.blit(text, (385, 180))
            text = font.render(" : ", True, (255, 255, 255))
            window.blit(text, (360, 180))
            text1 = str(t1//25//60)
            text = font.render(text1, True, (255, 255, 255))
            window.blit(text, (350, 180))
            image = pygame.image.load('images/napisy/wygrales.png')
            window.blit(image, (170,100))
            image = pygame.image.load('images/napisy/glowna.png')
            window.blit(image, (225.5,280))
            pygame.display.update()
                    
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit1 = True
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        mouseX, mouseY = event.pos
                        if mouseX > 225.5 and mouseX < 349.5 and mouseY > 280 and mouseY < 340:
                            quit1 = True
    
#uruchomienie gry
if __name__ == "__main__":
    poziom = ""
    width, height = 575, 550
    print ()
    pygame.init()
    window = pygame.display.set_mode((width, height))   
    clock = pygame.time.Clock()
    poczatek()
    pygame.quit()
