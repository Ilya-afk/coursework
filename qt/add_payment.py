# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_payment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_payment_window(object):
    def setupUi(self, add_payment_window):
        add_payment_window.setObjectName("add_payment_window")
        add_payment_window.resize(490, 178)
        self.centralwidget = QtWidgets.QWidget(add_payment_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_payment_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_payment_date.setGeometry(QtCore.QRect(110, 50, 131, 20))
        self.lineEdit_payment_date.setObjectName("lineEdit_payment_date")
        self.lineEdit_user_data_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_user_data_id.setGeometry(QtCore.QRect(110, 10, 131, 20))
        self.lineEdit_user_data_id.setObjectName("lineEdit_user_data_id")
        self.lineEdit_payment_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_payment_amount.setGeometry(QtCore.QRect(350, 50, 131, 20))
        self.lineEdit_payment_amount.setObjectName("lineEdit_payment_amount")
        self.lineEdit_tariff_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tariff_id.setGeometry(QtCore.QRect(350, 10, 131, 20))
        self.lineEdit_tariff_id.setObjectName("lineEdit_tariff_id")
        self.add_payment_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_payment_button.setGeometry(QtCore.QRect(400, 90, 81, 41))
        self.add_payment_button.setObjectName("add_payment_button")
        add_payment_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_payment_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        add_payment_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_payment_window)
        self.statusbar.setObjectName("statusbar")
        add_payment_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_payment_window)
        QtCore.QMetaObject.connectSlotsByName(add_payment_window)

    def retranslateUi(self, add_payment_window):
        _translate = QtCore.QCoreApplication.translate
        add_payment_window.setWindowTitle(_translate("add_payment_window", "MainWindow"))
        self.label.setText(_translate("add_payment_window", "user_data_id"))
        self.label_2.setText(_translate("add_payment_window", "payment_date"))
        self.label_3.setText(_translate("add_payment_window", "payment_amount"))
        self.label_4.setText(_translate("add_payment_window", "tariff_id"))
        self.add_payment_button.setText(_translate("add_payment_window", "add_payment"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_payment_window = QtWidgets.QMainWindow()
    ui = Ui_add_payment_window()
    ui.setupUi(add_payment_window)
    add_payment_window.show()
    sys.exit(app.exec_())
