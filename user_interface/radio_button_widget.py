from PyQt5.QtWidgets import QWidget, QLabel, QGroupBox, QRadioButton, QVBoxLayout, QButtonGroup


class RadioButtonWidget(QWidget):
    def __init__(self, label, instruction, button_list):
        super().__init__()
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)

        self.radio_button_list = []
        for button in button_list:
            self.radio_button_list.append(QRadioButton(button))
        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QVBoxLayout()
        self.radio_button_group = QButtonGroup()
        for index, button in enumerate(self.radio_button_list, start=1):
            self.radio_button_layout.addWidget(button)
            self.radio_button_group.addButton(button)
            self.radio_button_group.setId(button, index)

        self.radio_group_box.setLayout(self.radio_button_layout)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)
        self.setLayout(self.main_layout)

    def selected_button(self):
        return self.radio_button_group.checkedId()
