from passlib.hash import sha256_crypt
import sqlite3 as sql

class logIn():
    def get_user(self):
        self.user = input("Enter your username: ")
        with sql.connect("EscapeGame.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Username FROM Users WHERE username=?", (self.user,))
            user_exists = cur.fetchall()
            if not user_exists:
                print("I see that you are a new player...")
                self.make_new_user()
            else:
                # returning user, verify password and 'log-in'
                self.get_password()

    def make_new_user(self):
        pass_one = sha256_crypt.encrypt('1')
        pass_two = sha256_crypt.encrypt('2')
        while sha256_crypt.verify(pass_one) != sha256_crypt.verify(pass_two):
            pass_one = sha256_crypt.encrypt(input("Enter a password: "))
            pass_two = sha256_crypt.encrypt(input("Re-enter the password for confirmation: "))
            if sha256_crypt.verify(pass_one) != sha256_crypt.verify(pass_two):
                print("Passwords did not match, please try again.")
        self.password = pass_one
        with sql.connect("EscapeGame.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users(Username, Password) VALUES(?,?)", (self.user, self.password))
            con.commit()

    def get_password(self):
        with sql.connect("escapeGame.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Password FROM Users Where username=?", (self.user,))
            self.password = cur.fetchall()
            print(self.password) 
            while sha256_crypt.verify(self.password) != input("Enter your password: "):
                print("Incorrect password, please try again.")
            # at this point user is "logged-in", can use 'self.user' variable
            # as key for inserting scores into HighScores table