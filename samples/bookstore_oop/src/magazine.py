from src import Book

class Magazine(Book):
  def __init__(self, tittle):
    super().__init__(tittle)

  def gossip(self):
    return "I am gossiping about {}..".format(self.getTittle())

  @classmethod

  def all(cls):
    return 'List all magazines'
