#Ask a user to make a choice
#if choice is not valid print error
#let the computer make choice
#print choices emojis{}
#Determine the winner
# Ask user to continue or not
  # if not break | terminate

# winner conditions
# rock and scissor =>  rock wins
# paper and rock => paper wins
# scissor and paper => scissor wins



#rock '✊'
#scissor '✂'
#paper '📃'

import random


emojis = {'r':'✊','p':'📃','s':'✂'}
choices = ('r','p','s')

while True:
  userChoice = input("Enter rock,paper,scissor (r/p/s):").lower()
  if userChoice not in choices:
     print("invalid choice!")
  computerChoice = random.choice(choices)

  print(f"user choice:{emojis[userChoice]}")
  print(f"computer choices:{emojis[computerChoice]}")


  if computerChoice==userChoice:
     print("match is Tai")
  elif((userChoice=='r' and computerChoice=='s')or
       (userChoice=='s' and computerChoice=='p')or
       (userChoice=='p' and computerChoice=='r')):
         print("You Win!")
  else:
     print("You lose")

  should_continue = input("should continue y/n:").lower()

  if should_continue == 'n':
     break


