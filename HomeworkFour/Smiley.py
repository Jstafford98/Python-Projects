'''
Author: Jordan Stafford
Problem Statement: This program generates a smiley face using TKinter
'''

#Draw a simple picture with at least 3 graphical objects.
from graphics import *

def main():

  #Inititalize Graphics Window
  win = GraphWin("Shapes")

  #Initialize face shapes
  face_fill = Circle(Point(100,100),30)
  face_outline = Circle(Point(100,100),31)
  left_eye = Circle(Point(87,90),10)
  mouth = Line(Point(87,110),Point(110,110))

  #Set outline fill and width
  face_outline.setFill("black")
  face_outline.setWidth(2)

  #Set fill of face
  face_fill.setFill("yellow")

  #Set Left Eye Width
  left_eye.setWidth(2)

  #Create right eye and shift it 
  right_eye = left_eye.clone()
  right_eye.move(23,0)

  #Draw Face Objects
  face_outline.draw(win) 
  face_fill.draw(win)
  left_eye.draw(win)
  right_eye.draw(win)
  mouth.draw(win)

  #Pause so user can see output
  input()
  #Normally would close window here, but I want the results to remain on screen

main() 

