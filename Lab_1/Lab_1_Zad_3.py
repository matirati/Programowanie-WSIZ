import sys
def dodawanie(a, b):
    return a+b
def odejmowanie(a, b):
    return a-b
def mnożenie(a, b):
    return a*b
def dzielenie(a, b):
    if b == 0:
        raise ZeroDivisionError("Nie można dzielić przez 0")
    return a/b
def potęgowanie(a, b):
    return a**b



print("Wybierz Opcje.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")
print("5.Potęgowanie")

Wybór=input("Wpisz numer działania  (1,2,3,4,5):")

if Wybór != "1" and Wybór != "2" and Wybór != "3" and Wybór != "4" and Wybór != "5":
    print("Niepoprawna wartość")
    sys.exit(0)



#if Wybór>"5":
        #print("Niepoprawna wartość")
        #sys.exit(0)
try:
    pierwsza = float(input("Podaj pierwsza liczbe:"))
    druga = float(input("Podaj druga liczbe:"))
except ValueError:
    print("Nieprawidłowa wartość")
    sys.exit(1)
try:
    if Wybór == "1":
        print(pierwsza, "+", druga, "=", dodawanie(pierwsza, druga))
    elif Wybór == "2":
        print(pierwsza, "-", druga, "=", odejmowanie(pierwsza, druga))
    elif Wybór == "3":
        print(pierwsza, "*", druga, "=", mnożenie(pierwsza, druga))
    elif Wybór == "4":
        print(pierwsza, "/", druga, "=", dzielenie(pierwsza, druga))
    elif Wybór == "5":
        print(pierwsza, "**", druga, "=", potęgowanie(pierwsza, druga))
except OverflowError:
        print("Zbyt duża liczba, błąd")
