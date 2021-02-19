from graphics import *

def main():

    #Create Graphics Window
    win = GraphWin("Plotting Points",200,200)
    win.setCoords(0,0,9,10)

    #Add prompt to window
    prompt = Text(Point(5,1),"Select two dots")
    prompt.draw(win)

    #Add grid dots to window
    for i in range(1,9):
        for j in range(2,10):
            Point(i,j).draw(win)

    #Draw a line based on user selected points
    line_object = Line(win.getMouse(),win.getMouse())
    line_object.draw(win)
    calculateSlope(line_object)
    #Pause to view results
    input()

def calculateSlope(line_object):
    p1,p2 = line_object.getP1(),line_object.getP2()
    slope = (p2.getX()-p1.getX()) / (p2.getY()-p1.getY())
    print("Slope:",slope)

def displayResults():
    print()

main()
