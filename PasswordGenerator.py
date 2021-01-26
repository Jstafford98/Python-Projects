#This program generates a cryptographically-secure, random password of X length using capital/lowercase letters, symbols, and numbers
#Author: Jordan Stafford

import random,string 

def main():
  generateRandomPassword()

def generateRandomPassword():
  password  = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(10,25)))
  return password

main()
