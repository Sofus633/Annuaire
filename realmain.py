from ball import Ball
from settings import screen
from settings import pygame
from displays import Texte
from arbrebin import parcours_infixe_decroissant
from arbrebin import tree
from vector import Vector3
from settings import screen_size 
from ball import checkcollitions
from settings import clock
import math
def mainloop():
    running = True
    while running:
        accueille()
        annuaire()
        
def display(thingtods, linecolor=(150, 150, 150)):
    for thing in thingtods:
        if type(thing) == Ball:
            for ball in thingtods:
                if (abs(ball.position[0] - thing.position[0]) + abs(ball.position[1] - thing.position[1])) < 100:
                    pygame.draw.line(screen, linecolor, (ball.position[0], ball.position[1]), (thing.position[0], thing.position[1]), 1)
            pygame.draw.circle(screen, thing.color, (thing.position[0], thing.position[1]), thing.radius)
            if thing.destination != None:
                #pygame.draw.circle(screen, (0, 255, 0), (thing.destination[0], thing.destination[1]), 10)
                pass
            
        if type(thing) == Texte:
            screen.blit(thing.textvis, (thing.position[0], thing.position[1]))
    pygame.display.flip()
    screen.fill(backgroundcolor)
      
def update(toupd):
    for val in toupd:
        val.update()   
      
def setpos(balls, position):
    tab = []
    for i in range(0, len(balls), 2):
        if i + 1 < len(balls) and balls[i+1]:
            tab.append([balls[i], balls[i+1]])
        else:
            tab.append([balls[i]])
    x, y = position
    for val in tab:
        x = position[0]
        if len(val) > 1:
            val[0].destination = [x, y, 0]
            x +=100
            val[1].destination = [x, y, 0]
            y += 100
        else:
            val[0].destination = [x, y, 0]
        
def annuaire():
    inagenda = True
    balls = parcours_infixe_decroissant(tree)
    
    thingtodisplay = []
    balls2 = createballcircle((screen_size[0] / 2, screen_size[1] / 2),  (150, 150, 150))
    for balle in balls2:
        thingtodisplay.append(balle)
    barposition =  [screen_size[0]//2, screen_size[1]//2]
    setpos(balls, barposition)
    for ball in balls:
        thingtodisplay.append(ball)
        print(ball.destination)

    while inagenda:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inagenda = False
            if event.type == pygame.MOUSEWHEEL:
                print(barposition)
                if event.y > 0:
                    barposition[1] -= 100
                    setpos(balls, barposition)
                else:
                    barposition[1] += 100
                    setpos(balls, barposition)
        mousepos = pygame.mouse.get_pos()
        for ball in balls:
            dist = abs(mousepos[0] - ball.position[0]) + abs(mousepos[1] - ball.position[1])
            if dist < 25:
                print(ball.position[1], ball.position[1] < 0)
                if ball.radius < 20 :
                    ball.radius += 1
            else:
                if ball.radius >= 10:
                    ball.radius -= 1
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_f]:
            for ball in balls:
                ball.oncontrole = True
                print(ball.position)
            for ball in balls2:
                print(ball.oncontrole)
        update(balls)
        update(balls2)
        display(thingtodisplay)
        clock.tick(60)
            
def createballcircle(position, color=(0, 0, 0)):
    a = position[0]
    b = position[1]
    balls = []
    for r in range(0, 600, 3):
        x = a+r*math.cos(r)
        y = b+r*math.sin(r)
        if not x - a == 0 and not 0 == y- b:
            balls.append(Ball((x, y, 0), vector=Vector3((x - a, y- b, 0)).normalize(), color=color))
    return balls
            
def accueille():
    global backgroundcolor
    backgroundcolor = 0
    linecolor = (0, 0, 0)
    inaceuille = True
    animestate = 0
    welcome = Texte((screen_size[0] / 2 - 100, screen_size[1] / 2 - 50), "Annuaire")
    welcomefixed = False
    instructionfix = False
    instruction = Texte((screen_size[0] / 2 - 140, screen_size[1] / 2 + 60), "Press E")
    thingtodisplay = [welcome] 
    balls = []
    animationend = False 
    wait = 0
    while inaceuille:
        animestate += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inaceuille = False
                backgroundcolor = (200, 200, 200)
        mousepos = pygame.mouse.get_pos()
        for ball in balls:
            dist = abs(mousepos[0] - ball.position[0]) + abs(mousepos[1] - ball.position[1])
            if dist < 100:
                if ball.radius < 40 :
                    ball.radius += 1
            else:
                if ball.radius >= 40:
                    ball.radius -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            inaceuille = False
            backgroundcolor = (200, 200, 200)
        if not welcomefixed:
            if welcome.size < 100:
                welcome.change_size(1)
            else:
                welcomefixed = True
        else:
            if not instructionfix:
                if instruction not in thingtodisplay:
                    thingtodisplay.append(instruction) 
                    balls = createballcircle((screen_size[0] / 2, screen_size[1] / 2))
                    for ball in balls:
                        thingtodisplay.insert(0, ball) 
                if instruction.size < 40:
                    instruction.change_size(1)
                if wait < 50:
                    wait += 1
                else:
                    instructionfix = True
            else:
                if not animationend:
                    animationend = True 
                    for ball in balls:
                        ball.color = (150 , 150, 150)
                if instruction.color != (0, 0, 0):
                    instruction.change_color((0, 0, 0))
                if welcome.color != (0, 0, 0):
                    welcome.change_color((0, 0, 0))
                if backgroundcolor != (200, 200, 200):
                    backgroundcolor = (200, 200, 200)
                    linecolor = (150, 150, 150)
                
        
        checkcollitions(balls)
        update(balls)
        display(thingtodisplay, linecolor)
        clock.tick(60)
        
if __name__ == '__main__':
    mainloop()