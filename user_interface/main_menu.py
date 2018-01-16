# -*- coding: cp1251 -*-


import os
from PyQt5.QtWidgets import *
from openoffice_script.connector import Connector
from user_interface.radio_button_widget import RadioButtonWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.init_interface()
        self.create_select_type_layout()
        self.connector = Connector()

    def init_interface(self):
        open_output_file = QAction('Open', self)
        open_output_file.triggered.connect(self.open_openoffice_writer)
        open_file = QAction('Open', self)
        open_file.triggered.connect(self.show_input_file_dialog)

        bar = self.menuBar()
        input_file = bar.addMenu('Input file')
        input_file.addAction(open_file)
        output_file = bar.addMenu('Output file')
        output_file.addAction(open_output_file)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('TDSPP')
        self.show()

    def create_select_type_layout(self):
        self.radio_buttons = RadioButtonWidget('Type selection', 'Select type', ('Specification', 'List of elements'))
        instantiate_button = QPushButton('Export')

        initial_layout = QVBoxLayout()
        initial_layout.addWidget(self.radio_buttons)
        initial_layout.addWidget(instantiate_button)

        select_type_widget = QWidget()
        select_type_widget.setLayout(initial_layout)
        self.setCentralWidget(select_type_widget)

        instantiate_button.clicked.connect(self.create_document)

    def create_document(self):
        document_type = self.radio_buttons.selected_button()
        self.connector.execute_script(self.filename, str(document_type))

    def open_openoffice_writer(self):
        try:
            self.connector.connect_to_opened_document()
        except FileNotFoundError as e:
            os.remove(self.connector.filename)
            QMessageBox.about(self, "Error", f'{e}. Перезапустите программу.')

    def show_input_file_dialog(self):
        self.filename = QFileDialog.getOpenFileName(parent=self, caption='Open file')[0]
