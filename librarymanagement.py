data = [
    {'Book ID': 1, 'Book Name': 'harry potter', 'Author': 'j.k rowling', 'Year of Publish': 2000},
    {'Book ID': 2, 'Book Name': 'Sapiens', 'Author': 'Yuval Noah Harari', 'Year of Publish': 2010},
    {'Book ID': 3, 'Book Name': 'amazing spiderman', 'Author': 'stan lee', 'Year of Publish': 1985},
    {'Book ID': 4, 'Book Name': 'game of throns', 'Author': 'geroge rr martin', 'Year of Publish': 1975}
]

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
        book_name = input('Enter the name of the book: ')
        author_name = input('Enter the name of the author: ')
        year_of_pub = int(input('Enter the year of publish: '))
        data.append({'Book ID': book_id, 'Book Name': book_name, 'Author': author_name, 'Year of Publish': year_of_pub})
        print(f"{book_name} added!")

    elif option == 2:
        if data:
            print("\nAll books in the library:")
            for book in data:
                print(f"Book ID: {book['Book ID']}, Book Name: {book['Book Name']}, Author: {book['Author']}, Year of Publish: {book['Year of Publish']}")
        else:
            print("No books in the library.")

    elif option == 3:
        book_id_update = int(input("Enter the book ID to update: "))
        book_found = False
        for book in data:
            if book['Book ID'] == book_id_update:
                print("Current Name: " + book['Book Name'])
                new_name = input("Enter new name (leave blank to keep current): ")
                if new_name:
                    book['Book Name'] = new_name
                
                print("Current Author: " + book['Author'])
                new_author = input("Enter new author (leave blank to keep current): ")
                if new_author:
                    book['Author'] = new_author
                
                print("Current Year of Publish: " + str(book['Year of Publish']))
                new_year = input("Enter new year (leave blank to keep current): ")
                if new_year:
                    book['Year of Publish'] = int(new_year)
                
                print("Book updated successfully!\n")
                book_found = True
                break
        if not book_found:
            print("Book not found.")

    elif option == 4:
        book_id_remove = int(input("Enter the book ID to remove: "))
        book_found = False
        for book in data:
            if book['Book ID'] == book_id_remove:
                data.remove(book)
                book_found = True
                print(f"Book with ID {book_id_remove} has been removed.")
                break
        if not book_found:
            print("Book not found.")

    elif option == 5:
        search_name = input("Enter the name of the book to search: ")
        found = False
        for book in data:
            if search_name.lower() in book['Book Name'].lower():
                print(f"Found: Book ID: {book['Book ID']}, Book Name: {book['Book Name']}, Author: {book['Author']}, Year of Publish: {book['Year of Publish']}")
                found = True
        if not found:
            print("Book not found.")

    elif option == 6:
        print("Exiting the system....")
        break
    else:
        print("Invalid option. Please try again.")
