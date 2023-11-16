
lit=str(input("Wprowadź literę:"))

x=str(lit).islower()
if x == 1:
    print("Zmieniona litera to:", (lit.upper()))
else:
    print("Zmieniona litera to:", (lit.lower()))