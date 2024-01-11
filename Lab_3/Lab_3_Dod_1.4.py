
def zamiana(ciag):
    zmieniony_ciag = ''
    for znak in ciag:
        if ciag.count(znak) > 1:
            zmieniony_ciag += '@'
        else:
            zmieniony_ciag += znak
    return zmieniony_ciag

ciagi=input("Podaj ciąg znaków:")
koncowy = zamiana(ciagi)
print("Zmieniony ciąg znaków:", koncowy)
