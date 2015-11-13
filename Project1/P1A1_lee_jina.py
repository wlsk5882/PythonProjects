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

In this program provides with greeting customized with users' name, author information, 
and an instruction of the Dice Challenge.
All input and output are completed via the console.

"""

def main():
	#prompt for get a participant's name.
	user_name=input("Please type your name: ")
	print("Hello, ",user_name, "!", sep="")
	print("My name is Jina.")
	descr = """
	You are going to participate the Dice Challenge.
	The rules are as follows:
	A player of this game would roll two dice. 
	The player will win if the sum of rolled numbers a 5 or 10.
	The player will lose if the sum of rolled numbers a 2,4 or 11.
	The other numbers are "match number", if the player rolls one of match number, he would roll dice again.
	If the player rolls 5, he loses. If the player rolls "match number" again, he wins.
	Otherwise, he continues to roll the dice until either he would win or lose.
"""
	print(descr)
	
main()
	



