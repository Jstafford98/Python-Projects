'''
Author: Jordan Stafford
Problem: This program determines the cost per square inch of a pizza 
'''

from math import pi as pi 

def main():

  #Take user input
  price = eval(input("What is the price of this pizza?"))
  diameter = eval(input("What is the diameter of the pizza?"))
  #Print results
  print("The cost of a ${0:.2f} pizza with a diameter of {1:.2f} inches is ${2:.2f}".format(price,diameter,calc_cost(price,diameter)) )

def calc_cost(val,val2):
  #pi*r^2 / price
  return (pi * (val2 / 2)) / val2 
  
main() 
