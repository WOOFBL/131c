def na3(List,math,a,b,c):
 List=[]
 List = [int(input()) for i in range(10)]
 print ("Числа массива:",List)
 max(List)
 print("Максимально число в массиве равно:",max(List))
 List.sort()
 max_num = List[9]
 print("Максимально число в массиве равно:",max_num)
 List.sort()
 min_num = List[0]
 print("Минимальное число в массиве равно:",min_num)
 min(List)
 print("Минимальное число в массиве равно:",min(List))
 a=sum(List)/len(List)
 print("Среднее значение суммы равно:",a)


 def linear_Search(List, n, key):
    for i in range(0, n):
        if (List[i] == key):
            return i
    return -1


 list.copy(List)
 key = 2

 n = len(List)
 res = linear_Search(List, n, key)
 if (res == -1):
    print("Нету такого элемента")
 else:
    print("Индекс элемента: ", res)

 b=len(List)
 print("Колличество элементов в массиве равно:",b)
 List
 def elevent_number(List):
  count = 0
  for element in List:
     count += 1
  return count
 print("Колличество элементов в массиве равно:",elevent_number(List))

 c=sum(List)
 print("Сумма значений в списке равна:",c)

 total=0
 list.copy(List)
 for num in List:
    total += num
 print("Сумма значений в списке равна:",total)
 import math
 math.prod(List)
 print("Произведение чисел в масиве рвано:",math.prod(List))
def na4(list1,list2):
 from random import randint
 list1 = [[randint(0,10) for i in range(5)],[randint(0,10) for i in range(5)]]
 list2= list.copy(list1)
 list2 [0][3]=100
 print(f"list1:{list1}\t list2{list2}")

work_key= input("Выберите пункт\t")
match work_key:
    case "3":
        print("На 3")
        print(na3(1,2,3,4,5))
    case "4":
      print("На 4")
      print(na4(1,2))