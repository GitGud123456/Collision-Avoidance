import pygame
import math
import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



class Seeker:
    def __init__(self, r,x,y,dir):
        self.dir = dir
        self.xV = 5
        self.yV = 5
        self.r = r
        self.hit = False
        self.x = x
        self.y = y



    def caught_hunted_obj(self,hunted_object):
            did_it_hit = 
            if did_it_hit == True:
                self.hit = True
            return did_it_hit
    
    def movement(self,hunted_object):
        dx =  hunted_object.x - self.x
        dy =  hunted_object.y - self.y
        dist = (dx**2 + dy**2)**0.5
        angle = math.atan2(dy,dx)
        self.xV = 5 * math.cos(angle)
        self.yV = 5 * math.sin(angle)
        self.x += self.xV
        self.y += self.yV
        if dist < self.r + hunted_object.r:
            

























pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    #pygame.draw.rect(Surface, color, Rect, width=0): return Rect
    pygame.draw.rect(screen, RED, [55, 50, 20, 25], 0)
    # Draw on the screen a green line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)

    
    for i in range(200):
    
        radians_x = i / 20
        radians_y = i / 6
    
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200
    
        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)  
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text",True,BLACK)
    
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])




    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()