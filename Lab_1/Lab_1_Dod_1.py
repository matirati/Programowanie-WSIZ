
print("Wybierz funkcję:")
print("1.Funkcja a(x)")
print("2.Funkcja b(x)")
print("3.Funkcja c(x)")

wybór=input("Wpisz numer funkcji (1,2,3):")

if wybór == "1":
    xa=float(input("Wartość x dla funkcji a(x):"))
if wybór == "2":
    xb=float(input("Wartość x dla funkcji b(x):"))
if wybór == "3":
    xc=float(input("Wartość x dla funkcji c(x):"))

if wybór == "1":
    if xa > 0:
        print("Wynik wynosi:", xa*2)
    elif xa == 0:
        print("Wynik wynosi: 0")
    elif xa < 0:
        print("Wynik wynosi:", xa*(-3))
if wybór == "2":
    if xb >= 1:
        print("Wynik wynosi:", xb**2)
    elif xb < 1:
        print("Wynik wynosi:", xb)

if wybór == "3":
    if xc > 2:
        print("Wynik wynosi:", xc+2)
    elif xc == 2:
        print("Wynik wynosi:", 8)
    elif xc < 2:
        print("Wynik wynosi:", xc-4)