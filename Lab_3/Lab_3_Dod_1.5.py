zdanie=str(input("Podaj zdanie:"))

def najdluzsze_slowo(zdanie):
    slowa=zdanie.split()
    najdluzsze=max(slowa, key=len)
    dlugosc=len(najdluzsze)
    return najdluzsze, dlugosc

najdluzsze, dlugosc=najdluzsze_slowo(zdanie)
print("Najdłuższe słowo:", najdluzsze)
print("Długość tego słowa:", dlugosc)