x=int(input("Podaj wiek"))

if x > 18:
    print("Bilet kosztuje 20zł")
elif x < 0:
    print("Błąd")
elif x >= 4:
    print("Bilet kosztuje 10zł")
else:
    print("Bilet darmowy")