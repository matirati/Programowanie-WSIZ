a=int(input("Podaj pierwszą liczbę:"))
b=int(input("Podaj drugą liczbę:"))

if a<b:
    while a<=b:
        print(a)
        a+=1
elif a==b:
        print("Liczby są równe.")
else:
    while b<=a:
        print(b)
        b+=1