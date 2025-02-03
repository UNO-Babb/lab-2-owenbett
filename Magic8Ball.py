#Magic8Ball.py
#Name: Owen Betts
#Date: 01/23/2025
#Assignment: Lab 02, Magic 8 Ball Assignment

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ["As I see it, yes." , "Ask again later." , "Better not tell you now." , "Cannot predict now." , "Concentrate and ask again." , "Don't count on it." , "It is certain." , "It is decidedly so." , "Most Likely." , "My reply is no." , "My sources day no." , "Outlook is not good." , "Outlook is good." , "Reply hazy, try again." , "Signs point to yes." , "Very doubtful." , "Without a doubt." , "Yes." , "Yes - Definetly." , "You may rely on it"]
  #Prompt the user for their question.
  response = input ("Im the Mighty Magic 8 Ball... \nAsk me a question... \n")
  
  #Answer question randomly with one of the options from your earlier list.
  lenth = len(answers)
  r=random.random() * 20
  r=int(r) #cut off any decimal values
  print(r)
  response = answers[r]
  print(response)
if __name__ == '__main__':
  main()
