import sys

import psycopg2
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from qt.connection import Ui_MainWindow
from qt.appWindow import Ui_AppWindow
from test import Database, try_connection

import inspect


class UiConnection(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UiConnection, self).__init__()
        self.setupUi(self)

        self.con_button.clicked.connect(self.connect_to_db)

    def connect_to_db(self):
        if try_connection(self.line_user.text(), self.line_password.text()):
            # вызвать новое окно и передать туда юзер и пароль
            self.ui = UiDBWindow(self.line_user.text(), self.line_password.text())
            self.ui.show()
            ui.close()
        else:
            print('error')


class UiDBWindow(QMainWindow, Ui_AppWindow):
    loc = locals()
    def __init__(self, user, password):
        super(UiDBWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.current_table = 'user_data'

        func = f'get_{self.current_table}'
        method_list = [func for func in dir(UiDBWindow) if callable(getattr(UiDBWindow, func))]
        print(self.__dict__)
        print(UiDBWindow.loc[func])
        print(self.get_user_data)
        # self.select_button.clicked.connect(UiDBWindow.loc[func](self))
        self.select_button.clicked.connect(self.get_user_data)

    def get_user_data(self):
        self.db.get_user_data()


if __name__ == '__main__':
    app = QApplication([])
    ui = UiConnection()
    ui.show()
    app.exec()
