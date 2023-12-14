import pygame

from pygame.locals import *

import math
import random
objectArray = []
BLACK = (0,0,0)
GREEN = (0,255,0)


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

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int,float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for multiplication.")
    
    def __truediv__(self,scalar):
        return Vector(self.x / scalar, self.y /scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
    

    


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

    def draw_projection(self,width,height,collision_point):
        if collision_point == None:
            point = -100,-100
        else:
            point = collision_point 
        current_pos = self.position
        current_velo = self.velocity
        futrue_pos = current_pos
        print(futrue_pos,collision_point)
        while not (futrue_pos.x - self.radius <= 0 or futrue_pos.x + self.radius >= width or futrue_pos.y - self.radius <=0 or futrue_pos.y + self.radius >= height or futrue_pos == collision_point):
            futrue_pos = futrue_pos.__add__(current_velo)
            pygame.draw.circle(screen, BLACK, (int(futrue_pos.x), int(futrue_pos.y)), self.radius,2)
        return futrue_pos

    def check_wall_collision(self, width, height):

        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= width:
            if self.position.x > width/2:
                var = (self.position.x + self.radius) - width
                self.position.x -= var
                self.velocity.x *= -1
            else:
                var = (self.position.x - self.radius)
                self.position.x -= var
                self.velocity.x *= -1
            return True

        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= height:
             if self.position.y > height/2:
                var = (self.position.y + self.radius) - height
                self.position.y -= var
                self.velocity.y *= -1
             else:
                var = (self.position.y - self.radius)
                self.position.y -= var
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






# def solve_2d_collision(m1, u1x, u1y, m2, u2x, u2y,solve):

#     # Conservation of Momentum equations
#     v1x = (m1*u1x + m2*u2x - m2*(u1x - u2x)) / (m1 + m2)
#     v1y = (m1*u1y + m2*u2y - m2*(u1y - u2y)) / (m1 + m2)
    
#     v2x = (m1*u1x + m2*u2x - m1*(u1x - u2x)) / (m1 + m2)
#     v2y = (m1*u1y + m2*u2y - m1*(u1y - u2y)) / (m1 + m2)

#     if solve == "v1x":
#         return v1x
#     elif solve == "v1y":
#         return v1y
#     elif solve == "v2x":
#         return v2x
#     elif solve == "v2y":
#         return v2y
#     else:
#         return v1x, v1y, v2x, v2y





def perfectly_elastic_collision(circle1, circle2):

    # v1x = circle1.velocity.x
    # v1y = circle1.velocity.y
    # v2x = circle2.velocity.x
    # v2y = circle2.velocity.y

    v1 = circle1.velocity
    v2 = circle2.velocity
    m1 = circle1.mass  # Mass of circle1 
    m2 = circle2.mass  # Mass of circle2

    new_v1 = ((v1 * (m1 - m2)) + (Vector(2 * m2,2 * m2)) * v2) / (m1 + m2)

    new_v2 = ((v2 * (m2 - m1)) + (Vector(2 * m2,2 * m2)) * v1) / (m1 + m2)

    circle1.velocity = new_v1
    circle2.velocity = new_v2


# def elastic_collision(obj1, obj2):
#     # Calculate relative velocity components
#     relative_velocity_x = obj2.vx - obj1.vx
#     relative_velocity_y = obj2.vy - obj1.vy

#     # Calculate relative velocity in terms of the normal vector
#     relative_velocity_normal = (
#         relative_velocity_x * (obj2.x_pos - obj1.x_pos) +
#         relative_velocity_y * (obj2.y_pos - obj1.y_pos)
#     ) / ((obj2.x_pos - obj1.x_pos)**2 + (obj2.y_pos - obj1.y_pos)**2)

#     # Calculate new velocities after collision using the normal and tangential components
#     obj1.vx += relative_velocity_normal * (obj2.x_pos - obj1.x_pos)
#     obj1.vy += relative_velocity_normal * (obj2.y_pos - obj1.y_pos)

#     obj2.vx -= relative_velocity_normal * (obj2.x_pos - obj1.x_pos)
#     obj2.vy -= relative_velocity_normal * (obj2.y_pos - obj1.y_pos)


# def predict_collision_point(circle1, circle2):
#     # Calculate relative velocity
#     relative_velocity = circle2.velocity - circle1.velocity

#     # Calculate relative position
#     relative_position = circle2.position - circle1.position

#     # Calculate time to collision
#     a = relative_velocity.dot(relative_velocity)
#     b = 2 * relative_position.dot(relative_velocity)
#     c = relative_position.dot(relative_position) - (circle1.radius + circle2.radius)**2

#     discriminant = b**2 - 4 * a * c

#     if discriminant < 0:
#         # No real roots, no collision
#         return None

#     # Calculate the time of collision
#     t1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     t2 = (-b - math.sqrt(discriminant)) / (2 * a)

#     # Use the smaller positive root
#     time_to_collision = min(t1, t2) if t1 >= 0 and t2 >= 0 else max(t1, t2)

#     # Predict future positions of the circles at the time of collision
#     future_position1 = circle1.position + circle1.velocity * time_to_collision
#     future_position2 = circle2.position + circle2.velocity * time_to_collision

#     # Average the positions to get the collision point
#     collision_point = (future_position1 + future_position2) * 0.5
#     pygame.draw.circle(screen, GREEN, (int(collision_point.x), int(collision_point.y)), 5)
#     return collision_point.x, collision_point.y

# # Example usage:
# collision_point = predict_collision(circle1, circle2)
# print("Initial Collision Point Prediction:", collision_point)

# # Update velocities
# circle1.velocity = Vector(3, 2)
# circle2.velocity = Vector(-2, 1)

# # Re-predict collision point with updated velocities
# collision_point_updated = predict_collision(circle1, circle2)
# print("Updated Collision Point Prediction:", collision_point_updated)
def filter_circles(original_list):
    return [item for item in original_list if isinstance(item, Circle)]

def find_soonest_collision(circles):
    earliest_collision_time = float('inf')
    collision_pair = None
    collision_point = None

    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            collision_time,point = predict_collision_time(circles[i], circles[j])

            if collision_time is not None and collision_time <= earliest_collision_time:
                earliest_collision_time = collision_time
                collision_pair = (circles[i], circles[j])
                collision_point = point

    return collision_pair,collision_point


def predict_collision_time(circle1, circle2):
    # Calculate relative velocity
    relative_velocity = circle2.velocity - circle1.velocity

    # Calculate relative position
    relative_position = circle2.position - circle1.position

    # Calculate time to collision
    a = relative_velocity.dot(relative_velocity)
    b = 2 * relative_position.dot(relative_velocity)
    c = relative_position.dot(relative_position) - (circle1.radius + circle2.radius)**2

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        # No real roots, no collision
        return None,None

    # Calculate the time of collision
    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # Use the smaller positive root
    time_to_collision = min(t1, t2) if t1 >= 0 and t2 >= 0 else max(t1, t2)
    future_position1 = circle1.position + circle1.velocity * time_to_collision
    future_position2 = circle2.position + circle2.velocity * time_to_collision

    # Average the positions to get the collision point
    collision_point = (future_position1 + future_position2) * 0.5

    objectArray.append((screen,GREEN,(int(collision_point.x), int(collision_point.y)), 5, time_to_collision))
    return time_to_collision,collision_point






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
# for _ in range(0,5):
#     objectArray.append(Circle(position=[WIDTH // 4, HEIGHT // 2], velocity=[random.randint(-7,7), random.randint(-7,7)], radius=random.randint(10,40), color=RED,mass=random.randint(1,20)))
circle1 = Circle(position=[WIDTH // 4, HEIGHT // 2], velocity=[7, 4], radius=20, color=RED,mass=1)
circle2 = Circle(position=[WIDTH // 4, HEIGHT // 2], velocity=[-7, 2], radius=20, color=BLUE,mass=1)
circle3 = Circle(position=[3 * WIDTH // 4, HEIGHT // 2], velocity=[-5, 1], radius=20, color=BLUE,mass=1)

objectArray.append(circle2)
objectArray.append(circle3)
objectArray.append(circle1)
# Main game loop

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    # Update circle positions based on velocities
    for obj in objectArray:
        if isinstance(obj,Circle):
            obj.move()
            obj.check_wall_collision(WIDTH, HEIGHT)
        else:    
            objectArray.remove(obj)


    collision_pair,collision_point = find_soonest_collision(filter_circles(objectArray))





    # Draw background

    screen.fill(WHITE)
    

   


    # Draw the circles
    for obj in objectArray:
        if isinstance(obj,Circle):
            if collision_pair != None and (obj == collision_pair[0] or obj == collision_pair[1]):
                obj.draw_projection(WIDTH,HEIGHT,collision_point)
                obj.draw(screen)
            else:
                obj.draw_projection(WIDTH,HEIGHT,None)
                obj.draw(screen)
        else:
            pygame.draw.circle(obj[0], obj[1], obj[2], obj[3])
           

    # find_soonest_collision(objectArray)


    # Update the display

    pygame.display.flip()



    # Cap the frame rate

    clock.tick(FPS)



# Quit pygame

pygame.quit()