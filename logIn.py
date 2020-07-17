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
        pass_one = '1'
        pass_two = '2'
        while pass_one != pass_two:
            pass_one = input("Enter a password: ")
            pass_two = input("Re-enter the password for confirmation: ")
            if pass_one != pass_two:
                print("Passwords did not match, please try again.")
        password = pass_one
        encrypted_password = sha256_crypt.hash(password)
        #delete password variables from memory to increase security:
        del pass_one
        del pass_two
        del password
        with sql.connect("EscapeGame.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users(Username, Password) VALUES(?,?)", (self.user, encrypted_password))
            con.commit()

    def get_password(self):
        with sql.connect("EscapeGame.db") as con:
            cur = con.cursor()
            cur.execute("SELECT Password FROM Users Where username=?", (self.user,))
            #unpack list of tuple of password hash to verify against user input:
            (encrypted_password,) = cur.fetchall()[0]
            # check user entered password against 
            verified = sha256_crypt.verify(input("Enter your password: "), encrypted_password)
            while not verified:
                print("incorrect password please try again: ")
                verified = sha256_crypt.verify(input("Enter your password: "), encrypted_password)
            # at this point user is "logged-in", can use 'self.user' variable
            # as key for inserting scores into HighScores table