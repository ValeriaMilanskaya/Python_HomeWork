6. # Спортсмен занимается ежедневными пробежками.
   # В первый день его результат составил a километров.
   # Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
   # Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
   # Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


days = 1
start_km = float(input('Начальный результат - '))
last_km = float(input('Финальный результат - '))
while start_km < last_km:
    start_km *= 1.1
    days += 1
print(f'Результат через {days} дней')

