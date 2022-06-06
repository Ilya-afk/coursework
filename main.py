import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem

from qt.connection import Ui_MainWindow
from qt.appWindow import Ui_AppWindow
from qt.add_user import Ui_add_user_window
from qt.update_user import Ui_update_user_window
from qt.delete_user import Ui_delete_user_window
from qt.add_payment import Ui_add_payment_window
from qt.add_tariff_period import Ui_add_tariff_period_window
from qt.add_tariff import Ui_add_tariff_window
from qt.update_payment import Ui_update_payment_window
from qt.update_tariff_perid import Ui_update_tariff_period_window
from qt.update_tariff import Ui_update_tariff_window
from qt.delete_payment import Ui_delete_payment_window
from qt.delete_tariff_period import Ui_delete_tariff_period_window
from qt.delete_tariff import Ui_delete_tariff_window
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
        self.add_dict = {'user_data': self.add_user_data, 'payment': self.add_payment,
                         'tariff': self.add_tariff, 'tariff_period': self.add_tariff_period}
        self.update_dict = {'user_data': self.update_user_data, 'payment': self.update_payment,
                            'tariff': self.update_tariff, 'tariff_period': self.update_tariff_period}
        self.delete_dict = {'user_data': self.delete_user_data, 'payment': self.delete_payment,
                            'tariff': self.delete_tariff, 'tariff_period': self.delete_tariff_period}

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
        self.add_button.clicked.connect(self.add_dict[self.current_table])
        self.update_button.clicked.connect(self.update_dict[self.current_table])
        self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def set_current_tariff(self):
        self.current_table = 'tariff'
        self.get_tariff()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        self.add_button.clicked.connect(self.add_dict[self.current_table])
        self.update_button.clicked.connect(self.update_dict[self.current_table])
        self.delete_button.clicked.connect(self.delete_dict[self.current_table])

    def set_current_tariff_period(self):
        self.current_table = 'tariff_period'
        self.get_tariff_period()

        self.select_button.clicked.connect(self.get_dict[self.current_table])
        self.add_button.clicked.connect(self.add_dict[self.current_table])
        self.update_button.clicked.connect(self.update_dict[self.current_table])
        self.delete_button.clicked.connect(self.delete_dict[self.current_table])

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
        self.ui = UiAddPaymentWindow(self.user, self.password)
        self.ui.show()

    def update_payment(self):
        self.ui = UiUpdatePaymentWindow(self.user, self.password)
        self.ui.show()

    def delete_payment(self):
        self.ui = UiDeletePaymentWindow(self.user, self.password)
        self.ui.show()

    def add_tariff(self):
        self.ui = UiAddTariffWindow(self.user, self.password)
        self.ui.show()

    def update_tariff(self):
        self.ui = UiUpdateTariffWindow(self.user, self.password)
        self.ui.show()

    def delete_tariff(self):
        self.ui = UiDeleteTariffWindow(self.user, self.password)
        self.ui.show()

    def add_tariff_period(self):
        self.ui = UiAddTariffPeriodWindow(self.user, self.password)
        self.ui.show()

    def update_tariff_period(self):
        self.ui = UiUpdateTariffPeriodWindow(self.user, self.password)
        self.ui.show()

    def delete_tariff_period(self):
        self.ui = UiDeleteTariffPeriodWindow(self.user, self.password)
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
        rows = self.db.get_tariff_period()
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


