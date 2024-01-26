a=int(input("Podaj długość pierwszej podstawy:"))
b=int(input("Podaj długość drugiej podstawy:"))
h=int(input("Podaj wysokość trapezu:"))

def PoleTrapeza(a,b,h):
    pole=((a+b)*h)/2
    return pole

print("Wynik to:", PoleTrapeza(a,b,h))