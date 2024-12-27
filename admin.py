# admin.py
class AdminOperations:
    def __init__(self, customer_operations):
        self.customer_operations = customer_operations

    def show_books(self):
        print("\n--- Show Books ---")
        if not self.customer_operations.books:
            print("No books available.")
        else:
            for book_name, price in self.customer_operations.books.items():
                print(f"Book: {book_name}, Price: {price}")

    def show_customers(self, customers):
        print("\n--- Show Customers ---")
        if not customers:
            print("No registered customers.")
        else:
            for username in customers.keys():
                print(f"Customer: {username}")