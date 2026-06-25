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

issued_books = []

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

    # Issue book
    elif choice == "b":
        name = input("Book name: ")

        if name in books and books[name]["qty"] > 0:
            books[name]["qty"] -= 1
            issued_books.append(name)
            print("Book issued")
        else:
            print("Book not available")

    # Return book
    elif choice == "c":
        name = input("Book name: ")

        if name in issued_books:
            books[name]["qty"] += 1
            issued_books.remove(name)
            print("Book returned")
        else:
            print("Book was not issued")

    # Display books
    elif choice == "d":
        for name in books:
            print(
                name,
                "| Author:", books[name]["author"],
                "| Qty:", books[name]["qty"]
            )

    # Out of stock
    elif choice == "e":
        print("Out of stock books:")
        for name in books:
            if books[name]["qty"] == 0:
                print(name)

    # Unique authors
    elif choice == "f":
        authors = []

        for name in books:
            author = books[name]["author"]

            if author not in authors:
                authors.append(author)

        print("Authors:")
        for author in authors:
            print(author)

    # Highest quantity
    elif choice == "g":
        highest_book = ""
        highest_qty = -1

        for name in books:
            if books[name]["qty"] > highest_qty:
                highest_qty = books[name]["qty"]
                highest_book = name

        print("Highest stock book:", highest_book)
        print("Quantity:", highest_qty)

    # Total books
    elif choice == "h":
        total = 0

        for name in books:
            total += books[name]["qty"]

        print("Total books:", total)

    # Search book
    elif choice == "i":
        search = input("Enter book name: ")

        if search in books:
            print(
                search,
                "| Author:", books[search]["author"],
                "| Qty:", books[search]["qty"]
            )
        else:
            print("Book not found")

    # Issued books
    elif choice == "j":
        print("Issued books:")
        for book in issued_books:
            print(book)

    # Exit
    elif choice == "k":
        break

    else:
        print("Invalid choice")