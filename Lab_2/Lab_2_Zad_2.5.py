def silnia(n):
    if n==0 or n==1:
        return 1
    else:
        return n*silnia(n-1)

n=int(input("Podaj liczbę naturalną n: "))


if n<0:
    print("Podana liczba musi być nieujemna.")
else:
    try:
        wynik=silnia(n)
        print(f"Silnia z {n} to {wynik}")
    except RecursionError:
        print("Bład, zbyt duża liczba.")

