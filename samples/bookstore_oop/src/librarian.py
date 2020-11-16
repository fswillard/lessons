from src import Book

class Librarian:
  @classmethod

  def read(cls, book: Book):
    print(book.read())
