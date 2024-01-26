def potega(a, n):
    if n==0:
        return 1
    else:
        return a*potega(a,n-1)

# Przykład użycia
liczba=float(input("Podaj liczbę: "))
wykladnik=int(input("Podaj wykładnik: "))

wynik=potega(liczba, wykladnik)
print(f"{liczba} do potęgi {wykladnik} wynosi: {wynik}")