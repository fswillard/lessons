class Book:
  def __init__(self, tittle):
    self.__tittle = tittle

  def getTittle(self):
    return self.__tittle

  def setTittle(self, tittle):
    self.__tittle = tittle

  def read(self):
    return "I am reading {}".format(self.getTittle())

  @classmethod

  def all(cls):
    return 'List all books'
