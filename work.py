from PyQt5.Qt import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from design.main.main import Ui_MainWindow
from result import Result


class Work(QMainWindow, Ui_MainWindow):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.timer = QtCore.QTimer()
        self.text_name.setText(self.name)  # Установка имени поле
        self.wrong = 0  # Кол-во неправильных букв
        self.right = 0  # Кол-во правильных букв
        self.time = 0  # Время
        self.hms = ''  # Вывод времени
        self.flag_esc = False
        self.flag_start = False
        self.text_false.setText('Выберите занятие или свой файл')
        self.text_time.setText('0:0:0')
        self.btn_choice.clicked.connect(self.open)

        # Установка моноширинного шрифта для правильного и красивого отображения текста

        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont("files/RobotoMono-Regular.ttf")
        self.families = font_db.applicationFontFamilies(font_id)
        self.MyFont = QFont(self.families[0])
        self.text_print.setFont(self.MyFont)
        self.text_print.setFontPointSize(20)
        self.text_true.setVisible(False)

    def keyPressEvent(self, e):  # Обработчик событий нажатой клавиши
        if self.flag_start is True:
            self.checked(e.text())

        if e.key() == Qt.Key_Escape:
            if self.flag_esc is False:
                self.close()
            else:
                self.open_result(False)

        elif e.key() == Qt.Key_Space:
            if self.flag_start is False:
                # Начало работы ввода текста
                self.start()
                self.flag_esc = True
                self.flag_start = True
                self.text_print.setText(self.text[:46])
                self.text_info.setText('Esc - Выход/Пауза')
                self.progress.setStyleSheet("""QProgressBar {background-color: rgba(255,255,255,100);border: 1px solid #1565C0;} \
                QProgressBar::chunk {background-color: lightblue}""")
                self.set_temp_result()

    def open(self):
        # Открытие занятия или своего файла для набора в поле ввода
        i, okBtnPressed = QInputDialog.getItem(self, "Выбор",
                                               "Выберите занятие",
                                               ("аа-оо", "пп-рр", "Выбрать свой файл"),
                                               0, False)
        if i == "аа-оо":
            self.file = ''.join(open("files/аа-оо.txt", encoding="UTF-8").readlines())
        elif i == "пп-рр":
            self.file = ''.join(open("files/пп-рр.txt", encoding="UTF-8").readlines())
        elif i == "Выбрать свой файл":
            self.fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
            if self.fname:
                self.file = ''.join(open(self.fname, encoding="UTF-8").readlines())
        if self.file and okBtnPressed:
            self.btn_choice.setVisible(False)
            self.btn_choice.setEnabled(False)
            self.text = 23 * ' ' + self.file[1:]  # Текст
            self.letter = self.text[23]
            self.text_n = len(self.text) - 23
            self.text_info.setText('Space - начать, Esc - Выход/Пауза')
            self.text_true.setVisible(True)
            self.set_temp_result()

    def set_temp_result(self):
        # Вывод текущих результатов на экран
        self.text_false.setText(f'Ошибок: {self.wrong}')
        self.text_true.setText(f'Правильных: {self.right}')

    def start(self):
        # Запуск функции
        self.timer.timeout.connect(self.show_time)
        # Ожидание - 1 секунда
        self.timer.start(1000)

    def show_time(self):
        # Вывод времени на экран
        self.time += 1
        self.hms = str(self.time // 3600) + ":" + str(int((self.time % 3600) / 60)) + ":" + str(self.time % 60)
        self.text_time.setText(self.hms)

    def checked(self, new_letter):
        # Обработка введенного символа
        if (new_letter.isalpha() or new_letter in ' ,.:;!?') and new_letter != '':  # Проверка на валидность
            if new_letter == self.letter:  # Проверка на правильность введенного символа
                self.block_grey.setStyleSheet(
                    "background-color: rgba(60, 255, 70, 100);border: 1px solid #1565C0;border-top-left-radius: 8px;")
                self.right += 1
                self.shift()
            else:
                self.block_grey.setStyleSheet(
                    "background-color: rgba(255, 60, 60, 100);border: 1px solid #1565C0;border-top-left-radius: 8px;")
                self.wrong += 1
                self.shift()
        self.set_temp_result()

    def shift(self):
        # Установка параметров и обработка текста
        self.text = self.text[1:]
        self.text_print.setText(self.text[:46])
        if self.text_n != 0:
            self.progress.setValue(
                int(((self.right + self.wrong) / self.text_n) * 100))  # Установка значений ProgressBar
        if len(self.text) > 23:
            self.letter = self.text[23]  # Следующий символ
        else:
            self.open_result(True)  # Вывод результатов

    def open_result(self, b):
        # Открытие окна с результатом текущей сессии
        self.timer.stop()
        self.setEnabled(False)
        global result
        result = Result(self, self.name, str(self.time), str(self.right), str(self.wrong), str(self.text_n), b)
        result.show()
