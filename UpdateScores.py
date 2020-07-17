import sqlite3 as sql

def update_scores(user, level, score):
    with sql.connect("EscapeGame.db") as con:
        cur = con.cursor()
        if level == 1:
            cur.execute("INSERT INTO HighScores(Username, lev1_score) VALUES(?,?)", (user, score))
        elif level == 2:
            cur.execute("INSERT INTO HighScores(Username, lev2_score) VALUES(?,?)", (user, score))
        elif level == 3:
            cur.execute("INSERT INTO HighScores(Username, lev3_score) VALUES(?,?)", (user, score))
        elif level == 4:
            cur.execute("INSERT INTO HighScores(Username, lev4_score) VALUES(?,?)", (user, score))
        elif level == 5:
            cur.execute("INSERT INTO HighScores(Username, lev5_score) VALUES(?,?)", (user, score))
        con.commit()

def update_overall():
    pass
