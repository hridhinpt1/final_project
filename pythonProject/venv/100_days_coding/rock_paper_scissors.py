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

user_input = input(" Select ' Rock' ' Paper' ' scissors' ").lower()
game =['rock','paper','scissors']
selected = random.choice(game).lower()
if(user_input =='rock' and selected =='scissors'):
  print(game[user_input])
  print('VS')
  print(game[user_input])
  print('You win')
elif(user_input == 'scissors' and selected == 'paper'):
  print(game[user_input])
  print('VS')
  print(game[user_input])
  print('You win')
elif(user_input == 'paper' and selected == 'rock'):
  print(game[user_input])
  print('VS')
  print(game[user_input])
  print('You win')
else :
  print(game[user_input])
  print('VS')
  print(game[user_input])
  print('You win')
  print("Sorry try again ,Un lucky this time ")

