def fibonacci(n):
    if n<=0:
        return "Błąd: n musi być liczbą całkowitą dodatnią"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# Przykład użycia
numer_wyrazu=int(input("Podaj numer wyrazu ciągu Fibonacciego: "))

wynik=fibonacci(numer_wyrazu)
if type(wynik)==int:
    print(f"{numer_wyrazu}-ty wyraz ciągu Fibonacciego to: {wynik}")
else:
    print(wynik)