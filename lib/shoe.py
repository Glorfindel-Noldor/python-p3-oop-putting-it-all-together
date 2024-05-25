#!/usr/bin/env python3

class Shoe:
    def __init__(self, arg_brand, arg_size):
        self.brand = arg_brand
        self._size = arg_size

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else: print('size must be an integer')
    def cobble(self):
        """says that the shoe has ben repaired"""
        print('Your shoe is as good as new!')
        self.condition = 'New'
