#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('table.ui', self)
        # self.setWindowTitle('Table-Array PyQt5')  # Установка титула диалогового окна
        # self.setWindowIcon(QtGui.QIcon('logo.png'))  # Установка логотипа диалогового окна
        self.pushButton_fill.clicked.connect(self.fill_random_numbers)
        self.pushButton_execute.clicked.connect(self.solve)

    def fill_random_numbers(self):  # Функция для заполнения таблицы случайными числами
        row = col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)  # Присвоение перемнной случайных значений от 0 до 100
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0
        zero_counter = get_number_of_zeros(self.tableWidget)
        if not zero_counter:
            self.label_zero_amount.setText('Количество нулей: 0')
            self.label_status.setStyleSheet('color: gray; font: bold 14pt "Calibri"')
            self.label_status.setText('В таблице нет нулей!')
        else:
            self.label_zero_amount.setText('Количество нулей: ' + str(zero_counter))
            self.label_status.setText('')

    def solve(self):
        zero_counter = get_number_of_zeros(self.tableWidget)
        if not zero_counter:
            self.label_zero_amount.setText('Количество нулей: 0')
            self.label_status.setStyleSheet('color: red; font: bold 14pt "Calibri"')
            self.label_status.setText('В таблице отсутствуют нули!')
        else:
            self.label_status.setStyleSheet('color: green; font: bold 14pt "Calibri"')
            self.label_status.setText('Задание выполнено!')
            row = col = 0
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    number = self.tableWidget.item(row, col).text()
                    if int(number) % 2 != 0:
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(zero_counter)))
                    col += 1
                col = 0
                row += 1


def get_number_of_zeros(table_widget):
    # zero_counter = sum([i.count(0) for i in array])
    try:
        zero_counter = row = col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number == 0:
                    zero_counter += 1
                col += 1
            row += 1
            col = 0
        return zero_counter
    except Exception:
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
