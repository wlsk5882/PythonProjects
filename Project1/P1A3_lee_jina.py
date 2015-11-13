"""
author					: Jina Lee
original creation date	: Nov. 6, 2015
last modification date	: 

This program is a part of Dice Challenge.

The rules are as follows:
A player of this game would roll two dice. 
The player will win if the sum of rolled numbers a 5 or 10.
The player will lose if the sum of rolled numbers a 2,4 or 11.
The other numbers are "match number", if the player rolls one of match number, he would roll dice again.
If the player rolls 5, he loses. If the player rolls "match number" again, he wins.
Otherwise, he continues to roll the dice until either he would win or lose.

In this program provides a function that output a result of big start roll.
Rolled dice numbers are created randomly.
"""
import random

def main():
	#prompt to get a participant's name
	user_name=input("Please type your name: ")
	print("Hello, ",user_name, "!", sep="")
	print("My name is Jina.")
	# game description to be displayed for a participant
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
	
	
	# big start roll
	big_start_roll = roll_dice()
	print("Your big start roll is",big_start_roll)
	
	return(big_start_roll, b_start_roll(big_start_roll))


# This function generates 2 random dice number and returns sum of these numbers.
def roll_dice():
	#ask user to start a game
	input("Press Enter key to start your game!")
	
	num1 = random.randint(1,6) # result of dice1 roll
	num2 = random.randint(1,6) # result of dice2 roll
	
	#print("dice 1 roll: ",num1)
	#print("dice 2 roll: ",num2)
	
	roll_result = num1+num2
	print("You rolled", roll_result)
	return roll_result
	
# This function determines if a participant win/lose/match his first game.
# input "roll" is going to be a big start roll.
# This function returns the result as a number: 1(win), -1(lose), 0(match game)
def b_start_roll(roll):	
	if roll == 5 or roll==10:
		print("You won the big start roll!")
		return(1)
	elif roll == 2 or roll==4 or roll==11:	
		print("You lost the big start roll!")
		return(-1)
	else:
		print("You need to roll dice again to complete this game.")
		return(0)
	
main()
	



