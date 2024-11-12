import random
from settings import screen_size
from settings import screen
from vector import Vector3
import pygame
class Ball:
    def __init__(self,position=(random.randint(0, screen_size[0]), random.randint(0, screen_size[1]), 0), color=(0, 0, 0), radius=5, vector=Vector3((1, 0, 0)), destination=None, nom=None, num=None):
        self.position = position
        self.vector = vector
        self.color = color
        self.radius = radius
        self.destination = destination
        self.oncontrole = False
        self.nom = nom 
        self.num = num
        self.mindist = 1
        self.stabilise = False
    def update(self):
        if self.oncontrole == True and self.destination is not None:
            dist = distance(self.position, self.destination)
            
            # If the ball is far from the destination, apply movement
            if dist > self.mindist:  
                vect = calculate_collision_direction(self.position, self.destination).normalize()
                force_magnitude = dist / 1000 # Increase the speed as needed
                self.vector += vect.neg("xy") * force_magnitude  # Apply force to move towards the destination
                self.mindist += 0.5 if not self.stabilise else 0.1
            else:
                # If the ball is very close, reduce movement to stabilize
                if not self.stabilise:
                    self.stabilise = True
                
                if self.mindist != 1:
                    self.mindist = 1
                self.vector = Vector3((0, 0, 0))  # No movement needed
                self.position = self.destination  # Set position to destination to avoid bouncing

            
        self.position = self.vector.updpos(self.position)
        
        
        if self.position[0] >= screen_size[0] or self.position[0] <= 0 :
            self.vector = self.vector.neg("x")
        
        if ((self.position[1] >= screen_size[1]) if not self.oncontrole else False) or ((self.position[1] < 0) if not self.oncontrole else False):
            self.vector = self.vector.neg("y")

def distance(obj1, obj2):
    if type(obj1) == Ball and type(obj2) == Ball:
        return abs(obj1.position[0] - obj2.position[0]) + abs(obj1.position[1] - obj2.position[1])
    else:
        return abs(obj1[0] - obj2[0]) + abs(obj1[1] - obj2[1])

def calculate_collision_direction(ball1, ball2):
    if type(ball1) == Ball and type(ball2) == Ball:
        return Vector3((ball1.position[0] - ball2.position [0], ball1.position[1] - ball2.position [1], 0)).normalize()
    else:
        return Vector3((ball1[0] - ball2[0] , ball1[1] - ball2[1], 0)).normalize()

def checkcollitions(balls):
    print('check coll')
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):
            dist = distance(balls[i], balls[j])
            if dist < 10:
                vect = calculate_collision_direction(balls[i], balls[j])
                balls[i].vector = vect * 1
                balls[j].vector = vect.neg("xy") * 1
    
    
    
