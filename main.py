import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem

from qt.connection import Ui_MainWindow
from qt.appWindow import Ui_AppWindow
from qt.add_user import Ui_add_user_window
from qt.update_user import Ui_update_user_window
from qt.delete_user import Ui_delete_user_window
from test import Database, try_connection

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
    def __init__(self, user, password, current_table='user_data'):
        super(UiDBWindow, self).__init__()
        self.setupUi(self)
        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.current_table = current_table

        self.get_dict = {'user_data': self.get_user_data, 'payment': self.get_payment,
                         'tariff': self.get_tariff, 'tariff_period': self.get_tariff_period}
        self.add_dict = {'user_data': self.add_user_data}
        self.update_dict = {'user_data': self.update_user_data}
        self.delete_dict = {'user_data': self.delete_user_data}

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        self.add_button.clicked.connect(self.add_dict[self.current_table])
        self.update_button.clicked.connect(self.update_dict[self.current_table])
        self.delete_button.clicked.connect(self.delete_dict[self.current_table])

        self.user_data_button.clicked.connect(self.set_current_user)
        self.payment_button.clicked.connect(self.set_current_payment)
        self.tariff_button.clicked.connect(self.set_current_tariff)
        self.tariff_period_button.clicked.connect(self.set_current_tariff_period)

    def set_current_user(self):
        self.current_table = 'user_data'
        self.get_user_data()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        self.add_button.clicked.connect(self.add_dict[self.current_table])
        self.update_button.clicked.connect(self.update_dict[self.current_table])
        self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def set_current_payment(self):
        self.current_table = 'payment'
        self.get_payment()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        #self.add_button.clicked.connect(self.add_dict[self.current_table])
        #self.update_button.clicked.connect(self.update_dict[self.current_table])
        #self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def set_current_tariff(self):
        self.current_table = 'tariff'
        self.get_tariff()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        #self.add_button.clicked.connect(self.add_dict[self.current_table])
        #self.update_button.clicked.connect(self.update_dict[self.current_table])
        #self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def set_current_tariff_period(self):
        self.current_table = 'tariff_period'
        self.get_tariff_period()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        #self.add_button.clicked.connect(self.add_dict[self.current_table])
        #self.update_button.clicked.connect(self.update_dict[self.current_table])
        #self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def get_payment(self):
        rows = self.db.get_payment()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setHorizontalHeaderLabels(['payment_id', 'user_data_id', 'payment_date', 'payment_amount',
                                                    'tariff_id'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                newitem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newitem)

    def add_payment(self):
        self.ui = UiAddUserWindow(self.user, self.password)
        self.ui.show()

    def update_payment(self):
        self.ui = UiUpdateUserWindow(self.user, self.password)
        self.ui.show()

    def delete_payment(self):
        self.ui = UiDeleteUserWindow(self.user, self.password)
        self.ui.show()

    def add_tariff(self):
        self.ui = UiAddUserWindow(self.user, self.password)
        self.ui.show()

    def update_tariff(self):
        self.ui = UiUpdateUserWindow(self.user, self.password)
        self.ui.show()

    def delete_tariff(self):
        self.ui = UiDeleteUserWindow(self.user, self.password)
        self.ui.show()

    def add_tariff_period(self):
        self.ui = UiAddUserWindow(self.user, self.password)
        self.ui.show()

    def update_tariff_period(self):
        self.ui = UiUpdateUserWindow(self.user, self.password)
        self.ui.show()

    def delete_tariff_period(self):
        self.ui = UiDeleteUserWindow(self.user, self.password)
        self.ui.show()

    def get_tariff(self):
        rows = self.db.get_tariff()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setHorizontalHeaderLabels(['tariff_id', 'tariff_name', 'price', 'cost_per_min',
                                                    'number_of_free_min', 'tariff_period_id'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                newitem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newitem)

    def get_tariff_period(self):
        rows = self.db.get_tariff()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setHorizontalHeaderLabels(['tariff_period_id', 'payment_id', 'start_date', 'end_date'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                newitem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newitem)

    def get_user_data(self):
        rows = self.db.get_user_data()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setHorizontalHeaderLabels(['user_data_id', 'surname', 'first_name', 'middle_name',
                                                    'phone_number', 'address', 'balance'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                newitem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newitem)

    def add_user_data(self):
        self.ui = UiAddUserWindow(self.user, self.password)
        self.ui.show()

    def update_user_data(self):
        self.ui = UiUpdateUserWindow(self.user, self.password)
        self.ui.show()

    def delete_user_data(self):
        self.ui = UiDeleteUserWindow(self.user, self.password)
        self.ui.show()


class UiAddUserWindow(QMainWindow, Ui_add_user_window):
    def __init__(self, user, password):
        super(UiAddUserWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.add_user_button.clicked.connect(self.add_user)

    def add_user(self):
        if not self.lineEdit_balance.text().isdigit():
            return None
        data = [self.lineEdit_surname.text(), self.lineEdit_first_name.text(), self.lineEdit_middle_name.text(),
                self.lineEdit_phone_number.text(), self.lineEdit_address.text(), int(self.lineEdit_balance.text())]

        self.db.add_user(*data)


class UiUpdateUserWindow(QMainWindow, Ui_update_user_window):
    def __init__(self, user, password):
        super(UiUpdateUserWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.update_user_button.clicked.connect(self.update_user)

    def update_user(self):
        if not self.lineEdit_user_id.text().isdigit():
            return None

        if not self.lineEdit_balance.text().isdigit():
            balance = None
        else:
            balance = int(self.lineEdit_balance.text())

        data = [int(self.lineEdit_user_id.text()), self.lineEdit_surname.text(), self.lineEdit_first_name.text(),
                self.lineEdit_middle_name.text(), self.lineEdit_phone_number.text(),
                self.lineEdit_address.text(), balance]

        print(data)

        self.db.update_user(*data)


class UiDeleteUserWindow(QMainWindow, Ui_delete_user_window):
    def __init__(self, user, password):
        super(UiDeleteUserWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.delete_user_button.clicked.connect(self.delete_user)

    def delete_user(self):
        if not self.lineEdit_user_id.text().isdigit():
            return None

        self.db.delete_user(int(self.lineEdit_user_id.text()))


if __name__ == '__main__':
    app = QApplication([])
    ui = UiConnection()
    ui.show()
    app.exec()
