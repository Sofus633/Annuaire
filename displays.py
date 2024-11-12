from vector import Vector3
from settings import pygame
class Texte:
    def __init__(self, position, text='Place Holder',vector=Vector3()):
        self.vector = vector
        self.text = text
        self.size = 30
        self.color = (255, 255, 255)
        self.position = [position[0] -(len(self.text) * 1.33 * self.size) + 170, position[1] -   (1.33 * self.size)]
        self.font = pygame.font.SysFont('Consolas', self.size )
        self.textvis = self.font.render(str(text), False, self.color)

    def applvect(self, vect):
        self.vector += vect
        
    def change_size(self, num):
        self.size += num
        self.font = pygame.font.SysFont('Consolas', self.size )
        self.textvis = self.font.render(str(self.text), False, self.color)
    
    def change_color(self, color):
        self.color = color
        self.font = pygame.font.SysFont('Consolas', self.size )
        self.textvis = self.font.render(str(self.text), False, self.color)
    