# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_user_window(object):
    def setupUi(self, add_user_window):
        add_user_window.setObjectName("add_user_window")
        add_user_window.resize(484, 224)
        self.centralwidget = QtWidgets.QWidget(add_user_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 50, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 90, 61, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(80, 50, 131, 20))
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_surname.setGeometry(QtCore.QRect(80, 10, 131, 20))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.lineEdit_middle_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_middle_name.setGeometry(QtCore.QRect(80, 90, 131, 20))
        self.lineEdit_middle_name.setObjectName("lineEdit_middle_name")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(320, 10, 131, 20))
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(320, 50, 131, 20))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.lineEdit_balance = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_balance.setGeometry(QtCore.QRect(320, 90, 131, 20))
        self.lineEdit_balance.setObjectName("lineEdit_balance")
        self.add_user_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_button.setGeometry(QtCore.QRect(370, 130, 81, 41))
        self.add_user_button.setObjectName("add_user_button")
        add_user_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_user_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 21))
        self.menubar.setObjectName("menubar")
        add_user_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_user_window)
        self.statusbar.setObjectName("statusbar")
        add_user_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_user_window)
        QtCore.QMetaObject.connectSlotsByName(add_user_window)

    def retranslateUi(self, add_user_window):
        _translate = QtCore.QCoreApplication.translate
        add_user_window.setWindowTitle(_translate("add_user_window", "MainWindow"))
        self.label.setText(_translate("add_user_window", "surname"))
        self.label_2.setText(_translate("add_user_window", "first_name"))
        self.label_3.setText(_translate("add_user_window", "middle_name"))
        self.label_4.setText(_translate("add_user_window", "phone_number"))
        self.label_5.setText(_translate("add_user_window", "address"))
        self.label_6.setText(_translate("add_user_window", "balance"))
        self.add_user_button.setText(_translate("add_user_window", "add_user"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_user_window = QtWidgets.QMainWindow()
    ui = Ui_add_user_window()
    ui.setupUi(add_user_window)
    add_user_window.show()
    sys.exit(app.exec_())
