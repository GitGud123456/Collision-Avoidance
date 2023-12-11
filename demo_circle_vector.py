import pygame

from pygame.locals import *

import math


BLACK = (0,0,0)

class Vector:

    def __init__(self, *args):
        if len(args) == 2:
            self.x = float(args[0])
            self.y = float(args[1])
        elif len(args) == 1 and isinstance(args[0],Vector): # make a copy of a INPUTED Vector
            other = args[0]
            self.x = float(other.x)
            self.y = float(other.y)


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, (int,float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for multiplication.")
    
    def __truediv__(self,scalar):
        return Vector(self.x / scalar, self.y /scalar)

    def draw(self, screen):
        radius = 2
        distance = math.sqrt((old.x - self.x)**2 + (old.y - self.y)**2)
        if distance > 2*radius:
            pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), radius)


class Circle:

    def __init__(self, position, velocity, radius, color,mass):
        self.position = position
        self.velocity = Vector(*velocity)
        self.radius = radius
        self.mass = mass
        self.color = color

    def move(self):
        self.position = self.position + self.velocity



    def check_wall_collision(self, width, height):

        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= width:
            self.velocity.x *= -1

        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= height:
            self.velocity.y *= -1



    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)



def perfectly_elastic_collision(circle1, circle2):

    v1 = circle1.velocity

    v2 = circle2.velocity

    m1 = 1  # Mass of circle1 

    m2 = 1  # Mass of circle2



    new_v1 = ((v1 * (m1 - m2)) + (Vector(2 * m2,2 * m2)) * v2) / (m1 + m2)

    new_v2 = ((v2 * (m2 - m1)) + (Vector(2 * m2,2 * m2)) * v1) / (m1 + m2)



    circle1.velocity = new_v1

    circle2.velocity = new_v2


def elastic_collision(obj1, obj2):
    # Calculate relative velocity components
    relative_velocity_x = obj2.vx - obj1.vx
    relative_velocity_y = obj2.vy - obj1.vy

    # Calculate relative velocity in terms of the normal vector
    relative_velocity_normal = (
        relative_velocity_x * (obj2.x_pos - obj1.x_pos) +
        relative_velocity_y * (obj2.y_pos - obj1.y_pos)
    ) / ((obj2.x_pos - obj1.x_pos)**2 + (obj2.y_pos - obj1.y_pos)**2)

    # Calculate new velocities after collision using the normal and tangential components
    obj1.vx += relative_velocity_normal * (obj2.x_pos - obj1.x_pos)
    obj1.vy += relative_velocity_normal * (obj2.y_pos - obj1.y_pos)

    obj2.vx -= relative_velocity_normal * (obj2.x_pos - obj1.x_pos)
    obj2.vy -= relative_velocity_normal * (obj2.y_pos - obj1.y_pos)












# Initialize pygame

pygame.init()



# Constants

WIDTH, HEIGHT = 800, 600

FPS = 60



# Colors

WHITE = (255, 255, 255)

RED = (255, 0, 0)

BLUE = (0, 0, 255)



# Create screen

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Physics Simulation")



# Clock for controlling the frame rate

clock = pygame.time.Clock()



# Create circles using the Circle class

circle1 = Circle(position=[WIDTH // 4, HEIGHT // 2], velocity=[5, 1], radius=20, color=RED)

circle2 = Circle(position=[3 * WIDTH // 4, HEIGHT // 2], velocity=[-5, 1], radius=20, color=BLUE)



# Main game loop

running = True

while running:

    for event in pygame.event.get():

        if event.type == QUIT:

            running = False



    # Update circle positions based on velocities


    


    circle1.move()
    circle2.move()



    # Check for collisions with the walls

    circle1.check_wall_collision(WIDTH, HEIGHT)
    circle2.check_wall_collision(WIDTH, HEIGHT)



    # Check for collision between circles

    distance = math.sqrt((circle1.position.x - circle2.position.x)**2 + (circle1.position.y - circle2.position.y)**2)
    if distance <= 2 * circle1.radius:
        perfectly_elastic_collision(circle1, circle2)



    # Draw background

    screen.fill(WHITE)



    # Draw the circles

    circle1.draw(screen)

    circle2.draw(screen)



    # Update the display

    pygame.display.flip()



    # Cap the frame rate

    clock.tick(FPS)



# Quit pygame

pygame.quit()