print("Odpowiedz: 'Tak' lub 'Nie' ")
deszcz=str(input("Czy pada deszcz?"))
autobus=str(input("Czy na przystanku jest autobus?"))

if deszcz == "Tak" and autobus == "Tak":
    print("Weź parasol, dostaniesz się na uczelnię")
elif deszcz == "Tak" and not autobus == "Tak":
    print("Nie dostaniesz się na uczelnię")
elif not deszcz == "Tak" and autobus == "Tak":
    print("Dostaniesz się na uczelnię, miłego dnia i pięknej pogody")
else:
    print("Błąd")