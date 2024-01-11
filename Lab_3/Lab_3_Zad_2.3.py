rachunki={"Wrzesień":55, "Październik":60,"Listopad":65,"Grudzień":80}
print(rachunki)

suma=sum(rachunki.values())
print(f"Suma wynosi: {suma}")
max=max(rachunki.values())
print(f"Maksymalna wynosi: {max}")
min=min(rachunki.values())
print(f"Minimalna wynosi: {min}")
sred=(sum(rachunki.values())/len(rachunki))
print(f"Średnia wynosi:{sred}")

ost=rachunki["Grudzień"]
print(f"Ostatni miesiąc:{ost}")

if ost>sred:
    print("Zacznij oszczędzać!")
else:
    print("Jesteś bezpieczny")