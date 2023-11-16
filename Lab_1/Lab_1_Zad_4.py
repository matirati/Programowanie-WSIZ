import cmath

def równanie_kwadratowe(a, b, c):
    delta = (b**2-4*a*c)**(1/2)
    if delta.imag > 0:
        print("Równanie sprzeczne")
        return None
    x1 = (-b-delta)/(2*a)
    x2 = (-b+delta)/(2*a)
    return x1, x2

a=float(input("Podaj a"))
b=float(input("Podaj b"))
c=float(input("Podaj c"))

wynik = równanie_kwadratowe(a, b, c)

if wynik:
    print("Rozwiązanie równania kwadratowego")
    print("x1=", wynik[0])
    print("x2=", wynik[1])
