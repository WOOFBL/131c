a= int(input("Введите первое число a\t"))
b= int(input("Введите второе число b\t"))
print(f'произведение суммы и разности {a} и {b} = {(a-b)*(a+b)}')
print(f'разность {a} и {b} возведеная в степень 2 = {((a-b)**2)}')
print(f'сумма {a} и {b} возведенная в степень 2 = {((a+b)**2)}')
print(f'разность {a} и {b} возведенная в степень 3 = {((a-b)**3)}')
print(f'сумма {a} и {b} возведенная в степень 3 = {((a+b)**3)}')
print(f'произведение суммы {a} и {b} на разность {a} и {b} возведенная в степень 2 = {((a+b)*((a-b)**2))}')
print(f'произведение разности {a} и {b} на сумму {a} и {b} возведенная в степень 2 = {((a-b)*((a+b)**2))}')

c= int(input("Введите второе число c\t"))
print({(a*a)+((a+c)**2)/(10*b)-((c**2*a*4)**-1/2)}) #(a*a)+((a+c)**2)/(10*b)-((c**2*a*4)**-1/2)
