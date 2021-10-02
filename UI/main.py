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
                random_num = randint(0, 101)  # Присвоение перемнной случайных значений от 0 до 100
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        list_information_zero_num = get_info(self.tableWidget)
        if not list_information_zero_num:
            self.label_status.setStyleSheet('color: red; font: bold 14pt "Calibri"')
            self.label_status.setText('Введены неправильные данные!')
        else:
            self.label_zero_amount.setText('Количество нулей: ' + str(list_information_zero_num[0]))
            self.label_zero_index.setText('Индекс нулей: ' + ' [' +
                                          str(list_information_zero_num[1]) + ';' +
                                          str(list_information_zero_num[2]) + ']')
            self.label_status.setText('')

    def solve(self):

        list_information_zero_num = get_info(self.tableWidget)
        if not list_information_zero_num:
            self.label_status.setStyleSheet('color: red; font: bold 14pt "Calibri"')
            self.label_status.setText('В таблице отсутствуют нули!')
        else:
            self.label_status.setStyleSheet('color: green; font: bold 14pt "Calibri"')
            self.label_status.setText('Задание выполнено!')
            self.label_zero_amount.setText('Количество нулей: ' + str(list_information_zero_num[0]))
            self.label_zero_index.setText('Индекс нулей: ' + ' [' +
                                          str(list_information_zero_num[1]) + ';' +
                                          str(list_information_zero_num[2]) + ']')
            row = 0
            col = 0
            flag = False
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    item = self.tableWidget.item(row, col).text()
                    # три случая:
                    # 1) элемент равен нулю
                    # 2) элемент равен максимальному числу
                    #   2.1) максимальный элемент раплолагается в 1-ой ячейке и перед ним нет ячеек
                    # 3) элемент равен иному числу

                    # for i in range(len(array)):
                    #     for j in range(len(array[i])):
                    #         if array[i][j] % 2 != 0:
                    #             array[i][j] = zero
                    # return array

                    if int(item) == 0:
                        col += 1
                    elif int(item) == list_information_zero_num[0]:
                        if int(item) % 2 != 0:
                            self.tableWidget.setItem(QTableWidgetItem(str(list_information_zero_num[0])))
                        else:
                            self.tableWidget.setItem(QTableWidgetItem(str(list_information_zero_num[0])))
                        self.label_odds.setText('Количество нечётных элементов: ' + str(list_information_zero_num[0]))
                        flag = True
                        break
                    else:
                        self.label_odds.setText('Количество нечётных элементов: 0')
                        flag = True
                        break
                if flag:
                    break
                row += 1
                col = 0
            self.label_status.setText('')


def get_info(table_widget):
    # zero_counter = sum([i.count(0) for i in array])
    zero_counter = odd_counter = row = col = row_zero_number = col_zero_number = 0
    # zero_num = int(table_widget.item(row_zero_number, col_zero_number).text())

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number == 0:
                    # zero_num = number
                    row_zero_number = row
                    col_zero_number = col
                    zero_counter += 1
                col += 1
                # elif number == 0:
                #     odd_counter += 1

            row += 1
            col = 0
        return [zero_counter, row_zero_number, col_zero_number]
    except Exception:
        self.label_zero_amount.setText('В таблице отсутствуют нули!')
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
