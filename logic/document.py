from collections import OrderedDict


class Document(object):
    def __init__(self, model, section):
        self.model = model
        self.section = section
        self.tables = model.getTextTables()
        self.first_table_index = 0
        self.first_row_index = 2
        self.number_of_rows_in_title_block_on_first_page = 8
        self.number_of_rows_in_title_block_on_next_pages = 3


class Specification(Document):
    def __init__(self, model, section):
        Document.__init__(self, model, section)
        self.colons = OrderedDict([('components', 'E'), ('quantity', 'F'), ('designator', 'G')])


class ListOfElements(Document):
    def __init__(self, model, section):
        Document.__init__(self, model, section)
        self.colons = OrderedDict([('components', 'B'),('quantity', 'C'),('designator', 'A')])