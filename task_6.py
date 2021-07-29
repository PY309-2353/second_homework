# По данному целому положительному числу A > 1 определите каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что F_n = A. Если A не является числом Фибоначчи, выведите число -1.

input_number = int(input('Введите целое положительное число A > 1: '))

rnge = range(1, 22)
counter = 1

def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)

for number in rnge:
    if input_number == f(number):
        print(counter)
        break
    elif input_number < f(number):
        print(-1)
        break
    else:
        counter += 1