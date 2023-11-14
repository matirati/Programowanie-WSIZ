BokPierwszy=int(input("Podaj długość pierwszego boku"))
BokDrugi=int(input("Podaj długość drugiego boku"))

Pole=BokPierwszy*BokDrugi
Obwód=(BokPierwszy+BokDrugi)*2

print(type(Obwód))
print("Pole prostokąta to:", Pole)
print("Obwód prostokąta to:" + str(Obwód))