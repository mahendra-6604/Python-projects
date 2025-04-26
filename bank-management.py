# Simple Library Management System

# List of available books
books = ["The Alchemist", "Rich Dad Poor Dad", "The Power of Habit", "Atomic Habits", "Deep Work"]

def display_books():
    print("\nAvailable Books:")
    for book in books:
        print(f" - {book}")

def borrow_book(book_name):
    if book_name in books:
        books.remove(book_name)
        print(f"\nYou have borrowed '{book_name}'. Enjoy reading!")
    else:
        print(f"\nSorry, '{book_name}' is not available right now.")

def return_book(book_name):
    books.append(book_name)
    print(f"\nThanks for returning '{book_name}'.")

# Main function
def main():
    while True:
        print("\nLibrary Menu:")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            display_books()
        elif choice == '2':
            book_name = input("Enter the name of the book you want to borrow: ")
            borrow_book(book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book you are returning: ")
            return_book(book_name)
        elif choice == '4':
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
