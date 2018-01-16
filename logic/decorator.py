import uno
from com.sun.star.awt.FontSlant import ITALIC as FS_ITALIC
from com.sun.star.style.ParagraphAdjust import CENTER, LEFT
from com.sun.star.awt.FontUnderline import SINGLE


class Decorator(object):
    def __init__(self, document, ranges):
        self.document = document
        self.section = self.document.section
        self.ranges = ranges
        self.tables = self.document.tables
        self.table = self.tables.getByIndex(self.document.first_table_index)
        self.colons = self.document.colons
        self.number_of_rows_on_first_page = self.document.first_row_index
        self.property_values = ((FS_ITALIC, LEFT), (FS_ITALIC, CENTER), (FS_ITALIC, LEFT))

    def set_table_by_index(self, index):
        self.table = self.tables.getByIndex(index)

    def calculate_cell_range(self, ranges):
        ranges_names = []
        for colon in self.colons.values():
            range_name = ':'.join([colon + str(self.number_of_rows_on_first_page), colon + str(ranges)])
            ranges_names.append(range_name)
        return ranges_names

    def decorate_section_name(self):
        self.set_table_by_index(self.document.first_table_index)
        cell = self.table.getCellByName(''.join([self.colons['components'], str(self.number_of_rows_on_first_page)]))
        cursor = cell.createTextCursor()
        cursor.ParaAdjust = CENTER
        cursor.CharUnderline = SINGLE

    def decorate(self):
        for table_index in self.ranges.keys():
            self.set_table_by_index(table_index)
            for range_name, value in zip(self.calculate_cell_range(self.ranges[table_index]), self.property_values):
                self.table.getCellRangeByName(range_name).CharPosture = value[0]
                self.table.getCellRangeByName(range_name).ParaAdjust = value[1]
        if self.section.name:
            self.decorate_section_name()
