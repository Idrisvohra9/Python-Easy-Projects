import pygame
import sys

# Strictly speaking, import sys is not needed for PyGame, but as we'll see later, to be able to use the "close window" button on Windows or Mac, we'll need to use sys.exit(), so it is helpful.

pygame.init() # To initialize certain things.

""" Making a window:"""
# Syntax: var_win = pygame.display.set_mode((width_px, height_px))

# Note: always remember that the set_mode() function takes the first argument as the width and second argument as the height.
# So,
# For maths convinience and better usage of the width_px and height_px data in the future we will make two variables of HEIGHT and WIDTH that will go in the tuple of the window display function's set_mode function.

WIDTH=640
HEIGHT=480
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
RUN= True
# FPS=60

# If your screen is of size 640,480:

# The point (0,0) is at the upper left hand corner of the screen.
# x coordinates increase from left to right, y coordinates increase from top to bottom
# So:
    # Upper right is (640,0)
    # Lower left is (0,480)
    # Lower right is (640,480)


"""Filling the display with color:"""
# To fill the window with a certain color this syntax is used.

# Syntax: var_win.fill(color)
# But first we have to generate the color, for that we need to make a tuple variable with the color's name and the color's values in rgb.

# For Example:
# Colors:
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)

# Now filling the WIN variable with the color
WIN.fill(RED)

# Note: for making a window and adding a color the code will not automatically generate the window we have to update the display.
# So,
"""Updataing the display:"""
pygame.display.update()

"""Drawing in the window:"""
# Note: for drawing in the window code will not automatically generate the drawings we have to update the display again.

# Drawing lines:

# Syntax: pygame.draw.lines(screen, color, closed, pointlist, thickness)

    # draws a series of lines, connecting the points specified in pointlist
    # pointlist is a list of tuples, specifying a series of points, e.g. to draw a V you might use [(100,100), (150,200), (200,100)], with closed = False
    # closed should be either True or False, indicating whether to connect the last point back to the first
    # thickness is the thickness of the line (in pixels).
    # Example: pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)

pygame.draw.lines(WIN, BLACK ,False, [(100,100), (150,200), (200,100)],1)
pygame.display.update()
# clock = pygame.time.Clock()
while RUN:
    # clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            RUN=False