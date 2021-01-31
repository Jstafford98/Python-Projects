# Project: Homework 2 Project 2
# File Name:     FahrenheitToCelcius.py
# Programmer:    Jordan Stafford
# Date:          Jan. 27, 2021
#
# Problem Statement: Ask the user to enter a temperature in Fahrenheit and convert it to celcius
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a number representing the temperature in Fahrenheit
# 3. Convert the temperature to Celcius
# 4. Print the new temperature to the screen
#
# import the necessary python libraries
# -None

def main():
  #Welcome Message
  print("===========================================================")
  print("Welcome to the Fahrenheit to Celcius Temperature Converter!")
  print("===========================================================")
  #User Input
  degreesF = eval(input("Enter a temperature in Fahrenheit: "))
  #Convert Input to Celcius
  degreesC = 5*(degreesF-32)/9
  #Display Results
  print(degreesF, "degrees Fahrenheit is",round(degreesC,1),"degrees Celcius.")
main()
