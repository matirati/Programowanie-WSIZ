promien=int(input("Podaj długość promienia koła:"))

def PoleKola(r):
    pole=3.14*r**2
    return pole

wynik=PoleKola(promien)
print("Pole wynosi:", wynik)