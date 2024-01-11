import random

wejscie=input("Podaj pięć cyfr rozdzielonych przecinkiem: ")

cyfry=wejscie.split(',')
if len(cyfry)!=5:
    print("Podano niewłaściwą liczbę cyfr.")
else:

    tablica=[int(cyfra) for cyfra in cyfry]
    zbior=set(tablica)
    wylosowany=random.choice(list(zbior))


    if wylosowany_element==min(tablica):
        print(f"Wylosowany element {wylosowany} jest najmniejszą z podanych liczb.")
    elif wylosowany_element==max(tablica):
        print(f"Wylosowany element {wylosowany} jest największą z podanych liczb.")
    else:
        print(f"Wylosowany element: {wylosowany}")
