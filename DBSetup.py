# Setup module for the highscores database

import sqlite3 

conn = sqlite3.connect('EscapeGame.db')

conn.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        Username TEXT NOT NULL PRIMARY KEY,
        Password TEXT NOT NULL)
    """)
conn.commit()

conn.execute(""" 
    CREATE TABLE IF NOT EXISTS HighScores(
        Username TEXT NOT NULL UNIQUE,
        Lev1_score FLOAT,
        lev2_score FLOAT,
        Lev3_score FLOAT,
        Lev4_score FLOAT,
        lev5_score FLOAT,
        Overall FLOAT,
        FOREIGN KEY (Username)
            REFERENCES Users (Username))
    """)
conn.commit()
print("database setup properly, closing connection...")
conn.close()