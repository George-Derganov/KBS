import sqlite3
from PyQt5.Qt import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from design.result.result import Ui_MainWindow


class Result(QMainWindow, Ui_MainWindow):
    def __init__(self, parent, name, *args):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.name = name
        self.args = args[:]
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Убрать рамку и заголовок окна
        self.time_print()
        self.written_print()
        self.wrongs_print()
        self.v_print()
        self.btn_finish.clicked.connect(self.close_program)
        if args[-1] is False:
            self.btn_continue.clicked.connect(self.continue_program)
        else:
            self.btn_continue.setText('Сохранить результат')
            self.btn_continue.clicked.connect(self.update_db)

    def update_db(self):
        valid = QMessageBox.question(self, 'Подтверждение',
                                     "Вы действительно хотите сохранить результат?",
                                     QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.update_wrong()
            self.update_right()
            self.update_time()

    def update_wrong(self):
        #  Обновление поля неправильных букв в базе данных для авторизированного пользователя
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        cur.execute("""Update users set wrongs = wrongs + {} WHERE name = '{}'""".format(int(self.args[2]),
                                                                                         self.name)).fetchall()
        con.commit()
        con.close()

    def update_right(self):
        #  Обновление поля правильных букв в базе данных для авторизированного пользователя
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        cur.execute("""Update users set rights = rights + {} WHERE name = '{}'""".format(int(self.args[1]),
                                                                                         self.name)).fetchall()
        con.commit()
        con.close()

    def update_time(self):
        #  Обновление поля времени в базе данных для авторизированного пользователя
        con = sqlite3.connect("data_user.db")
        cur = con.cursor()
        cur.execute(
            """Update users set time = time + {} WHERE name = '{}'""".format(int(self.args[0]), self.name)).fetchall()
        con.commit()
        con.close()

    def keyPressEvent(self, e):  # Обработчик событий
        if e.key() == Qt.Key_Escape:
            if self.args[-1] is False:
                self.continue_program()
            else:
                self.close_program()

    def time_print(self):
        # Вывод времени
        self.time_p.setText(
            'Время прошло: ' + str(int(self.args[0]) // 3600) + "ч " + str(
                int((int(self.args[0]) % 3600) / 60)) + "м " + str(int(self.args[0]) % 60) + "с ")

    def written_print(self):
        # Вывод текущего состояние набора текста
        self.summ = str(int(self.args[1]) + (int(self.args[2])))
        self.written.setText('Написано: ' + self.summ + ' из ' + self.args[3] + ' букв(ы)')

    def wrongs_print(self):
        # Вывод кол-ва ошибок
        if int(self.args[2]) + int(self.args[1]) == 0:
            self.error = 0
        else:
            self.error = int(self.args[2]) / (int(self.args[2]) + int(self.args[1])) * 100
        self.wrongs.setText('Ошибок: ' + str(int(self.error)) + '%')

    def v_print(self):
        # Вывод скорости
        if int(self.args[0]) == 0:
            self.V = 0
        else:
            self.V = (int(self.args[1]) / int(self.args[0])) * 60
        self.v.setText('Скорость: ' + str(int(self.V)) + ' зн/мин')

    def close_program(self):
        # Закрытие программы
        valid = QMessageBox.question(self, 'Подтверждение',
                                     "Вы действительно хотите закрыть программу ", QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            exit()

    def continue_program(self):
        # Закрытие окна с результатом и продолжение работы главного окна
        self.parent.start()
        self.parent.setEnabled(True)
        self.close()
