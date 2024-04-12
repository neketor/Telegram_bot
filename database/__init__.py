import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()
cities = """ CREATE TABLE IF NOT EXISTS cities(name TEXT) """
cursor.execute(cities)
