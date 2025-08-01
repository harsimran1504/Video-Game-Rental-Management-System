import database
import matplotlib.pyplot as plt
import numpy as np
import feedbackManager as FM

# Gets rid of user warning message from matplotlib
import warnings
warnings.filterwarnings("ignore")


'''
Student ID: F328307

InventoryPruning Module

This module contains functions for inventory pruning such as a function
to display a bar chart showing average ratings for games as well as a 
function to display games that have low ratings that can be removed

Functions:
- ratingsBarChart(): Displays a bar chart with all of the games and average ratings
- inventoryPruning(): Returns the games with low ratings to recommend removing
''' 


# Code must be exectuted in the order ratingsBarChart() then inventoryPruning()

def ratingsBarChart():
	'''
    Generates a bar chart displaying the average ratings for games based on feedback data.

    Reads feedback and game information from respective files, calculates average ratings for each game,
    and displays the information as a bar chart using Matplotlib.

    Requires:
    - "Game_Feedback.txt": File containing feedback data for games.
    - "Game_info.txt": File containing information about the games.

    Displays:
    - Bar chart: Represents average ratings for each game.
    '''

	global games, averageScore

	# FM.load_feedback() did not work so I have read the file myself
	gameFeedback = database.readfile("Game_Feedback.txt") 
	gameInfo = database.readfile("Game_info.txt")
	ratings = {}
	count = {}
	average = {}
	for feedback in gameFeedback:
		gameID = feedback["GameID"][:-2]
		if gameID in ratings.keys():
			ratings[gameID] += int(feedback["Rating"])
			count[gameID] += 1

		else:
			ratings[gameID] = int(feedback["Rating"])
			count[gameID] = 1

	for key in ratings:
		average[key] = round(ratings[key]/count[key], 1)

	games = list(average.keys())
	averageScore = list(average.values())

	for i in range(len(games)):
		fullID = games[i]+"01"
		for game in gameInfo:
			if game["ID"] == fullID:
				games[i] = game["Title"] 


	# Plots a bar chart using matplotlib
	fig, ax = plt.subplots()

	ax.grid()
	ax.bar(games, averageScore, align='center')
	plt.xticks(rotation=30, ha='right')
	plt.show()

	


def inventoryPruning():
	'''
    Identifies games for removal based on their average ratings.

    Returns:
    - list: A list of games identified for removal based on an average rating threshold (less than 3).
    '''
	toRemove = [] 
	for i in range(len(averageScore)):
		if averageScore[i] < 3:
			toRemove.append(games[i])

	return toRemove




if __name__ == "__main__": 
	# TESTING FOR INVENTORY PRUNING

	# The function should display 
	ratingsBarChart()
	# TEST SUCCESSFUL


	# The function should return a list of appropriate games to remove
	print(inventoryPruning())
	# TEST SUCCESSFUL
