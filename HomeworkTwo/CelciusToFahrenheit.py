# Project: Homework 2 Project 1
# File Name:     CelciusToFahrenheit.py
# Programmer:    Jordan Stafford
# Date:          Jan. 27, 2021
#
# Problem Statement: This program will take a user provided Celcius temperature and convert it to Fahrenheit.
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for a number representing a temperature in Celcius
# 3. Covert the Celcius temperature to Fahrenheit
# 4. Print the resultant temperature to the screen
#
# import the necessary python libraries
# -None

def main():

  #welcome message
  print("===========================================================")
  print("Welcome to the Celcius to Fahrenheit Temperature Converter!")
  print("===========================================================")
  #user input
  celcius = eval(input("What is the Celcius temperature?"))
  #Convert Celcius temperature to Fahrenheit
  fahrenheit = 9/5 * celcius + 32
  #Display
  print("The temperature is",fahrenheit,"degrees Fahrenheit.")

main()
