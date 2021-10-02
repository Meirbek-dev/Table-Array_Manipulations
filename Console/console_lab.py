#!/usr/bin/env python3
# coding=utf-8

try:
    print("Введите желаемое количество столбцов:")
    column_amount = int(input())
    print("Введите желаемое количество строк:")
    row_amount = int(input())
except ValueError:
    print("Введите целое число!")
    quit()


def input_array(row, column):  # Метод ввода массива
    array = []
    for row_number in range(row):
        sub_array = []
        for column_number in range(column):
            try:
                print('Введите число [', row_number, ':', column_number, ']:')
                number = int(input())
                sub_array.append(number)
            except ValueError:
                print("Вы ввели неверные данные!")
                quit()
        array.append(sub_array)
    return array


def output_array(array):  # Метод вывода массива
    print()
    for row_element in array:
        for column_element in row_element:
            print("%d\t" % column_element, end='')
        print()


def find_zeros(array):  # Нахождение нулей в массиве
    zero_counter = sum([i.count(0) for i in array])
    print("Количество нулей в массиве: ", zero_counter)
    return zero_counter


def execute(array, zero):  # Выполнение задания
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] % 2 != 0:
                array[i][j] = zero
    return array


def main():
    array = input_array(column_amount, row_amount)
    output_array(array)
    zero = find_zeros(array)
    array = execute(array, zero)
    output_array(array)


if __name__ == '__main__':
    main()
