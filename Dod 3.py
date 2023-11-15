import sys


def dodawanie(a, b):
    return a+b
def odejmowanie(a, b):
    return a-b
def mnożenie(a, b):
    return a*b
def dzielenie(a, b):
    return a/b



print("Wybierz Opcje.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

Wybór=input("Wpisz numer działania  (1,2,3,4):")

if Wybór>"4":
        print("Niepoprawna wartość")
        sys.exit(0)

pierwsza = int(input("Podaj pierwsza liczbe:"))
druga = int(input("Podaj druga liczbe:"))

if Wybór=="1":
    print(pierwsza,"+",druga,"=", dodawanie(pierwsza, druga))
elif Wybór=="2":
    print(pierwsza,"-",druga,"=", odejmowanie(pierwsza, druga))
elif Wybór=="3":
    print(pierwsza,"*", druga,"=", mnożenie(pierwsza, druga))
elif Wybór=="4":
    print(pierwsza,"/", druga,"=",dzielenie(pierwsza,druga))
else:
    print("Niepoprawna wartość")



