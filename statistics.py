import sqlite3
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMainWindow
from design.statistics.statistics import Ui_MainWindow


class Statistics(QMainWindow, Ui_MainWindow):
    def __init__(self, parent, name):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.name_user = name
        self.view()

    def view(self):
        # Вывод статистики пользователя из базы данных по его имени
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        info = cur.execute("""SELECT * FROM users WHERE name = '{}'""".format(str(self.name_user))).fetchall()[0]
        con.close()
        self.wrongs_n = info[1]
        self.rights_n = info[2]
        self.time_n = info[3]

        self.print_name()
        self.print_time()
        self.print_all()
        self.print_wrongs()
        self.print_v()

    def print_name(self):
        self.name.setText(f'Статистика пользователя "{self.name_user}":')

    def print_time(self):
        self.time.setText(f'Времени проведено за печатанием: {self.time_n} ')

    def print_all(self):
        self.all.setText(f'За это время натыкано: {str(self.wrongs_n + self.rights_n)} букв')

    def print_wrongs(self):
        if self.wrongs_n + self.rights_n == 0:
            self.error = 0
        else:
            self.error = self.wrongs_n / (self.wrongs_n + self.rights_n) * 100
        self.wrongs.setText(f'Процент ошибок составляет: {str(int(self.error))}%')

    def print_v(self):
        if self.time_n == 0:
            self.V = 0
        else:
            self.V = (self.rights_n / self.time_n) * 60
        self.v_sr.setText(f'Средняя скорость печатания: {str(int(self.V))} зн/мин')

    def keyPressEvent(self, e):  # Обработчик событий
        if e.key() == Qt.Key_Escape:
            self.parent.setEnabled(True)
            self.close()

    def closeEvent(self, e):
        # Закрытие окна
        self.parent.setEnabled(True)
        self.close()
