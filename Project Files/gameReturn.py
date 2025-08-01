import database
import feedbackManager as FM
from datetime import datetime

'''
Student ID: F328307

gameReturn Module

This module contains a function related to returning a game.

Functions:
- returnGame(gameID, rating, comments): Returns a game and adds
a rating and comments from the user to get feedback of the game
'''


def returnGame(gameID, rating, comments):
	'''
    Return a game by its ID, allowing the user to provide a rating and comments.

    Args:
    - gameID (str): The ID of the game being returned.
    - rating (int): The rating given to the game.
    - comments (str): Additional comments or feedback about the game.

    Returns:
    - str: A message indicating the result of the return attempt.
    '''
	rentalFile = database.readfile("Rental.txt")

	for i in range(len(rentalFile)):
		if gameID == rentalFile[i]["GameID"]:
			if rentalFile[i]["ReturnDate"] == " ":
				rentalFile[i]["ReturnDate"] = datetime.today().date()
				FM.add_feedback(gameID, rating, comments)
				message = "Game has been returned\nThank You"
				break
			else:
				message = "Game cannot be returned"
		else:
			message = "Game ID does not exist"


	headers = rentalFile[0].keys()
	database.writeToFile("Rental.txt", headers, rentalFile)
	
	return message



if __name__ == "__main__": 
	# TESTING FOR GAME RETURN

	# The function should add a return date to the rental text file for the zelda01 file
	# and the passed data into the game feedback text file
	# This will only work if zelda01 is not returned otherwise an appropriate message is displayed
	returnGame("zelda01", 4, "Great Gameplay!")
	# TEST SUCCESSFUL