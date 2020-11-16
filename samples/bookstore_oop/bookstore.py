# from src import Book
# from src import Magazine
# from src import Librarian
from src import *

book = Book('Game of Thrones') # Initialize a new Book
print(book.read()) # Read the book

# print(book.__tittle) # Can't read a private attribute
book.__tittle = 'Dracarys' # Try to change the book tittle
print(book.read()) # Stills the same tittle

book.setTittle('Dracarys') # Change the book tittle
print(book.read()) # Read the book with new tittle

print(Book.all()) # Return all books - class method

print('---')

magazine = Magazine('Woman\'s Day') # Initialize a new Magazine (inherited from Book)

print(magazine.read()) # Read the magazine
print(magazine.gossip())  # Gossip about the magazine
print(Magazine.all())  # Return all magazines - class method

print('---')

Librarian.read(book) # Read book using Librarian
Librarian.read(magazine) # Read magazine using Librarian
