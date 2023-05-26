#author: David Labra Gaona
#Purpose: Read a text file and display the information

with open("books.txt") as books:
    for book in books:
        book = book.strip()
        print(f"Book: {book}")