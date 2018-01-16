# -*- coding: cp1251 -*-


import csv
import os
import re


class Extractor(object):
    def __init__(self, data):
        self.data = data

    def import_data(self, filename):
        if os.path.exists(filename):
            with open(filename) as f:
                f_csv = csv.reader(f, delimiter="\t")
                headings = next(f_csv)
                for row in f_csv:
                    if row:
                        self.data.designators.append(row[0])
                        self.data.components.append(row[1])
                        self.data.quantity.append(row[2])
