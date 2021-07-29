# По данному целому положительному числу N определите N-ое число Фибоначчи

input_number = int(input('Введите целое положительное число n: '))

def f(x):
    if x == 1 or x == 2:
        return 1
    else:
        return f(x-1) + f(x-2)

print(f(input_number))