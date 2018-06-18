#!/usr/bin/env python3


import csv
import sqlite3


if __name__ == "__main__":
	# Establishes a connection to the database file master.db.
	connection = sqlite3.connect("master.db", check_same_thread=False)
	# Creates a cursor object, which represents the "gaze" of the RDBMS.
	cursor = connection.cursor()
	# Opens MSFT.csv (read-only) and saves a list of all the rows.
	with open("MSFT.csv", "r") as file:
		rows = csv.reader(file)
		next(rows)
		# Opens CSV file and inserts the values of each row into a row in the database file.
		for row in rows:
			cursor.execute(
				"""INSERT INTO msft(
					date,
					open,
					high,
					low,
					adj_close,
					volume
					) VALUES(?,?,?,?,?,?);
				""", (row[0], row[1], row[2], row[3], row[4], row[5],)
			)
	# Commits (saves) the changes made to the database file.
	connection.commit()
	# Closes the cursor and connection to the database file.
	cursor.close()
	connection.close()
