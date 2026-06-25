# Add a new book to the library.
# Issue a book and update quantity.
# Return an issued book.
# Display all books with available quantity.
# Find books that are out of stock.
# Display all unique authors.
# Find the book with the highest quantity.
# Count the total number of books in the library.
# Search for a book by name.
# Display all issued books.


books = {
    "Python": {"author": "Akhil", "qty": 5},
    "C++": {"author": "John", "qty": 3},
    "Java": {"author": "Akhil", "qty": 0}
}


while True:

    print("\na -> Add new book")
    print("b -> Issue book")
    print("c -> Return book")
    print("d -> Display all books")
    print("e -> Out of stock books")
    print("f -> Unique authors")
    print("g -> Highest quantity book")
    print("h -> Total books count")
    print("i -> Search book")
    print("j -> Display issued books")
    print("k -> Exit")

    choice = input("Enter choice: ")

    # Add book
    if choice == "a":
        name = input("Book name: ")
        author = input("Author: ")
        qty = int(input("Quantity: "))

        books[name] = {"author": author, "qty": qty}
