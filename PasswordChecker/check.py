import re

from PasswordChecker.commonPasswords import commonPasswords

class PasswordChecker:
    
    def __init__(self, password):
        self.symbolPattern = r'[!@#$%^&*()\-_=+[\]{};:\'",.<>?£]'
        self.commonPasswords = commonPasswords()
        self.password = password
        self.points = 0

    def checkPassword(self) -> bool:
        """Checks the length and symbol presence of a password"""

        if not self.password:
            print("Password is empty.")
            return False
        if self.password in self.commonPasswords:
            print("Password found in database of common passwords.")
            return False
        elif len(self.password) < 6:
            print("Password is too short.")
            return False
        elif len(self.password) > 15:
            print("Password is too long.")
            return False

        if bool(re.search(self.symbolPattern, self.password)):
            self.points += 2
            matches = re.findall(self.symbolPattern, self.password)
            if len(matches) > 1:
                self.points += 3
        else:
            self.points = self.points

        if len(self.password) >= 6 and len(self.password) <= 15:
            self.points += 1

        if self.password not in self.commonPasswords:
            self.points += 1
        
        return self.ratePassword()

    def ratePassword(self) -> bool:
        """Returns a rating for the password"""

        if self.points <= 3:
            status = "weak"
        elif self.points > 6:
            status = "strong"
        else:
            status = "moderate"

        print(f"Your password '{self.password}' is {status} with a rating of {self.points} points")
        return True

    def showPoints(self) -> int:
        """Returns the amount of points"""
        return self.points
