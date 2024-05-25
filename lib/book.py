#!/usr/bin/env python3

class Book:
    def __init__(self, arg_title, arg_page_count):
        self._title = arg_title
        self._page_count = arg_page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self.page_count = value
        else: print('page_count must be an integer')

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')
