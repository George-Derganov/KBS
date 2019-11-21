import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from design.login.login import Ui_MainWindow
from work import Work
from statistics import Statistics


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.view()
        self.add_user.clicked.connect(self.append)
        self.delete_user.clicked.connect(self.delete)
        self.select_user.clicked.connect(self.select)
        self.statistics.clicked.connect(self.open_statistics)

    def view(self):
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        # Получили список имен всех пользователей
        names = cur.execute("""SELECT name FROM users""").fetchall()
        # Заполнили ими виджет имен
        for elem in names:
            self.list_users.addItem(elem[0])
        con.close()

    def append(self):
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        # Получили имя, которое ввели в текстовое поле
        # Записали новое значение в базу данных в поле 'name' (Добавили нового пользователя)
        if len(self.name.text()) != 0:
            cur.execute("""INSERT INTO users(name) VALUES('{}')""".format(str(self.name.text()))).fetchall()
        self.list_users.clear()
        self.name.clear()
        con.commit()
        con.close()
        self.view()

    def delete(self):
        if self.list_users.currentItem().text():
            name = self.list_users.currentItem().text()
            valid = QMessageBox.question(self, 'Подтверждение',
                                         'Вы действительно хотите удалить пользователя "' +
                                         name + '"?', QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                con = sqlite3.connect("data_user.db")
                cur = con.cursor()
                # Удаление пользователя по выбранному имени в виджете имен
                cur.execute("""DELETE from users WHERE name = '{}'""".format(name)).fetchall()
                self.list_users.clear()
                con.commit()
                con.close()
                self.view()

    def select(self):
        if self.list_users.currentItem().text():
            # Запуск главного окна программы для выбранного пользователя
            name = self.list_users.currentItem().text()
            global main
            main = Work(name)
            main.show()
            self.setVisible(False)

    def open_statistics(self):
        if self.list_users.currentItem().text():
            # Открытие окна статистики для выбранного пользователя
            name = self.list_users.currentItem().text()
            global st
            st = Statistics(self, name)
            st.show()
            self.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Log = Login()
    Log.show()
    sys.exit(app.exec())
