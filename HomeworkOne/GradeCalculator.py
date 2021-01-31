# Project: Homework 1 Project 3
# File Name:     GradeCalculator.py
# Programmer:    Jordan Stafford
# Date:          Jan. 26, 2021
#
# Problem Statement: Ask the user to enter two numbers representing the total questions on a quiz and the total number of questions the student answered
# correctly. Using these values, calculate the grade percentage and then display the results to the screen.
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for two integers representing the total questions on a quiz and the total number of questions the student answered
#    correctly
# 3. Calculate the grade percentage by dividing the correct questions by total questions and multiplying by 100
# 4. Print the grade percentage to the screen
#
# import the necessary python libraries
# -None

def main():

  #Welcome message
  print("================================")
  print("Welcome To The Grade Calculator!")
  print("================================")

  #Prompt the user for the total questions on the quiz and the total questions the student got correct
  total_questions = eval(input("How many questions were on the exam?"))
  correct_questions = eval(input("How many questions did the student get correct?"))

  #Calculate grade percentage (Result is multiplied by 100 for formatting purposes)
  grade_percentage = (correct_questions / total_questions) * 100

  #Display result to user
  print("The student recieved a",grade_percentage,"% (",correct_questions,"/",total_questions,")")

main()
