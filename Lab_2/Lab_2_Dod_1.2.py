
n=int(input("Podaj liczbę studentów: "))

suma_pkt=0
numer_studenta=1

if n<=0:
    print("Błąd.")
    exit()


while True:
#while numer_studenta <=n: - to z początku zadania
    try:
        punkty=float(input(f"Podaj liczbę punktów jaką uzyskał student {numer_studenta}: "))
        if punkty<0 or punkty>100:
            print("Liczba punktów nie jest z przedziału 0-100, błąd.")
            continue
        suma_pkt+=punkty
        numer_studenta+=1
        if numer_studenta>n: #to oraz break nizej dodane razem z "while True"
            break
    except ValueError:
        print("Niepoprawna liczba")

srednia_pkt=suma_pkt/n

print(f"Średnia liczba punktów w grupie to: {srednia_pkt}")
