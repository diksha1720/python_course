import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice==0:
  user_gesture=rock
elif user_choice==1:
  user_gesture=paper
else:
  user_gesture=scissors

system_options=[rock, paper, scissors]
system_gesture=random.choice(system_options)

print("You chose :\n", user_gesture)

print("System chose :\n",system_gesture)


if user_gesture==system_gesture:
  print("Game came to a draw")
elif system_gesture==rock:
  if user_gesture==paper:
    print("You win!!!!!!")
  elif user_gesture==scissors:
    print("You lose!! Game Over")
elif system_gesture==paper:
  if user_gesture==scissors:
    print("You win!!!!!!")
  elif user_gesture==rock:
    print("You lose!! Game Over")
else:
  if user_gesture==rock:
    print("You win!!!!!!")
  elif user_gesture==paper:
    print("You lose!! Game Over")


