# Setup module for the highscores database

import sqlite3 

conn = sqlite3.connect('EscapeGame.db')

conn.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        Username TEXT NOT NULL PRIMARY KEY,
        Password TEXT NOT NULL)
    """)
conn.commit()
conn.close()