class Book:
    def __init__(self, author, name):
        self.__dict__ = author
        self.__dict__ = name
