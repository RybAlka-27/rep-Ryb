from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery
import sys
import dbApp
import dbconnection
import dbBasket
import dbCustomer


class Login(QtWidgets.QMainWindow, dbconnection.LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupButton.clicked.connect(lambda: self.connection(self.nameEdit.text(), self.loginEdit.text(), self.passwordEdit.text()))
        self.loginEdit.setText("employee")
        self.passwordEdit.setText("user")
        self.nameEdit.setText("postgres")

    def connection(self, name_, user_, password_):
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName("localhost")  
        self.db.setPort(5432)
        self.db.setDatabaseName(name_)  
        self.db.setUserName(user_)  
        self.db.setPassword(password_) 

        if self.db.open():
            print("Connected")
            self.closeApp()
        else:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("Неправильниый логин или пароль")
            self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBox.show()

    def closeApp(self):
        self.close()
        dbconnection.LoginWindow = App(self.db).show()
        # if self.loginEdit.text() == "administrator":
        #     dbconnection.LoginWindow = App(self.db).show()
        # else:
        #     pass
        #     dbconnection.LoginWindow = Customer(self.db).show()


class Customer(QtWidgets.QMainWindow, dbCustomer.Ui_mainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi(self)
        self.setupButton.clicked.connect(lambda: self.onClick())
        
    def onClick(self):
        if self.accountEdit.text().isdigit():
            self.addCustomer()
            self.close()
            App(self.db).show()
        else:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("В поле 'На счету' должны быть только числа")
            self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.msgBox.show()
    
    def addCustomer(self):
        string1 = 'INSERT INTO "Store".customer (name, address, phone, email, wallet)'
        string2 =   "VALUES ('" + str(self.nameEdit.text()) + "', '" + str(self.addressEdit.text()) + "', '" + str(self.numberEdit.text()) + "', '" + str(self.emailEdit.text()) + \
                "'," + str(self.accountEdit.text()) + ");"
        print(string1 + string2)
        QSqlQuery(string1 + string2, self.db)


class App(QtWidgets.QMainWindow, dbApp.Ui_MainWindow):
    def __init__(self, db, account=''):
        super().__init__()
        self.db = db
        self.setupUi(self)
        if self.db.userName() == "employee":
            self.add_Data.setEnabled(False)
            self.delete_Data.setEnabled(False)
        self._id = 0
        self.account.setText(account)
        self.getData()
        self.loginMenu.triggered.connect(lambda: self.relogin())
        self.basketMenu.triggered.connect(lambda: self.openBasket())
        self.customerMenu.triggered.connect(lambda: self.openCustomer())
        self.get_Data.clicked.connect(lambda: self.getData())
        self.add_Data.clicked.connect(lambda: self.addData())
        self.delete_Data.clicked.connect(lambda: self.deleteData())
        self.tableView.clicked.connect(lambda: self.onClick())
        self.toBasket.clicked.connect(lambda: self.makingBasket())
        self.comboBox.currentIndexChanged.connect(lambda: self.getData(4))

    def makingBasket(self):
        index = (self.tableView.selectionModel().currentIndex())
        id_prod = index.row() + 1
        if self.comboBox.currentText() == "product":
            QSqlQuery('INSERT INTO "Store".order_product (product_id) VALUES (' + str(id_prod) + ')', self.db)

    def onClick(self):
        index = (self.tableView.selectionModel().currentIndex())
        self._id = index.row()
        self.value = index.sibling(index.row(),5).data()
        if self.comboBox.currentText() == "customer":
            self.account.setText(str(self.value))

    def openBasket(self):
        Basket(self.db, self.account.text(), self._id).show()

    def openCustomer(self):
        Customer(self.db).show()
        self.close()
        self.getData()

    def relogin(self):
        self.close()
        dbApp.Ui_MainWindow = Login().show() 

    def getData(self):
        self.model = QSqlTableModel()
        self.comboTable = self.comboBox.currentText()
        self.model.setTable('"Store".' + self.comboTable)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.sortByColumn(0, QtCore.Qt.SortOrder())
        self.tableView.show()

    def deleteData(self):
        indices = self.tableView.selectionModel().selectedRows() 
        for index in sorted(indices):
            self.model.removeRow(index.row())
        self.getData()    
        
    def addData(self):
        self.model.insertRow(self.model.rowCount())
        self.model.OnRowChange


class Basket(QtWidgets.QMainWindow, dbBasket.Ui_MainWindow):
    def __init__(self, db, account, _id):
        super().__init__()
        self.db = db
        self.account = account
        self.id = _id + 1
        self.setupUi(self)
        self.func()
        self.view()
        self.apply.clicked.connect(lambda: self.transaction())
        
    def transaction(self):
        query = 'BEGIN; \
                    UPDATE "Store".customer SET wallet = (wallet - "Store".get_profit()) where id = ' + str(self.id) + '; \
                 END;'
        QSqlQuery(query, self.db)
        query = QSqlQuery('SELECT wallet FROM "Store".customer WHERE id = ' + str(self.id) + ';', self.db)
        while (query.next()):
            self.onAccount.setText(str(query.value(0)))
        self.apply.setEnabled(False)
        self.purchase.setText("Покупка успешно завершена")
        App(self.db).getData()

    def view(self):
        self.model = QSqlTableModel()
        self.model.setTable('"Store".view_name')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.show()
        self.onAccount.setText(self.account)

    def func(self):
        query = QSqlQuery('SELECT "Store".get_profit();', self.db)
        while (query.next()):
            self.sum.setText(query.value(0))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login()
    ui.show()
    sys.exit(app.exec_())