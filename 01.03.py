def arithmetic_sum_formula(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)

def arithmetic_sum_loop(a, d, n):
    b = 0
    for i in range(n):
        b += a + i * d
    return b

def geometric_sum_formula(a, x, n):
    if x == 1:
        return n * a
    else:
        return a * (1 - x ** n) / (1 - x)

def geometric_sum_loop(a, x, n):
    b = 0
    for i in range(n):
        b += a * x ** i
    return b

a = int(input("Введите первый член прогрессии: "))
n = int(input("Введите номер последнего члена прогрессии: "))

while True:
    choice = input("Выберите способ решения (1 - формулы, 2 - циклы): ")
    if choice == "1":
        d = int(input("Введите разность арифметической прогрессии или знаменатель геометрической прогрессии: "))
        print("Сумма арифметической прогрессии:", arithmetic_sum_formula(a, d, n))
        print("Сумма геометрической прогрессии:", geometric_sum_formula(a, d, n))
        break
    elif choice == "2":
        d = int(input("Введите разность арифметической прогрессии или знаменатель геометрической прогрессии: "))
        print("Сумма арифметической прогрессии:", arithmetic_sum_loop(a, d, n))
        print("Сумма геометрической прогрессии:", geometric_sum_loop(a, d, n))
        break
    else:
        print("Ошибка: не верный вариант. Попробуйте еще раз.")
