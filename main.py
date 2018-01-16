import sys
from PyQt5.QtWidgets import QApplication
from user_interface.main_menu import MainWindow
from openoffice_script.connector import Connector

connector = Connector()
sys.path.insert(0, connector.get_office_path())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
