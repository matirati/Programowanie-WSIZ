print("Wybierz ciąg liczb do wypisania")
print("Nr.1- 1, 2, 3, ... , 99, 100")
print("Nr.2- 100, 99, ... , 2, 1, 0")
print("Nr.3- 3= 7, 14, 21, ... , 70, 77")
print("Nr.4- 20, 18, ... , 2, 0")


opcja=input("Podaj, który ciąg wypisać:")

if opcja=="1":
    for a in range(1,101):
        print(a)
elif opcja=="2":
    for b in range(100,0,-1):
        print(b)
elif opcja=="3":
    for c in range(7,78,7):
        print(c)
elif opcja=="4":
    for d in range(20,-1,-2):
        print(d)
else:
    print("Błąd")