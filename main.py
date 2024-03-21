from PasswordChecker import PasswordChecker

password: str = input("Password > ")

checker = PasswordChecker(password)

check = checker.checkPassword()
