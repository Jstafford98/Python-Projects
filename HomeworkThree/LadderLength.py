'''
Author: Jordan Stafford
Problem Statement: This program determines the length of ladder needed based on the height of a home and the angle
                   of the ladder
'''

from math import pi as pi

def main():
  #Take user input values
  home_height,ladder_angle = eval(input("What is the height of your home?")),eval(input("What is the angle of the ladder?"))
  #Display Results of the calculate_length function
  print("You will need a {0:.2f} foot ladder.".format(calculate_length(home_height,ladder_angle)))

#This function determines the length of an object required based on a height and angle using the height / angle (in radians) formula
def calculate_length(height,angle):
  return height / ((pi/180)*angle)

main()
