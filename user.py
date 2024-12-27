# user.py
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.account_activated = False
        self.balance = 0
