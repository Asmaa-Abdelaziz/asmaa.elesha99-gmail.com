from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def myInit ():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
             0,0,0,
             0,1,0)
    glMatrixMode(GL_MODELVIEW) 
            
                
def drawWay():
    glColor3f (0.4,0.4,0.4)
    glBegin(GL_POLYGON)
    glVertex3d(-100,3,0)
    glVertex3d(100,3,0)
    glVertex3d(100,3,100)
    glEnd ()
  
      
x=0
theta=0
forward=True 

def draw ():
    global x
    global theta
    global forward
    glLoadIdentity()

    glClearColor(.6,.7,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    drawWay()
#car
    glColor3f(0,0,0)
    glTranslate(x,0,0)
    glScalef(4,1,2)
    glutSolidCube(1)

    glLoadIdentity()
    glTranslate(x,1,0)
    glScalef(2,1,2)
    glutSolidCube(1)

    glColor3f(0,0,0)
    glLoadIdentity()
    glTranslate(x+2,-.5,-1)
    glRotate(theta,0,0,-1)
    glutWireTorus (.1,.3,30,10)

    glLoadIdentity()
    glTranslate(x-2,-.5,-1)
    glRotate(theta,0,0,-1)
    glutWireTorus (.1,.3,30,10)

    glLoadIdentity()
    glTranslate(x-2,-.5,1)
    glRotate(theta,0,0,-1)
    glutWireTorus (.1,.3,30,10)

    glLoadIdentity()
    glTranslate(x+2,-.5,1)
    glRotate(theta,0,0,-1)
    glutWireTorus (.1,.3,30,10)


#lamp
    glColor3f(.8,.6,.0)
    glLoadIdentity()
    glTranslate(x+2,.3,-1)
    glScalef(2,1,2)
    glutSolidCube(.09)

    glLoadIdentity()
    glTranslate(x+2,.3,1)
    glScalef(2,1,2)
    glutSolidCube(.09)

    glLoadIdentity()
    glTranslate(x-2,.3,1)
    glScalef(2,1,2)
    glutSolidCube(.09) 

    glLoadIdentity()
    glTranslate(x-2,.3,-1)
    glScalef(2,1,2)
    glutSolidCube(.09)
    
       
#BLOCS
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(0,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(2,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(4,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(6,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(8,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-4,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-8,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-12,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-16,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-2,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-6,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-10,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2)

    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(-14,3,0)
    glScalef(1,.2,.2)
    glutSolidCube(2) 

#houses & doors & windows
#house
    glLoadIdentity()
    glColor3f(.5,.5,1)
    glTranslate(-4,4.3,-3)
    glScalef(1,1,.2)
    glutSolidCube(5)
#door
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-4,2.6,-3)
    glScalef(1,1,.2)
    glutSolidCube(2)
#window
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-5.5,5.5,-3)
    glScalef(1,1,.2)
    glutSolidCube(1)
#house
    glLoadIdentity()
    glColor3f(1,.5,.5)
    glTranslate(1,4.3,-3)
    glScalef(1,1,.2)
    glutSolidCube(5)
#door
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(1,2.6,-3)
    glScalef(1,1,.2)
    glutSolidCube(2)
#window
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(-.5,5.5,-3)
    glScalef(1,1,.2)
    glutSolidCube(1)
#house
    glLoadIdentity()
    glColor3f(.5,.5,1)
    glTranslate(6,4.3,-3)
    glScalef(1,1,.2)
    glutSolidCube(5)
#door
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(6,2.6,-3)
    glScalef(1,1,.2)
    glutSolidCube(2)
#window
    glLoadIdentity()
    glColor3f(1,1,1)
    glTranslate(4.5,5.5,-3)
    glScalef(1,1,.2)
    glutSolidCube(1)

#tree  
    glColor3f(0.3,.2,0.1)
    glTranslate(-14,-2.4,0)
    glScalef(.5,3,2)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0,.9,0)
    glTranslate(-5.5,5.5,0)
    glScalef(.5,0.5,.5)
    glutSolidSphere (2,3,2)
    
    

    glutSwapBuffers()
    
    if forward :
        x=x+.01
        theta=theta+.88
    else:
        x=x-.01
        theta=theta-.88

    if x >=5:
        forward = False

    if x<= -10:
        forward= True

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (600,600)
glutCreateWindow(b"moving car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
