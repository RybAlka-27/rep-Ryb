# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbconnection.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from psycopg2 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Подключение")
        MainWindow.resize(350, 200)
        MainWindow.setMinimumSize(QtCore.QSize(350, 200))
        MainWindow.setMaximumSize(QtCore.QSize(350, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setupButton = QtWidgets.QPushButton(self.centralwidget)
        self.setupButton.setGeometry(QtCore.QRect(100, 150, 150, 30))
        self.loginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginEdit.setGeometry(QtCore.QRect(100, 30, 211, 22))
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(100, 70, 211, 22))
        self.passwordEdit.setObjectName("passwordEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(100, 120, 211, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.loginLabel.setObjectName("loginLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 120, 61, 21))
        self.nameLabel.setObjectName("nameLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDatabase = QtWidgets.QAction(MainWindow)
        self.actionDatabase.setObjectName("actionDatabase")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Подключение"))
        self.setupButton.setText(_translate("MainWindow", "OK"))
        self.loginLabel.setText(_translate("MainWindow", "Логин"))
        self.passwordLabel.setText(_translate("MainWindow", "Пароль"))
        self.nameLabel.setText(_translate("MainWindow", "Название"))
        self.actionDatabase.setText(_translate("MainWindow", "Database"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())