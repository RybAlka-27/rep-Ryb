# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(350, 300)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.name.setObjectName("name")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.address.setObjectName("address")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.number.setObjectName("number")
        self.lemail = QtWidgets.QLabel(self.centralwidget)
        self.lemail.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.lemail.setObjectName("lemail")
        self.account = QtWidgets.QLabel(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(20, 190, 47, 13))
        self.account.setObjectName("account")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(100, 30, 200, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(100, 70, 200, 20))
        self.addressEdit.setObjectName("addressEdit")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(100, 110, 200, 20))
        self.numberEdit.setObjectName("numberEdit")
        self.emailEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailEdit.setGeometry(QtCore.QRect(100, 150, 200, 20))
        self.emailEdit.setObjectName("emailEdit")
        self.accountEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.accountEdit.setGeometry(QtCore.QRect(100, 190, 200, 20))
        self.accountEdit.setObjectName("accountEdit")
        self.setupButton = QtWidgets.QPushButton(self.centralwidget)
        self.setupButton.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.setupButton.setObjectName("setupButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Регистрицая покупателя"))
        self.name.setText(_translate("mainWindow", "Имя"))
        self.address.setText(_translate("mainWindow", "Адрес"))
        self.number.setText(_translate("mainWindow", "Номер"))
        self.lemail.setText(_translate("mainWindow", "email"))
        self.account.setText(_translate("mainWindow", "На счету"))
        self.setupButton.setText(_translate("mainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
