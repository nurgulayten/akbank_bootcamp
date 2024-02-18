import sys
class Library:
    def __init__(self):
        self.file = "books.txt"
        self.books = []
        self.file_handle = open(self.file, "a+")

    def __del__(self):
        self.file_handle.close()

    def list_books(self):
        self.file_handle.seek(0)
        self.books = self.file_handle.read().splitlines()
        for book in self.books:
            book_info = book.split(",")
            print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")

        book_info = f"\n{title},{author},{release_year},{num_pages}"
        self.file_handle.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file_handle.seek(0)
        self.books = self.file_handle.read().splitlines()
        for book in self.books:
            if title in book:
                self.books.remove(book)
                break
        self.file_handle.seek(0)
        self.file_handle.truncate()
        for book in self.books:
            self.file_handle.write(book + "\n")
        print("Book removed successfully.")

# Create object
lib = Library()

# Menu
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1/2/3/Q): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice=="Q" or "q":
        print("program kapatılıyor")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
