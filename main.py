# Try to import pygame, if pygame fails to import, raise an error.
try:
    import pygame
except ImportError:
    raise ImportError("ERR: Failed to import pygame. Please install pygame.")

import math

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GREEN = (0,255,0)

# Define sprite classes
# Define class for circle sprite
class Circle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up sprite surface
        self.image = pygame.Surface([500, 500])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw the circle
        pygame.draw.circle(self.image, BLUE, (pos_x // 2, pos_y // 2), 200, 5)
        self.rect = self.image.get_rect()

# define class for the line across the x axis
class XLine(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up sprite surface
        self.image = pygame.Surface([500, 700])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw the line
        pygame.draw.rect(self.image, RED, (pos_x, pos_y, 5, 400))
        self.rect = self.image.get_rect()

# define class for the line across the y axis       
class YLine(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up sprite surface
        self.image = pygame.Surface([500, 700])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw the line
        pygame.draw.rect(self.image, RED, (pos_x, pos_y, 400, 5))
        self.rect = self.image.get_rect()

# define class for the marker that moves across the x marker        
class XMarker(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up variables
        self.angle = 0
        self.angle_speed = 0.05
        self.pos_x = pos_x
        self.pos_y = pos_y
        # set up sprite surface
        self.image = pygame.Surface([600, 600])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw the marker
        pygame.draw.circle(self.image, YELLOW, (self.pos_x // 2, self.pos_y // 2), 15)
        self.rect = self.image.get_rect()
    
    # define method to move the x marker
    def move(self):
        # set up variables
        radius = 400
        center = 600
        
        # increase angle
        self.angle += self.angle_speed
        
        # do math
        # This represents the following equation:
        # x = c + cos(a) * r
        # x = 600 + cos(angle) * 400 
        self.new_x = math.floor(center + math.cos(self.angle) * radius)
        
        # apply new x value to marker
        # clear the image
        self.image.fill(BLACK)
        # redraw the marker
        pygame.draw.circle(self.image, YELLOW, (self.new_x // 2, self.pos_y // 2), 15)
    
# define class for the marker that will move along the y axis 
class YMarker(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up variables
        self.angle = 0
        self.angle_speed = 0.05
        self.pos_x = pos_x
        self.pos_y = pos_y
        # set up sprite surface
        self.image = pygame.Surface([600, 600])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw the marker
        pygame.draw.circle(self.image, YELLOW, (self.pos_x // 2, self.pos_y // 2), 15)
        self.rect = self.image.get_rect()
    
    # define a method to move the y marker
    def move(self):
        # set variables
        radius = 400
        center = 600
        
        self.angle += self.angle_speed
        
        # do math
        # this represents the equation:
        # y = c + sin(a) * r
        # y = 600 + sin(angle) * 400
        self.new_y = math.floor(center + math.sin(self.angle) * radius)
        
        # redraw the marker
        self.image.fill(BLACK) # clear the sprite
        pygame.draw.circle(self.image, YELLOW, (self.pos_x // 2, self.new_y // 2), 15) # redraw

# define class for the marker that will move along the circle
class CircleMarker(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # set up variables
        self.angle = 0
        self.angle_speed = 0.05
        # set up sprite surface
        self.image = pygame.Surface([1000, 1000])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # draw marker
        pygame.draw.circle(self.image, GREEN, (pos_x // 2, pos_y // 2), 15)
        self.rect = self.image.get_rect()
    
    # define method to move the circle marker
    def move(self):
        # define variables 
        radius = 400
        self.center = 600
        
        # increase angle
        self.angle += self.angle_speed
        
        # do math
        # this represents the equation:
        # x = c + cos(a) * r
        # y = c + sin(a) * r
        self.new_x = math.floor(self.center + math.cos(self.angle) * radius)
        self.new_y = math.floor(self.center + math.sin(self.angle) * radius)
        
        # redraw the marker w/ new coordinates
        self.image.fill(BLACK) # clear the surface
        pygame.draw.circle(self.image, GREEN, (self.new_x // 2, self.new_y // 2), 15) # redraw the marker

# define class for the text     
class Text(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # define the font; arial at size 24
        self.font = pygame.font.SysFont('Arial', 24)
        
        # define the surface
        self.image = pygame.Surface([1000, 1000])
        # fill with black and make transparent
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # define all the different text
        # define the text
        self.angle_text = self.font.render('Angle θ: ', False, WHITE)
        # render it to the surface
        self.image.blit(self.angle_text, (25, 25))
        
        self.speed_text = self.font.render('Speed: ', False, WHITE)
        self.image.blit(self.speed_text, (25, 50))
        
        self.sin_text = self.font.render('SIN: ', False, WHITE)
        self.image.blit(self.sin_text, (25, 75))
        
        self.cos_text = self.font.render('COSINE: ', False, WHITE)
        self.image.blit(self.cos_text, (25, 100))
        
        self.rect = self.image.get_rect()
    
    # method to update the text
    def update_text(self, angle, speed, sin, cos):
        # clear surface
        self.image.fill(BLACK)
        
        # update the text with new values
        self.angle_text = self.font.render(f'Angle θ: {angle}', False, WHITE)
        self.speed_text = self.font.render(f'Speed: {speed}', False, WHITE)
        self.sin_text = self.font.render(f'SIN: {sin}', False, WHITE)
        self.cos_text = self.font.render(f'COS: {cos}', False, WHITE)
        
        # render the text to the surface
        self.image.blit(self.angle_text, (25, 25))
        self.image.blit(self.speed_text, (25, 50))
        self.image.blit(self.sin_text, (25, 75))
        self.image.blit(self.cos_text, (25, 100))   

# function to determine the current angle of the location of the circle marker in respect to it's place around the circle.
def determine_angle(y, x, c):
    # determine the current angle of the circle
    angle = math.floor((math.atan2(( y - c ), ( x - c ) )) * (180 / math.pi)) 
    # if the angle is a negative then add 360 (otherwise angle goes from 180 to -180 not 0 - 360)
    if angle < 0:
        angle += 360
   
    return angle

def determine_sin(sine):
    # define max and min variables
    min = 200
    max = 999
    
    # normalize the y location of the marker to be scaled to sine
    # this represents the equation:
    # x = (s - min / max - min) * 2 - 1
    # x = (s - 200 / 999 - 200) * 2 - 1
    normalized_sin = round(((sine - min) / (max - min)) * 2 - 1, 3)
    
    # return the inverse of the normalized sine
    return -normalized_sin

def determine_cos(cosine):
    # define max and min variables
    min = 200
    max = 999
    
    # normalize the x location of the marker to be scaled correctly to cosine
    normalized_cosine = round(((cosine - min) / (max - min)) * 2 - 1, 3)
    
    # return the normalized cosine
    return normalized_cosine
            
     
    
# define basic variables
WIDTH = 600
HEIGHT = 600
FPS = 30

# initalise pygame
pygame.init()
# define pygame variables
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trig functions in pygame")
clock = pygame.time.Clock()

# Create sprite group and sprites
sprites = pygame.sprite.Group()
circle = Circle(600, 600)
x_line = XLine(297, 100)
y_line = YLine(100, 297)
x_marker = XMarker(200, 600)
y_marker = YMarker(600, 200)
c_marker = CircleMarker(1000, 600)
text = Text()
sprites.add(circle)
sprites.add(x_line)
sprites.add(y_line)
sprites.add(x_marker)
sprites.add(y_marker)
sprites.add(c_marker)
sprites.add(text)

# Game loop
running = True
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    # update the sprites group
    sprites.update()
    
    # fill the background with black
    screen.fill(BLACK)

    # draw the sprites on the screen
    sprites.draw(screen)
    
    # move each of the marker sprites
    
    c_marker.move()
    x_marker.move()
    y_marker.move()
    
    # update the text
    text.update_text(determine_angle(c_marker.new_y, c_marker.new_x, c_marker.center), c_marker.angle_speed, determine_sin(y_marker.new_y), determine_cos(x_marker.new_x))
    
    # update the display
    pygame.display.update()

    # sync the clock
    clock.tick(FPS)

# when the loop exits, quit pygame
pygame.quit()
