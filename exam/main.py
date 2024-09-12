data = []
while True:
    print('\nWelcome to the Library Management System!')     
    print("1. Add books")
    print("2. View all books")
    print("3. Update a book")
    print("4. Remove a book")
    print("5. Search for a book")
    print("6. Exit") 
    option = int(input('Select an option: '))

    if option == 1:
        book_id = int(input("Enter book ID: "))
        book_name = str(input('Enter the name of the book: '))
        author_name = str(input('Enter the name of the author: '))
        year_of_pub = int(input('Enter the year of publish: '))
        data.append([book_id, book_name, author_name, year_of_pub])
        print(book_name, 'added!')

    elif option == 2:
        if data:
            print("\nAll books in the library:")
            for book in data:
                print(f"Book ID: {book[0]}, Book Name: {book[1]}, Author: {book[2]}, Year of Publish: {book[3]}")
        else:
            print("No books in the library.")

    elif option == 3:
        book_id_update = int(input("Enter the book ID to update: "))
        book_found = False
        for book in data:
            if book[0] == book_id_update:
                print("Current Name: " + book[1])
                new_name = input("Enter new name (leave blank to keep current): ")
                book[1] = new_name or book[1]
                
                print("Current Author: " + book[2])
                new_author = input("Enter new author (leave blank to keep current): ")
                book[2] = new_author or book[2]
                
                print("Current Year of Publish: " + str(book[3]))
                new_year = input("Enter new year (leave blank to keep current): ")
                book[3] = int(new_year) if new_year else book[3]
                
                print("Book updated successfully!\n")
                book_found = True
                break        
        if not book_found:
            print("Book not found.")

    elif option == 4:
        book_id_remove = int(input("Enter the book ID to remove: "))
        book_found = False
        for book in data:
            if book[0] == book_id_remove:
                data.remove(book)
                book_found = True
                print(f"Book with ID {book_id_remove} has been removed.")
                break
        if not book_found:
            print("Book not found.")

    elif option == 5:
        search_name = input("Enter the name of the book to search: ").lower()
        found = False
        for book in data:
            if search_name in book[1].lower():
                print(f"Found: Book ID: {book[0]}, Book Name: {book[1]}, Author: {book[2]}, Year of Publish: {book[3]}")
                found = True
        if not found:
            print("Book not found.")
    elif option == 6:
        print("Exiting the system...")
        break
    else:
        print("Invalid option. Please try again.")
