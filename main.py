import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


class CoffeeTable(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)

        self.set_table()

    def set_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setQuery(QSqlQuery("""SELECT * FROM coffee"""))

        self.tableView.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = CoffeeTable()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
