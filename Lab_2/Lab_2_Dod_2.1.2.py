import math

while True:
    dana=input("Podaj liczbę całkowitą (aby zakończyć, wpisz 'koniec'): ")

    if dana.lower()=='koniec':
        print("Dziękujemy za skorzystanie z naszej aplikacji.")
        break

    try:
        dana=int(dana)
        if dana>=0:
            print("To jest liczba.")
            pierwiastek=math.sqrt(dana)
            print(f"Pierwiastek kwadratowy z {dana} to {pierwiastek}")
        else:
            print("To jest liczba ujemna.")
    except ValueError:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")


