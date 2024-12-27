# library_management.py
from customer import Customer
from operations import CustomerOperations
from admin import AdminOperations

class LibraryManagement:
    def __init__(self):
        self.customers = {}
        self.operations = CustomerOperations()
        self.admin_operations = AdminOperations(self.operations)

    def customer_menu(self):
        while True:
            print("\n--- Customer Menu ---")
            print("1. Register\n2. Login\n3. Exit\n4. Delete Account")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print("Exiting to main menu.")
                break
            elif choice == '4':
                self.delete_account()
            else:
                print("Invalid choice. Try again.")

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Show Books\n2. Show Customers\n3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.admin_operations.show_books()
            elif choice == '2':
                self.admin_operations.show_customers(self.customers)
            elif choice == '3':
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Try again.")

    def register(self):
        print("\n--- Register ---")
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        if password == confirm_password:
            if username in self.customers:
                print("Username already exists. Try another.")
            else:
                self.customers[username] = Customer(username, email, password)
                print("Registration successful.")
        else:
            print("Passwords do not match. Please re-enter your details.")

    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.customers and self.customers[username].password == password:
            print("Login successful.")
            if not self.customers[username].activated:
                print("Account is not activated. Deposit at least 1000 to activate.")
                amount = int(input("Enter amount: "))
                if amount >= 1000:
                    self.customers[username].activated = True
                    self.customers[username].balance += amount
                    print("Activation successful. Returning to main menu.")
                else:
                    print("Amount insufficient for activation. Returning to main menu.")
            else:
                self.customer_operations(username)
        else:
            print("Invalid username or password.")

    def delete_account(self):
        print("\n--- Delete Account ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")

        if username in self.customers and self.customers[username].password == password and password == confirm_password:
            confirmation = input("Are you sure you want to delete your account? (yes/no): ").lower()
            if confirmation == 'yes':
                refund = self.customers[username].balance
                del self.customers[username]
                print(f"Account deleted. Refund amount: {refund}")
            else:
                print("Account deletion canceled.")
        else:
            print("Invalid details or account does not exist.")

    def customer_operations(self, username):
        while True:
            print("\n--- Customer Operations ---")
            print("1. Buy Book\n2. Sell Book\n3. Search for Book\n4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.operations.buy_book()
            elif choice == '2':
                self.operations.sell_book()
            elif choice == '3':
                self.operations.search_book()
            elif choice == '4':
                print("Logging out.")
                break
            else:
                print("Invalid choice. Try again.")

    def main_menu(self):
        while True:
            print("\n--- Welcome to Book Library Management ---")
            print("1. Customer\n2. Admin\n3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.customer_menu()
            elif choice == '2':
                self.admin_menu()
            elif choice == '3':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    library_system = LibraryManagement()
    library_system.main_menu()
