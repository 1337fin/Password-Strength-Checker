from PasswordChecker import PasswordChecker

# Author: 1f1n
# Date: 21/03/2024
# File: ~/PasswordChecker/main.py

password: str = input("Password > ")

checker = PasswordChecker(password)

check = checker.checkPassword()
