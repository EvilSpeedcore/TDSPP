# -*- coding: cp1251 -*-

from itertools import groupby
from logic.data import Data
from logic.element import Element
from logic.rows_builder import RowsBuilder
from logic.section import Section
from logic.extractor import Extractor


def make_elements(filename):
    data = Data()
    extractor = Extractor(data)
    extractor.import_data(filename)
    elements = list(map(lambda x: Element(*x), data))
    return elements


def make_section_for_specification(elements):
    row_builder = RowsBuilder(elements)
    rows = row_builder.make_rows_for_specification()
    product_section = Section()
    product_section.name = 'Прочие изделия'
    for key, group in groupby(rows, lambda x: x.name):
        [product_section.setdefault(key + 'ы', []).append(row) for row in group]
    return product_section


def make_section_for_list_of_elements(elements):
    row_builder = RowsBuilder(elements)
    rows = row_builder.make_rows_for_list_of_elements()
    product_section = Section()
    for key, group in groupby(rows, lambda x: x.name):
        [product_section.setdefault(key + 'ы', []).append(row) for row in group]
    return product_section


