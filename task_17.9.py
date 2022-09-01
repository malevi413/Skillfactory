numbers = input('Введите целые числа через пробел: ')
user_element = int(input('Введите проверяемое число: '))
list_numbers = list(map(int, numbers.split()))


# Сортировка списка слиянием
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


sorted_numbers = merge_sort(list_numbers)
print(f'Упорядоченный по возрастанию список: {sorted_numbers}')


# Установка позиции элемента
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Элемент вне диапазона списка.'


# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.
# (Не уверен что корректно понял данную часть задания)
if not binary_search(sorted_numbers, user_element, 0, len(sorted_numbers)):
    element_ = min(sorted_numbers, key=lambda x: (abs(x - user_element), x))
    ind = sorted_numbers.index(element_)
    max_ind = ind + 1
    min_ind = ind - 1
    if element_ < user_element:
        print(f'''
Ближайший меньший элемент: {element_}, индекс: {ind}
Ближайший больший элемент: {sorted_numbers[max_ind]}, индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''
Ближайший больший элемент: {element_}, индекс: {sorted_numbers.index(element_)}
В списке нет меньшего элемента''')
    elif element_ > user_element:
        print(f'''
Ближайший больший элемент: {element_}, индекс: {sorted_numbers.index(element_)}
Ближайший меньший элемент: {sorted_numbers[min_ind]}, индекс: {min_ind}''')
    elif sorted_numbers.index(element_) == 0:
        print(f'Индекс введенного элемента: {sorted_numbers.index(element_)}')
else:
    print(
        f'Индекс введенного элемента: {binary_search(sorted_numbers, user_element, 0, len(sorted_numbers))}')
