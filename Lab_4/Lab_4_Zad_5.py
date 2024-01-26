waga = int(input("Podaj wagę:"))
wzrost = int(input("Podaj wzrost:"))

def fun(waga, wzrost):
    BMI = waga / (wzrost / 100)**2
    if BMI<16:
        return "Wygłodzenie"
    elif BMI<16.99:
        return "Wychudzenie"
    elif BMI<18.49:
        return "Niedowaga"
    elif BMI<24.99:
        return "Dobra"
    elif BMI>29.99:
        return "Nadwaga"
    else:
        return "Błąd"

wynik=fun(waga,wzrost)
print(wynik)