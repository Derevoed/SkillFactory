list = []
while len(list) == 0:
    nums = input('Введите последовательность целых чисел в любом порядке, через пробел: ')

    import re

    r = re.search(r'^[0-9 -]+$', nums)
    if r:
        nums_ = nums.split()
        for i in nums_:
            list.append(int(i))
    else:
        print('Введите корректные значения!')
        list = []
a = int(input('Введите любое целое число: '))
if a in list:
    def sorting(array):
        for i in range(1, len(array)):
            x = array[i]
            idx = i
            while idx > 0 and array[idx - 1] > x:
                array[idx] = array[idx - 1]
                idx -= 1
            array[idx] = x
        return (list)

    print(sorting(list))

    def binary_search(array, element, left, right):
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            if middle == 0:
                return f'Введенное число находится на крайней левой позиции с индексом {middle} и не имеет соседнего элемента слева,' \
                       f' \nНомер позиции большего либо равного элемента справа: {middle + 1}'
            elif middle == len(list) - 1:
                return f'Введенное число находится на крайней правой позиции с индексом {middle} и не имеет соседнего элемента справа, ' \
                       f'\nНомер позиции меньшего элемента слева: {middle - 1} '
            elif array[middle] == array[0]:
                return f'Введенное число находится на крайней левой позиции с индексом 0 и не имеет соседнего элемента слева,' \
                       f' \nНомер позиции большего либо равного элемента справа: 1'
            return f'Номер позиции элемента, который меньше введенного числа: {middle - 1}, ' \
                   f'\nНомер позиции элемента большего, либо равного введенному числу: {middle + 1}'
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)

    print(binary_search(list, a, 0, len(list) - 1))

else:
    print(f'Число {a} не входит в последовательность, поиск позиции не имеет смысла')
