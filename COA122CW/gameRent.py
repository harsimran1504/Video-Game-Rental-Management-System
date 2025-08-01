import database
import subscriptionManager as SM
from datetime import datetime

'''
Student ID: F328307

gameRent Module

This module contains functions that allows the user to rent game and
also has functions to check if the game is available.

Functions:
- checkAvailability(gameID): Checks whether a game is available or not so that
the user can rent the game
- rentGame(customerID, gameID): Allows the user to rent a game as long as they
have valid customer credentials and the game is valid and available.
'''

subscriptions = SM.load_subscriptions("Subscription_Info.txt")

def checkAvailability(gameID):
	'''
	Checks the availibilty of the game from the game ID in the rental database text file.

	Parameters:
		- gameID (str): The game ID of the game that is being checked for availability.

	Returns:
		- bool: True if the game is available for rent, False otherwise.

	'''

	isAvailable = True
	rentalFile = database.readfile("Rental.txt")
	for row in rentalFile:
		if row["GameID"] == gameID:
			if row["ReturnDate"] == " ":
				isAvailable = False

	return isAvailable



def rentGame(customerID, gameID):
	'''
	Rents a game based on game ID for a customer with a customer ID.

	Parameters:
		- customerID (str): The ID of the customer renting the game.
		- gameID (str): The game ID of the game to be rented.

	Returns:
		- tuple: A tuple containing a message (str) indicating the result of the rental attempt
		and a dictionary representing the newly rented game details.

	'''
	hasSubscription = SM.check_subscription(customerID, subscriptions)
	rentalFile = database.readfile("Rental.txt")

	newGame = {}

	if hasSubscription:
		subcriptionType = subscriptions[customerID]["SubscriptionType"]
		rentalLimit = SM.get_rental_limit(subcriptionType)
		isAvailable = checkAvailability(gameID)

		gamesRented = 0


		for game in rentalFile:
			if game["RentedCustomerID"] == customerID:
				gamesRented += 1

		if gamesRented <= rentalLimit:

			if isAvailable:
				
				newGame = {'GameID': gameID, 'RentalDate': datetime.today().date(), 'ReturnDate': ' ', 'RentedCustomerID': customerID}
				rentalFile.append(newGame)

				headers = rentalFile[0].keys()
				database.writeToFile("Rental.txt", headers, rentalFile)
				message = "Game is available. Game has been rented"

			else:
				message = "Game not available"

		else:
			message = "You have reached the limit for renting games at your subscription"

	else:
		message = "User currently has no subscriptions. Can't rent game."


	return message, newGame



if __name__ == "__main__": 
	# TESTING FOR GAME RENT

	# Should print that the game is available and the game rental information
	# and will display approprirate message when other conditions are met
	message, game = rentGame("witcher01", "tdnv")
	print(message)
	print(game)
	# TEST SUCCESSFUL


	# Should print True as long as the game witcher01 is not being rented
	print(checkAvailability("witcher01"))
	# TEST SUCCESSFUL