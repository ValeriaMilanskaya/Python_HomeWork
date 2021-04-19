# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [ (-4 + 5j), 6, 9.3, True, None, 'string', [5, 6], (1, 2, 2.3),
            {4: 'four', 5: 'five'}, {6,7}, frozenset(), range(8), b'nine', bytearray(b'ten'),
            zip(*[(11 , 12), (13, 14), ('a', 'b')]), TypeError]
for i, item in enumerate(my_list, 1):
    print(f"{i} {item} - {type(item)}")
    