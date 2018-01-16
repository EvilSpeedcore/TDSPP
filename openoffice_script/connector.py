# -*- coding: cp1251 -*-

import os
from subprocess import Popen


class Connector:
    def __init__(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__)) + '\script.py'
        self.filename = 'office_path.txt'
        self.office_path = self.get_office_path()

    def execute_script(self, filename, doc_type):
        Popen([self.office_path + '\python', self.script_path, filename, doc_type], cwd=self.office_path)

    def connect_to_opened_document(self):
        command = "-accept=socket,host=localhost,port=2002;urp;"
        Popen([self.office_path + '\soffice', command])

    def get_office_path(self):
        if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    return f.read()
        else:
            for root, dirs, files in os.walk('C:/'):
                if 'soffice.exe' in files:
                    with open(self.filename, 'w') as f:
                        f.write(os.path.join(root))
                    return os.path.join(root)
