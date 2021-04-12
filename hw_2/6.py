# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    features = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f'\nТекущая аналитика по товарам: \n{"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}:{value}')
    print("*" * 30)