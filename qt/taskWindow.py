# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_taskWindow(object):
    def setupUi(self, taskWindow):
        taskWindow.setObjectName("taskWindow")
        taskWindow.resize(745, 520)
        self.centralwidget = QtWidgets.QWidget(taskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 0, 641, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(640, 420, 101, 51))
        self.backButton.setObjectName("backButton")
        self.task3aButton = QtWidgets.QPushButton(self.centralwidget)
        self.task3aButton.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.task3aButton.setObjectName("task3aButton")
        self.task3fButton = QtWidgets.QPushButton(self.centralwidget)
        self.task3fButton.setGeometry(QtCore.QRect(0, 160, 101, 41))
        self.task3fButton.setObjectName("task3fButton")
        self.task3eButton = QtWidgets.QPushButton(self.centralwidget)
        self.task3eButton.setGeometry(QtCore.QRect(0, 120, 101, 41))
        self.task3eButton.setObjectName("task3eButton")
        self.task3dButton = QtWidgets.QPushButton(self.centralwidget)
        self.task3dButton.setGeometry(QtCore.QRect(0, 80, 101, 41))
        self.task3dButton.setObjectName("task3dButton")
        self.task3cButton = QtWidgets.QPushButton(self.centralwidget)
        self.task3cButton.setGeometry(QtCore.QRect(0, 40, 101, 41))
        self.task3cButton.setObjectName("task3cButton")
        taskWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(taskWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
        self.menubar.setObjectName("menubar")
        taskWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(taskWindow)
        self.statusbar.setObjectName("statusbar")
        taskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(taskWindow)
        QtCore.QMetaObject.connectSlotsByName(taskWindow)

    def retranslateUi(self, taskWindow):
        _translate = QtCore.QCoreApplication.translate
        taskWindow.setWindowTitle(_translate("taskWindow", "MainWindow"))
        self.backButton.setText(_translate("taskWindow", "назад"))
        self.task3aButton.setText(_translate("taskWindow", "3a"))
        self.task3fButton.setText(_translate("taskWindow", "3f"))
        self.task3eButton.setText(_translate("taskWindow", "3e"))
        self.task3dButton.setText(_translate("taskWindow", "3d"))
        self.task3cButton.setText(_translate("taskWindow", "3c"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_payment_window = QtWidgets.QMainWindow()
    ui = Ui_taskWindow()
    ui.setupUi(update_payment_window)
    update_payment_window.show()
    sys.exit(app.exec_())
