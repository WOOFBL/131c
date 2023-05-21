def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

def get_primes(a, x):
    primes = []
    for i in range(a, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes

a = int(input("Введите начало диапазона: "))
x = int(input("Введите конец диапазона: "))
primes = get_primes(a, x)
print("Простые числа от", a, "до", x, ":", primes)