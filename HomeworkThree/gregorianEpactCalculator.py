'''
Author: Jordan Stafford
Problem Statement: This program calculates the gregorian epact based on a user provided year
'''

def main():
  #Take user input
  year = eval(input("Enter a year:"))
  #Display gregorian epact
  print("The Gregorian Epact is:",calculator_gregorian_epact(year))

def calculator_gregorian_epact(year):
  c = year // 100
  return (8+(c//4) - c + ((8*c + 13)//25) + 11*(year%19))%30
  
main()
