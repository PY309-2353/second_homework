# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

input_number = int(input('Введите целое положительное число n: '))

sum = str()

for i in range(1, input_number + 1):
    if (i ** 2) <= input_number:
        sum += str(i ** 2) + (' ')
    else:
        break

print(sum)