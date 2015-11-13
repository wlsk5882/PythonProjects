"""
author					: Jina Lee
original creation date	: Nov. 11, 2015
last modification date	: Nov. 12, 2015

This program is the 5th activity of Dice Challenge.

The rules of Dice Challenge are as follows:
A player of this game would roll two dice. 
The player will lose if the sum of rolled numbers is 5.
The player will win if the sum of rolled numbers the "match number".
Otherwise, he continues to roll the dice until either he would win or lose.

This program provide a functionality that allows the computer to play on its own without user prompting.
User can choose play mode on prompt. (key: 1- manual run, 2-automatic run)


"""
import random


def main():
	
	user_name=input("Please type your name: ")
	print("Hello, ",user_name, "!", sep="")
	print("My name is Jina.")
	descr = """
	You are going to participate the Dice Challenge.
	The rules are as follows:
	You would roll two dice. 
	You will win if the sum of rolled numbers a 5 or 10.
	You will lose if the sum of rolled numbers a 2,4 or 11.
	The other numbers are "match number", if you rolls one of match number, you would roll dice again.
	If the two dice rolls 5, you lose. If you roll "match number" again, you wins.
	Otherwise, you may continue to roll the dice until either you win or lose.
	"""
	print(descr)
	
	# set a game_mode
	game_mode = input_gamemode()
	
	# if the game mode is manual(1), run a game.
	if game_mode==1:
		run_game(game_mode)
		
	else:
		# put a number of games an user want on number_of_game variable.
		numbers_of_game=int(input("How many games do you want to run automatically?: "))
		# a list to store results of each game
		result=[]
		for game in range(numbers_of_game):
			print("\n================================")
			print("Game",game+1)
			print("================================")
			
			# result of this game run : 1(win), -1(lose), 0(match game)
			this_game=run_game(game_mode)
			print(this_game)
			# put the result into the result list
			result.append(this_game)
			
		print("\n=================================\nSummary\n================================= ")
		for game in range(numbers_of_game):
			#display Win if the result is 1, otherwise display "Lost"
			a= "Won!" if result[game]==1 else "Lost"
			print("Game",game+1,":", a)

# This function checks if an user want to run next game or not. And if the user want run another game, proceed it.
# This is only applicable for a manual mode.
def check_run_next_game(game_mode=1):
	next_game= input("Do you want to play a game again? If you want, press y, or press n: ")
		
	#to prevent value error of prompted value
	while not(next_game=="y" or next_game == "n"):
		next_game =input("Please re-type only one of 'y' for next game or 'n' to finish.")
	
	# run a new game if an user want.
	if next_game == "y":
		print("\n===============NEW GAME=================")
		run_game(game_mode)
	
# This function returns game mode(1: manual mode, 2: automatic run) chosen by user through a prompt.
def input_gamemode():

	str_game_mode = input("If you want to play this game manually, press 1, or if you favor of automatic mode, press 2: ")
	# ask a user to type again when the value is not 1 or 2
	while not(str_game_mode=="1" or str_game_mode=="2"):
		str_game_mode=input("If you want to play this game manually, press 1, or if you favor of automatic mode, press 2: ")
	
	# return game_mode value in int type
	return int(str_game_mode)
	
# run a game according to a game mode.
def run_game(game_mode):
	#input("Press Enter key to start your game!")
	# get and store a big start roll
	big_start_roll = roll_dice()
	output = 0
	print("Your big start roll is",big_start_roll)
	
	#result of the big start roll :  1(win), -1(lose), 0(match game)
	first_roll_result=b_start_roll(big_start_roll)
	
	#move to next round if the result is match game(0) in case a user want to proceed the game or automatically.
	if first_roll_result==0:
		#set a match number
		match_number=big_start_roll
		# run next round of roll, round 2
		output= determine_next(match_number,2,game_mode)
	else:
		output= first_roll_result
		
	return output
	

	
#This function runs next rounds of rolls if big_start_roll is a match game. 
def determine_next(match_number,round,game_mode):
	#print("\nThe match number to win is", match_number,".")
	replay=""
	output=0
	if game_mode==1:
		replay =input("Would you like to roll again to determine win or lose? If Yes, press y, or n: ")
		
		#handling value excepetion
		while not(replay=="y" or replay == "n"):
			replay =input("Please re-type only one of 'y' or 'n'.")
	
	if game_mode==2:
		replay="y"
		
	# if a user want to roll again
	if replay=="y":		
		print("\nRound :",round, ", \nYou will win if you roll the match number, ",match_number, ". You will lose if you roll 5.", sep="")
		roll = roll_dice()
		# if the number of roll is 5, the user lose.
		if roll ==5:
			print("\n...You lost...")
			print("#####Game completed#####\n")
			output = -1
			check_run_next_game()
		# if the number of roll is same as the match number, the user win.
		elif roll == match_number:
			print("\n!!! You won !!!")
			print("#####Game completed#####\n")
			output = 1
			check_run_next_game()
		else:
			#print("You rolled",roll)
			print("going to next round: ")
			output = determine_next(match_number, round+1, game_mode)
	elif replay=="n": print("Finishing this game at your request.")
	return output
	

# This function generates 2 random dice number and returns sum of these numbers.
def roll_dice():

	num1 = random.randint(1,6) # result of dice1 roll
	num2 = random.randint(1,6) # result of dice2 roll
	
	#print("dice 1 roll: ",num1)
	#print("dice 2 roll: ",num2)
	
	# two dice roll number
	roll_result = num1+num2
	print("You rolled", roll_result)
	return roll_result
		
		
# This function determines if a participant win/lose/match his first game.
# input "roll" is going to be a big start roll.
# This function returns the result as a number: 1(win), -1(lose), 0(match game)
def b_start_roll(roll):	
	output=0
	if roll == 5 or roll==10:
		output=1		
		print("\n!!!You won the big start roll!!!")
		check_run_next_game()
	elif roll == 2 or roll==4 or roll==11:	
		print("\nYou lost the big start roll!")
		output=-1
		check_run_next_game()
	else:
		print("You need to roll dice again to complete this game.")
	
	return output
	
			
main()
	



