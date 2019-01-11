import time
import random

print("Rock")
time.sleep(0.5)
print("Paper")
time.sleep(0.5)
print("Scissors")
time.sleep(0.5)
print("Shoot!")
time.sleep(0.5)

player_move = input('What is your move? ')
print('Player move was: ' + player_move)

computer_move = random.choice(["Rock", "Paper", "Scissors"])
print('Computer move was: ' + computer_move)

if player_move == "Rock" and computer_move == "Scissors":
	print("You win. Rock crushes scissors!")

if player_move == "Paper" and computer_move == "Rock":
	print("You win. Paper swallows rock!")

if player_move == "Scissors" and computer_move == "Paper":
	print("You win. Scissors cuts paper!")	

if player_move == "Rock" and computer_move == "Rock":
	print("It is tied!")

if player_move == "Paper" and computer_move == "Paper":
	print("It is tied!")

if player_move == "Scissors" and computer_move == "Scissors":
	print("It is tied!")

if player_move == "Scissors" and computer_move == "Rock":
	print("You lose! Scissors gets crushed by Rock.")

if player_move == "Paper" and computer_move == "Scissors":
	print("You lose! Paper gets cut by Scissors.")	

if player_move == "Rock" and computer_move == "Paper":
	print("You lose! Paper gets swallowed by Rock.")					