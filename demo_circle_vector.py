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

    


class Circle:

    def __init__(self, position, velocity, radius, color,mass):
        self.position = Vector(*position)
        self.velocity = Vector(*velocity)
        self.radius = radius
        self.mass = mass
        self.color = color
        self.futrue = (self.position,self.velocity)

    def move(self):
        self.position = self.position + self.velocity

    def draw_projection(self,width,height):
        current_pos = self.position
        current_velo = self.velocity
        futrue_pos = current_pos.__add__(current_velo)
        while not (futrue_pos.x - self.radius <= 0 or futrue_pos.x + self.radius >= width or futrue_pos.y - self.radius <=0 or futrue_pos.y + self.radius >= height):
            futrue_pos = futrue_pos.__add__(current_velo)
            pygame.draw.circle(screen, BLACK, (int(futrue_pos.x), int(futrue_pos.y)), self.radius)

    def check_wall_collision(self, width, height):

        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= width:
            self.velocity.x *= -1
            return True

        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= height:
            self.velocity.y *= -1
            return True
        return False



    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    # def drawfutrue(self, screen):
    #     radius = 2
    #     distance = math.sqrt((old.x - self.x)**2 + (old.y - self.y)**2)
    #     if distance > 2*radius:
    #         pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), radius)






def solve_2d_collision(m1, u1x, u1y, m2, u2x, u2y,solve):

    # Conservation of Momentum equations
    v1x = (m1*u1x + m2*u2x - m2*(u1x - u2x)) / (m1 + m2)
    v1y = (m1*u1y + m2*u2y - m2*(u1y - u2y)) / (m1 + m2)
    
    v2x = (m1*u1x + m2*u2x - m1*(u1x - u2x)) / (m1 + m2)
    v2y = (m1*u1y + m2*u2y - m1*(u1y - u2y)) / (m1 + m2)

    if solve == "v1x":
        return v1x
    elif solve == "v1y":
        return v1y
    elif solve == "v2x":
        return v2x
    elif solve == "v2y":
        return v2y
    else:
        return v1x, v1y, v2x, v2y





def perfectly_elastic_collision(circle1, circle2):

    v1x = circle1.velocity.x
    v1y = circle1.velocity.y
    v2x = circle2.velocity.x
    v2y = circle2.velocity.y
    m1 = circle1.mass  # Mass of circle1 
    m2 = circle2.mass  # Mass of circle2

    (new_v1x,new_v1y,new_v2x,new_v2y) = solve_2d_collision(m1,v1x,v1y,m2,v2x,v2y,0)

    # new_v1 = ((v1 * (m1 - m2)) + (Vector(2 * m2,2 * m2)) * v2) / (m1 + m2)

    # new_v2 = ((v2 * (m2 - m1)) + (Vector(2 * m2,2 * m2)) * v1) / (m1 + m2)



    circle1.velocity = Vector(*(new_v1x,new_v1y))

    circle2.velocity = Vector(*(new_v2x,new_v2y))
    # circle1.velocity = new_v1

    # circle2.velocity = new_v2


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

circle1 = Circle(position=[WIDTH // 4, HEIGHT // 2], velocity=[5, 1], radius=20, color=RED,mass=1)

circle2 = Circle(position=[3 * WIDTH // 4, HEIGHT // 2], velocity=[-5, 1], radius=20, color=BLUE,mass=1)



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

    # distance = math.sqrt((circle1.position.x - circle2.position.x)**2 + (circle1.position.y - circle2.position.y)**2)
    # if distance <= 2 * circle1.radius:
    #     perfectly_elastic_collision(circle1, circle2)



    # Draw background

    screen.fill(WHITE)



    # Draw the circles
    circle1.draw_projection(WIDTH,HEIGHT)
    circle2.draw_projection(WIDTH,HEIGHT)
    circle1.draw(screen)
    circle2.draw(screen)
    


    # Update the display

    pygame.display.flip()



    # Cap the frame rate

    clock.tick(FPS)



# Quit pygame

pygame.quit()