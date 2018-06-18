#!/usr/bin/env python3


import sqlite3


if __name__ == "__main__":
	# Establishes a connection to the database file master.db.
	connection = sqlite3.connect("master.db", check_same_thread=False)
	# Creates a cursor object, which represents the "gaze" of the RDBMS.
	cursor = connection.cursor()
	# Creates msft table with the specified schema.
	cursor.execute(
		"""CREATE TABLE msft(
			pk INTEGER PRIMARY KEY AUTOINCREMENT,
			date DATETIME,
			open FLOAT,
			high FLOAT,
			low FLOAT,
			adj_close FLOAT,
			volume INTEGER
		);"""
	)
	# Closes cursor and connection to the database file.
	cursor.close()
	connection.close()
