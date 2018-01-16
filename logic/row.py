# -*- coding: cp1251 -*-


from collections import namedtuple


class Row(namedtuple('Row', ['designator', 'component', 'quantity'])):
    name = None
