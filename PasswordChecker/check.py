import re

# Author: 1337fin
# Date: 21/03/2024
# File: ~/PasswordChecker/check.py

class PasswordChecker:
    
    def __init__(self, password):
        self.symbolPattern = r'[!@#$%^&*()\-_=+[\]{};:\'",.<>?£]'
        self.password = password
        self.points = 0

    def checkPassword(self) -> bool:
        """Checks the length and symbol presence of a password"""

        if not self.password:
            print("Password is empty.")
            return False
        elif len(self.password) < 8:
            print("Password is too short.")
            return False
        elif len(self.password) > 15:
            print("Password is too long.")
            return False

        for letter in self.password:
            if letter == letter.upper():
                self.points += 5
            if letter == letter.lower():
                self.points += 5
        
        numeric_count = sum(1 for char in self.password if char.isdigit())
        self.points += numeric_count * 10

        if self.password == self.password.lower():
            for i in self.password: 
                self.points -= 3

        if self.password == self.password.upper():
            for i in self.password:
                self.points -= 3

        if bool(re.search(self.symbolPattern, self.password)):
            self.points += 2
            matches = re.findall(self.symbolPattern, self.password)
            self.points += len(matches) * 10
        else:
            self.points = self.points
        
        return self.ratePassword()

    def ratePassword(self) -> bool:
        """Returns a rating for the password"""

        if self.points <= 20:
            status = "very low"
        elif 21 <= self.points <= 40:
            status = "low"
        elif 41 <= self.points <= 70:
            status = "medium"
        elif 71 <= self.points <= 80:
            status = "high"
        else:
            status = "very high"

        print(f"Your password '{self.password}' is {status} with a rating of {self.points} points")
        return True

    def showPoints(self) -> int:
        """Returns the amount of points"""
        return self.points
