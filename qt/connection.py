from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 273)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(60, 50, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 100, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.con_button = QtWidgets.QPushButton(self.centralwidget)
        self.con_button.setGeometry(QtCore.QRect(230, 170, 81, 51))
        self.con_button.setObjectName("con_button")
        self.line_user = QtWidgets.QLineEdit(self.centralwidget)
        self.line_user.setGeometry(QtCore.QRect(130, 60, 181, 31))
        self.line_user.setObjectName("line_user")
        self.line_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_password.setGeometry(QtCore.QRect(130, 110, 181, 31))
        self.line_password.setObjectName("line_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_label.setText(_translate("MainWindow", "user"))
        self.password_label.setText(_translate("MainWindow", "password"))
        self.con_button.setText(_translate("MainWindow", "connect"))

    def add_functions(self):
        self.con_button.clicked.connect(self.connect_to_db)

    def connect_to_db(self):
        print(self.line_user.text(), self.line_password.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
