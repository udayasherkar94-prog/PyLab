#generate a random number
#take a  input as guess number from user

#if it is not a number then
   #show error
# if number < guess number
   #print to low
#if number > guess number
   #print to high
#if number is equal to guess then
  #print congratulation you got write number

import random

number = random.randint(1,100)


while True:
   
  try:
       user_input = input("guess the number between 1 to 100:")
       guess = int(user_input)
       print(guess)

       if guess > number :
           print("to high")
       elif guess < number:
          print("too low")
       else:
          print("congratulation you got it..!")
          break
       
  except:
     print("refernce error")        
     print("invalid guess please enter intiger between 1 to 100")
