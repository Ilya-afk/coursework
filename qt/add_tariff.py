# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_tariff.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_tariff_window(object):
    def setupUi(self, add_tariff_window):
        add_tariff_window.setObjectName("add_tariff_window")
        add_tariff_window.resize(508, 182)
        self.centralwidget = QtWidgets.QWidget(add_tariff_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(110, 50, 131, 20))
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.lineEdit_tariff_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tariff_name.setGeometry(QtCore.QRect(110, 10, 131, 20))
        self.lineEdit_tariff_name.setObjectName("lineEdit_tariff_name")
        self.lineEdit_number_of_free_min = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_of_free_min.setGeometry(QtCore.QRect(360, 50, 131, 20))
        self.lineEdit_number_of_free_min.setObjectName("lineEdit_number_of_free_min")
        self.lineEdit_cost_per_min = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cost_per_min.setGeometry(QtCore.QRect(360, 10, 131, 20))
        self.lineEdit_cost_per_min.setObjectName("lineEdit_cost_per_min")
        self.add_tariff_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_tariff_button.setGeometry(QtCore.QRect(390, 90, 101, 41))
        self.add_tariff_button.setObjectName("add_tariff_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_tariff_period_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tariff_period_id.setGeometry(QtCore.QRect(110, 90, 131, 20))
        self.lineEdit_tariff_period_id.setObjectName("lineEdit_tariff_period_id")
        add_tariff_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_tariff_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        add_tariff_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_tariff_window)
        self.statusbar.setObjectName("statusbar")
        add_tariff_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_tariff_window)
        QtCore.QMetaObject.connectSlotsByName(add_tariff_window)

    def retranslateUi(self, add_tariff_window):
        _translate = QtCore.QCoreApplication.translate
        add_tariff_window.setWindowTitle(_translate("add_tariff_window", "MainWindow"))
        self.label.setText(_translate("add_tariff_window", "tariff_name"))
        self.label_2.setText(_translate("add_tariff_window", "price"))
        self.label_3.setText(_translate("add_tariff_window", "number_of_free_min"))
        self.label_4.setText(_translate("add_tariff_window", "cost_per_min"))
        self.add_tariff_button.setText(_translate("add_tariff_window", "add_tariff"))
        self.label_5.setText(_translate("add_tariff_window", "tariff_period_id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_tariff_window = QtWidgets.QMainWindow()
    ui = Ui_add_tariff_window()
    ui.setupUi(add_tariff_window)
    add_tariff_window.show()
    sys.exit(app.exec_())
