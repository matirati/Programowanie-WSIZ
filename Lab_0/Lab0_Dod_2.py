import math
a=float(input("Bok a: "))
b=float(input("Bok b: "))
c=float(input("Bok c: "))

p=(a+b+c)/2

P=(p*((p-a)*(p-b)*(p-c)))**(1/2)
#if a+b<c:
   # print("Taki trójkąt nie istnieje.")
#elif a+c<b:
  #  print("Taki trójkąt nie istnieje.")
#elif b+c<a:
  #  print("Taki trójkąt nie istnieje.")
if a+b<c or a+c<b or b+c<a:
    print("Taki trójkąt nie istnieje")
else:
    print("Pole trójkąta wynosi: {:3.2f}".format(P))
