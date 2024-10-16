'''
WRITE A LIBRARY CLASS WITH NO_OF_BOOKS AND BOOKS AS TWO INSTANCE VARIABLES.WRITE A POGRAM TO CREATE A LIBRARY FROM THIS
LIBRARY CLASS AND SHOW HOW YOU CAN PRINT ALL BOOKS , ADD A BOOK AND GET THE NUMBER OF BOOKS USING DIFFERENT METHODS.
SHOW THAT YOUR POGRAM DOESNT PERSIST THE BOOKS and BOOK name AFTER THE POGRAM IS STOPPED
'''

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        self.no_of_books+=1
    def display_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books:
                print(book)
    def get_no_of_books(self):
        return self.no_of_books
library=Library()

library.add_book("SN DEY MATHEMATICS")
library.add_book("CONCEPTS OF PHYSICS")
library.add_book("CONCISE CHEMISTRY")

print("Books in Library:-")
library.display_books()
print("Number of books:-",library.get_no_of_books())


print("Books in Library:-")
library.display_books()
print("Number of books:-")
library.get_no_of_books()