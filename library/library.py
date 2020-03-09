from book import Book


class Library:

    def __init__(self):
        self.__dict__ = {'Chuk Palahniuk': 'Fight club'}

    def print_info(self):
        print(self.__dict__)

    def readers_list(self):
        pass

    def add_book(self):
        pass

    def take_book(self):
        pass

    def retake_book(self):
        pass