from collections import OrderedDict


class Section(OrderedDict):
    def __init__(self):
        super(Section, self).__init__()
        self.name = None

