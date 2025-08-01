import csv

'''
Student ID: F328307

database Module

This module deals with all the file handling such as reading a text file or
writing to a text files.

Functions:
- readfile(filename): Reads the given file and returns all the data in the
file as a dictionary by converting the file data into a csv format
- writeToFile(filename, fieldnames, data) - Write to the given file by using
a csv format of the fieldnames and the data in the given in the form of a dictionary
'''

def readfile(filename):
	'''
	Reads a file into a dictionary using csv.

	Parameters:
		- filename (str): The name of the text file to be read.

	Returns:
		- list: A list of dictionaries representing the data in the text file as a csv.

	'''
	rows = []
	f = open(filename, "r")
	reader = csv.DictReader(f)
	for row in reader:
		rows.append(row)

	f.close()

	return rows


def writeToFile(filename, fieldnames, data):
	'''
	Writes data into text file using csv.

	Parameters:
		- filename (str): The name of the text file to be written to.
		- fieldnames (list): A list containing the fieldnames/headers for the database text files.
		- data (list): A list of dictionaries of the data to be added to the database text files.

	Returns:
		- None
	'''
	f = open(filename, "w", newline="")
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(data)

	f.close()
