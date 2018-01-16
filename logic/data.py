# -*- coding: cp1251 -*-


class Data(object):
    """Storing imported data from BOM-file."""
    def __init__(self):
        self.designators, self.components, self.quantity = [], [], []

    def __iter__(self):
        return iter(zip(self.designators, self.components, self.quantity))


