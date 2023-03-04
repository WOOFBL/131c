n= int(input("Введите количество выводимых чисел:\nn="))
b_first= int(input("Введите первое число прогрессии:\nb_1="))
q= int(input("Введите знаменатель геометрической прогрессии\nq="))
print(b_first)
b_alfa=b_first
for i in range(1,n):
  b_next= b_alfa*q
  print(b_next)
  b_alfa= b_next

print("Арифметическая прогрессия")
n= int(input("Введите количество выводимых чисел:\nn="))
a_first= int(input("Введите первое число прогрессии:\na_1="))
d= int(input("Введите знаменатель арифметической прогрессии:\nd="))
a_alfa=a_first
for i in range(1,n):
  a_next= a_alfa+(i-1)*d
  print("a",i,"=",a_next)
  a_alfa= a_next
# вроде правильно но я не уверен (о_о)