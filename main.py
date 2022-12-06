def sort(array):                   # функция сортировки (алгоритм сортировки вставками)
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def search_indx(array, element, left, right):  # функция поиска позиции элемента (алгоритм двоичного поиска,)
    middle = (right + left) // 2
    if left > right:
        return middle
    if array[middle] == element:
        return middle-1
    elif element < array[middle]:

        return search_indx(array, element, left, middle - 1)
    else:
        return search_indx(array, element, middle + 1, right)



array = input("Введите последовательность целых  чисел через пробел :   ").split()  # ввод последовательности чисел
number = int(input("Введите целое число:   "))       # ввод числа
array = list(map(int, list(array)))         # преобразование введённой последовательности в список
array = sort(array)                         # cортировка списка
if  number <= array[0] or number > array[len(array)-1]:      # проверка условия нахождения введеного числа в диапазоне значения списка
    print("Введенное число вне диапазона последовательности чисел.")  # если вне списка  вывод ошибки
else:
    print("Для числа {0}\nв отсортированной последовательности {1}\nискомая позиция :" \
          .format(number,array), search_indx(array,number,0,len(array)))            # в противном случае печатаем ответ
