import sys
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class App(object):
    def __init__(self, width= 800, height= 600):
        self.title= b"XD"
        self.width= width
        self.height= height
        self.angle= 0
        self.distance= 20

def start(self):
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(self.width, self.height)
    glutCreateWindow(self.title)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)