# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_tariff_period.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update_tariff_period_window(object):
    def setupUi(self, update_tariff_period_window):
        update_tariff_period_window.setObjectName("update_tariff_period_window")
        update_tariff_period_window.resize(508, 182)
        self.centralwidget = QtWidgets.QWidget(update_tariff_period_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_payment_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_payment_id.setGeometry(QtCore.QRect(110, 10, 131, 20))
        self.lineEdit_payment_id.setObjectName("lineEdit_payment_id")
        self.lineEdit_end_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_end_date.setGeometry(QtCore.QRect(360, 50, 131, 20))
        self.lineEdit_end_date.setObjectName("lineEdit_end_date")
        self.lineEdit_start_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_start_date.setGeometry(QtCore.QRect(360, 10, 131, 20))
        self.lineEdit_start_date.setObjectName("lineEdit_start_date")
        self.update_tariff_period_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_tariff_period_button.setGeometry(QtCore.QRect(370, 90, 121, 41))
        self.update_tariff_period_button.setObjectName("update_tariff_period_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_tariff_period_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tariff_period_id.setGeometry(QtCore.QRect(110, 50, 131, 20))
        self.lineEdit_tariff_period_id.setObjectName("lineEdit_tariff_period_id")
        update_tariff_period_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(update_tariff_period_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        update_tariff_period_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(update_tariff_period_window)
        self.statusbar.setObjectName("statusbar")
        update_tariff_period_window.setStatusBar(self.statusbar)

        self.retranslateUi(update_tariff_period_window)
        QtCore.QMetaObject.connectSlotsByName(update_tariff_period_window)

    def retranslateUi(self, update_tariff_period_window):
        _translate = QtCore.QCoreApplication.translate
        update_tariff_period_window.setWindowTitle(_translate("update_tariff_period_window", "MainWindow"))
        self.label.setText(_translate("update_tariff_period_window", "payment_id"))
        self.label_3.setText(_translate("update_tariff_period_window", "end_date"))
        self.label_4.setText(_translate("update_tariff_period_window", "start_date"))
        self.update_tariff_period_button.setText(_translate("update_tariff_period_window", "update_tariff_period"))
        self.label_5.setText(_translate("update_tariff_period_window", "tariff_period_id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_tariff_period_window = QtWidgets.QMainWindow()
    ui = Ui_update_tariff_period_window()
    ui.setupUi(update_tariff_period_window)
    update_tariff_period_window.show()
    sys.exit(app.exec_())