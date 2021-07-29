# Дано целое положительное число. Найти сумму его цифр.

input_number = str(input('Введите целое положительное число n: '))

total = 0
list_of_int = [int(x) for x in list(input_number)]

for i in list_of_int :
    total += i

print(total)