import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dbconnection import *

def connetcion(_user, _password):
    try:
        con = psycopg2.connect(
            database="postgres", 
            user=_user, 
            password=_password, 
            host="localhost", 
            port="5432"
        )
        cursor = con.cursor()

        print("Информация о сервере PostgreSQL")
        print(con.get_dsn_parameters(), "\n")
        print()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

if __name__ == "__main__":
    # connect_to_db()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupButton.clicked.connect(connetcion(ui.loginEdit.text, ui.passwordEdit.text))

    MainWindow.show()
    sys.exit(app.exec_())
