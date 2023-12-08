n=int(input("Podaj liczbę studentów:"))

suma_pkt=0
numer_studenta=1

if n<=0:
    print("Wprowadziłeś niepoprawną liczbę")
    exit()
while numer_studenta<=n:
    punkty=float(input(f"Podaj liczbę punktów jaką uzyskał student: {numer_studenta}"))
    suma_pkt+=punkty
    numer_studenta+=1

srednia_pkt=suma_pkt/n

print(f"Średnia liczba punktów w grupie to: {srednia_pkt}")