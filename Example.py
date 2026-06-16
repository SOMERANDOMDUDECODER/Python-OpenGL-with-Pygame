import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 800)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

run = True

while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
quit()