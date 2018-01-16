# -*- coding: cp1251 -*-
from collections import OrderedDict


class Exporter(object):
    def __init__(self, document):
        self.document = document
        self.section = self.document.section
        self.colons = self.document.colons
        self.table_index = self.document.first_table_index
        self.table = self.document.tables.getByIndex(self.table_index)
        self.number_of_rows_on_first_page = self.document.number_of_rows_in_title_block_on_first_page
        self.number_of_rows_on_next_page = self.document.number_of_rows_in_title_block_on_next_pages
        self.first_row_index = self.document.first_row_index
        self.current_row_index = self.first_row_index
        self.number_of_rows = self.table.Rows.getCount()
        self.cell_ranges = OrderedDict()

    def insert_text_in_cell(self, cell_name, text):
        cell = self.table.getCellByName(cell_name)
        cursor = cell.createTextCursor()
        cell.setString(text)

    def is_end_of_the_page(self):
        if self.current_row_index > self.number_of_rows - self.number_of_rows_on_first_page and self.table_index == 0:
            return True
        elif self.current_row_index > self.number_of_rows - self.number_of_rows_on_next_page:
            return True

    def turn_the_page(self):
        self.table_index += 1
        self.table = self.document.tables.getByIndex(self.table_index)
        self.current_row_index = self.first_row_index

    def get_ranges(self):
        return self.cell_ranges

    def export(self):
        if self.section.name:
            self.insert_text_in_cell(self.colons['components'] + str(self.current_row_index), self.section.name)
            self.current_row_index += 1
        for group_name, group in self.section.items():
            self.insert_text_in_cell(self.colons['components'] + str(self.current_row_index), group_name)
            self.current_row_index += 1
            for item in group:
                self.insert_text_in_cell(self.colons['components'] + str(self.current_row_index), item.component)
                self.insert_text_in_cell(self.colons['quantity'] + str(self.current_row_index), item.quantity)
                self.insert_text_in_cell(self.colons['designator'] + str(self.current_row_index), item.designator)
                self.cell_ranges[self.table_index] = self.current_row_index
                row = self.table.Rows.getByIndex(self.current_row_index - 1)
                row.IsAutoHeight = True
                self.current_row_index += 1
                if self.is_end_of_the_page():
                    self.turn_the_page()
            self.current_row_index += 1