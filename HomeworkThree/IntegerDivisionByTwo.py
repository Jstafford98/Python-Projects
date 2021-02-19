'''
Author: Jordan Stafford
Problem Statement: This program shows the result of integer division by 2 on a number 
'''
def main():

  #Take an input and display results to user
  num1 = eval(input("Enter a number to divide:"))
  print("{0} divided by 2 is {1}R{2}.".format(num1,str(num1//2),str(num1%2)))

main() 
