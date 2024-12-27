# operations.py
class CustomerOperations:
    def __init__(self):
        self.books = {}

    def buy_book(self):
        print("\n--- Buy Book ---")
        if not self.books:
            print("No books available.")
            return

        book_name = input("Enter book name: ")
        if book_name in self.books:
            print(f"Original price: {self.books[book_name]}")
            while True:
                bargain_amount = int(input("Enter your offer: "))
                if bargain_amount >= self.books[book_name] * 0.75:
                    print(f"Bargain accepted. Purchase successful at {bargain_amount}.")
                    del self.books[book_name]
                    break
                else:
                    print("Offer too low. Try again.")
        else:
            print("Book not found.")

    def sell_book(self):
        print("\n--- Sell Book ---")
        book_name = input("Enter book name to sell: ")
        price = int(input("Enter price of the book: "))
        self.books[book_name] = price
        print(f"Book '{book_name}' added for sale at price {price}.")

    def search_book(self):
        print("\n--- Search Book ---")
        book_name = input("Enter book name: ")
        if book_name in self.books:
            print(f"'{book_name}' is available at price {self.books[book_name]}.")
        else:
            print(f"'{book_name}' not found.")
