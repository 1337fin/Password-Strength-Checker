from PasswordChecker import PasswordChecker

# Author: fin702106
# Date: 21/03/2024
# File: ~/PasswordChecker/main.py

password: str = input("Password > ")

checker = PasswordChecker(password)

check = checker.checkPassword()
