import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets

from qt.connection import Ui_MainWindow
from test import Database


class UiConnection(Ui_MainWindow):
    def __init__(self):
        super().__init__(Ui_MainWindow)

