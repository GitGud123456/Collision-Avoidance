import pygame

from pygame.locals import *

import math



class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y



    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y)



    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        elif isinstance(scalar, Vector):
            return Vector(self.x * scalar.x, self.y * scalar.y)
        else:
            raise TypeError("Unsupported operand type for multiplication.")
    
    def __truediv__(self,scalar):
        return Vector(self.x / scalar, self.y /scalar)



class Circle:

    def __init__(self, position, velocity, radius, color):

        self.position = Vector(*position)

        self.velocity = Vector(*velocity)

        self.radius = radius

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

    m1 = 1  # Mass of circle1 (assumed to be 1 for simplicity)

    m2 = 1  # Mass of circle2 (assumed to be 1 for simplicity)



    new_v1 = ((v1 * (m1 - m2)) + (Vector(2 * m2,2 * m2)) * v2) / (m1 + m2)

    new_v2 = ((v2 * (m2 - m1)) + (Vector(2 * m2,2 * m2)) * v1) / (m1 + m2)



    circle1.velocity = new_v1

    circle2.velocity = new_v2



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