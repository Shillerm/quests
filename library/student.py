from book import Book


class Student:
    def __init__(self, name, books):
        self.name = name
        self.book = books

    def take_book(self, book):
        pass
        # print(f'Take book {self.book.author}: {self.book.name}')

    def print_info(self):
        print(f'Name: {self.name} \nBooks: {self.book}')