class UiAddPaymentWindow(QMainWindow, Ui_add_payment_window):
    def __init__(self, user, password):
        super(UiAddPaymentWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.add_payment_button.clicked.connect(self.add_payment)

    def add_payment(self):
        if not self.lineEdit_payment_amount.text().isdigit():
            return None
        if not self.lineEdit_user_data_id.text().isdigit():
            return None
        if not self.lineEdit_tariff_id.text().isdigit():
            return None
        data = [int(self.lineEdit_user_data_id.text()), self.lineEdit_payment_date.text(),
                int(self.lineEdit_payment_amount.text()), int(self.lineEdit_tariff_id.text())]

        self.db.add_payment(*data)


class UiUpdatePaymentWindow(QMainWindow, Ui_update_payment_window):
    def __init__(self, user, password):
        super(UiUpdatePaymentWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.update_payment_button.clicked.connect(self.update_payment)

    def update_payment(self):
        if not self.lineEdit_payment_id.text().isdigit():
            return None

        if not self.lineEdit_payment_amount.text().isdigit():
            payment_amount = None
        else:
            payment_amount = int(self.lineEdit_payment_amount.text())

        if not self.lineEdit_tariff_id.text().isdigit():
            tariff_id = None
        else:
            tariff_id = int(self.lineEdit_tariff_id.text())

        if not self.lineEdit_user_data_id.text().isdigit():
            user_data_id = None
        else:
            user_data_id = int(self.lineEdit_user_data_id.text())

        data = [int(self.lineEdit_payment_id.text()), user_data_id, self.lineEdit_payment_date.text(),
                payment_amount, tariff_id]

        self.db.update_payment(*data)


class UiDeletePaymentWindow(QMainWindow, Ui_delete_payment_window):
    def __init__(self, user, password):
        super(UiDeletePaymentWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.delete_payment_button.clicked.connect(self.delete_payment)

    def delete_payment(self):
        if not self.lineEdit_payment_id.text().isdigit():
            return None

        self.db.delete_payment(int(self.lineEdit_payment_id.text()))


class UiAddTariffWindow(QMainWindow, Ui_add_tariff_window):
    def __init__(self, user, password):
        super(UiAddTariffWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.add_tariff_button.clicked.connect(self.add_tariff)

    def add_tariff(self):
        if not self.lineEdit_price.text().isdigit():
            return None
        if not self.lineEdit_tariff_period_id.text().isdigit():
            return None
        if not self.lineEdit_cost_per_min.text().isdigit():
            return None
        if not self.lineEdit_number_of_free_min.text().isdigit():
            return None
        data = [self.lineEdit_tariff_name.text(), int(self.lineEdit_price.text()),
                int(self.lineEdit_cost_per_min.text()), int(self.lineEdit_number_of_free_min.text()),
                int(self.lineEdit_tariff_period_id.text())]

        self.db.add_tariff(*data)


class UiUpdateTariffWindow(QMainWindow, Ui_update_tariff_window):
    def __init__(self, user, password):
        super(UiUpdateTariffWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.update_tariff_button.clicked.connect(self.update_tariff)

    def update_tariff(self):
        if not self.lineEdit_tariff_id.text().isdigit():
            return None

        if not self.lineEdit_price.text().isdigit():
            price = None
        else:
            price = int(self.lineEdit_price.text())

        if not self.lineEdit_tariff_period_id.text().isdigit():
            tariff_period_id = None
        else:
            tariff_period_id = int(self.lineEdit_tariff_period_id.text())

        if not self.lineEdit_number_of_free_min.text().isdigit():
            number_of_free_min = None
        else:
            number_of_free_min = int(self.lineEdit_number_of_free_min.text())

        if not self.lineEdit_cost_per_min.text().isdigit():
            cost_per_min = None
        else:
            cost_per_min = int(self.lineEdit_cost_per_min.text())

        data = [int(self.lineEdit_tariff_id.text()), self.lineEdit_tariff_name.text(), price, cost_per_min,
                number_of_free_min, tariff_period_id]

        self.db.update_tariff(*data)


class UiDeleteTariffWindow(QMainWindow, Ui_delete_tariff_window):
    def __init__(self, user, password):
        super(UiDeleteTariffWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.delete_tariff_button.clicked.connect(self.delete_tariff)

    def delete_tariff(self):
        if not self.lineEdit_tariff_id.text().isdigit():
            return None

        self.db.delete_tariff(int(self.lineEdit_tariff_id.text()))


class UiAddTariffPeriodWindow(QMainWindow, Ui_add_tariff_period_window):
    def __init__(self, user, password):
        super(UiAddTariffPeriodWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.add_tariff_period_button.clicked.connect(self.add_tariff_period)

    def add_tariff_period(self):
        if not self.lineEdit_payment_id.text().isdigit():
            payment_id = None
        else:
            payment_id = int(self.lineEdit_payment_id.text())
        data = [payment_id, self.lineEdit_start_date.text(), self.lineEdit_end_date.text()]

        self.db.add_tariff_period(*data)


class UiUpdateTariffPeriodWindow(QMainWindow, Ui_update_tariff_period_window):
    def __init__(self, user, password):
        super(UiUpdateTariffPeriodWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.update_tariff_period_button.clicked.connect(self.update_tariff_period)

    def update_tariff_period(self):
        if not self.lineEdit_tariff_period_id.text().isdigit():
            return None

        if not self.lineEdit_payment_id.text().isdigit():
            payment_id = None
        else:
            payment_id = int(self.lineEdit_payment_id.text())

        data = [int(self.lineEdit_tariff_period_id.text()), payment_id, self.lineEdit_start_date.text(),
                self.lineEdit_end_date.text()]

        self.db.update_tariff_period(*data)


class UiDeleteTariffPeriodWindow(QMainWindow, Ui_delete_tariff_period_window):
    def __init__(self, user, password):
        super(UiDeleteTariffPeriodWindow, self).__init__()
        self.setupUi(self)

        self.user = user
        self.password = password

        self.db = Database()
        self.db.connection(self.user, self.password)

        self.delete_tariff_period_button.clicked.connect(self.delete_tariff_period)

    def delete_tariff_period(self):
        if not self.lineEdit_tariff_period_id.text().isdigit():
            return None

        self.db.delete_tariff_period(int(self.lineEdit_tariff_period_id.text()))


if __name__ == '__main__':
    app = QApplication([])
    ui = UiConnection()
    ui.show()
    app.exec()
