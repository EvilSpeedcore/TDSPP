from collections import namedtuple


class Element(namedtuple('Element', ['designator', 'component', 'quantity'])):
    """Model of element from BOM-file."""
    def __eq__(self, other):
        return self.component == other.component

    def __ne__(self, other):
        return self is not other
