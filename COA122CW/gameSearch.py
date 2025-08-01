import database

'''
Student ID: F328307

gameSearch Module

This module has functions that relate to allowing the user to search
for a game by either using its Title, Genre or Platform

Functions:
-searchByTitle(title): Searches for all the games with a matching title
and returns it to the user
-searchByGenre(genre): Searches for all the games with a matching genre
and returns it to the user
-searchByPlatform(platform): Searches for all the games with a matching platform
and returns it to the user
'''

def searchByTitle(title):
	'''
	Searches for a game in Game_info.txt by title.

	Parameters:
		- title (str): The title of the game to be searched for.

	Returns:
		- list: A list of dictionaries of all the games matching the title with the availability.

	'''

	allGames = []
	gameInfo = database.readfile("Game_info.txt")
	for games in gameInfo:
		if games["Title"] == title:
			allGames.append(games)
			gameID = games["ID"]
			rentalInfo = database.readfile("Rental.txt")

			for rented in rentalInfo:
				if rented["GameID"] == gameID:
					if rented["ReturnDate"] == " ":
						games["available"] = False

					else:
						games["available"] = True

	return allGames


def searchByGenre(genre):
	'''
	Searches for a game in Game_info.txt by genre.

	Parameters:
		- genre (str): The genre of the game to be searched for.

	Returns:
		- list: A list of dictionaries of all the games matching the genre with the availability.

	'''

	allGames = []
	gameInfo = database.readfile("Game_info.txt")
	for games in gameInfo:
		if games["Genre"] == genre:
			allGames.append(games)
			gameID = games["ID"]
			rentalInfo = database.readfile("Rental.txt")

			for rented in rentalInfo:
				if rented["GameID"] == gameID:
					if rented["ReturnDate"] == " ":
						games["available"] = False

					else:
						games["available"] = True

	return allGames



def searchByPlatform(platform):
	'''
	Searches for a game in Game_info.txt by platform

	Parameters:
		- plaform (str): The platform of the game to be searched for.

	Returns:
		- list: A list of dictionaries of all the games matching the platform with the availability

	'''

	allGames = []
	gameInfo = database.readfile("Game_info.txt")
	for games in gameInfo:
		if games["Platform"] == platform:
			allGames.append(games)
			gameID = games["ID"]
			rentalInfo = database.readfile("Rental.txt")
			
			for rented in rentalInfo:
				if rented["GameID"] == gameID:
					if rented["ReturnDate"] == " ":
						games["available"] = False

					else:
						games["available"] = True

	return allGames




if __name__ == "__main__": 
	# TESTING FOR GAME SEARCH
	
	# Should print a list of dictionaries with all the games that have the title FIFA
	print(searchByTitle("FIFA"))
	# TEST SUCCESSFUL


	# Should print a list of dictionaries with all the games that have the genre Shooter
	print(searchByGenre("Shooter"))
	# TEST SUCCESSFUL


	# Should print a list of dictionaries with all the games that have the platform Xbox
	print(searchByPlatform("Xbox"))
	# TEST SUCCESSFUL