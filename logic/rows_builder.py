from logic.row import Row


class RowsBuilder(object):
    """Class, which is used for making rows of specification from elements."""
    def __init__(self, elements):
        """

        :param elements: list of Elements objects.
        """
        self.elements = elements

    def make_rows_for_specification(self):
        """

        :return: list of Rows objects.
        """
        rows = []
        for this_index, this_item in enumerate(self.elements):
            quantity = 1
            designators = []
            if this_item:
                designators.append(this_item.designator)
                for next_index in range(this_index+1, len(self.elements)):
                    next_item = self.elements[next_index]
                    if next_item:
                        if this_item == next_item:
                            quantity += 1
                            designators.append(next_item.designator)
                            self.elements[next_index] = ''
                row = Row(', '.join(designators), ' '.join(this_item.component.split()[1:]), quantity)
                row.name = this_item.component.split()[0]
                rows.append(row)
        return rows

    def make_rows_for_list_of_elements(self):
        """

        :return: list of Rows objects.
        """
        rows = []
        for this_index, this_item in enumerate(self.elements):
            quantity = 1
            designators = []
            if this_item:
                designators.append(this_item.designator)
                for next_index, next_item in enumerate(self.elements):
                    if next_item:
                        last_character_1 = designators[-1][-1]
                        last_character_2 = next_item.designator[-1:]
                        if this_item == next_item and int(last_character_2) - int(last_character_1) == 1:
                            quantity += 1
                            designators.append(next_item.designator)
                            self.elements[next_index] = ''
                if len(designators) > 2:
                    designators = [designators[0], designators[-1]]
                    row = Row('...'.join(designators), ' '.join(this_item.component.split()[1:]), quantity)
                else:
                    row = Row(', '.join(designators), ' '.join(this_item.component.split()[1:]), quantity)
                row.name = this_item.component.split()[0]
                rows.append(row)
        return rows




