import math
print("Введите коэффиценты для уравнения")
print("ax^2+bx+c=0:")
a= float(input("a= "))
b= float(input("b= "))
c= float(input("c= "))
D= (b**2)-(4*a*c)
if D> 0:
 x1 = (-b + math.sqrt(D)) / (2 * a)
 x2 = (-b - math.sqrt(D)) / (2 * a)
 print("x1 =  ", x1)
 print("x2 = ", x2)
elif D == 0:
     x0 = -b / (2 * a)
     print("x = " , x0)
else:
   print("Уравнение не имеет корней")