# customer.py
class Customer:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.activated = False
        self.balance = 0