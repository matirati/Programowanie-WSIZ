
import random
import string

n=int(input("Podaj wartość n:"))
x=int(input("Podaj wartość x:"))

def listaa(n,x):
    lista=[]
    for _ in range(n):
        dlugosc=random.randint(1,x)
        ciag='' .join(random.choice(string.ascii_lowercase) for _ in range (dlugosc))
        lista.append(ciag)
    return lista


wynik=listaa(n,x)
print(wynik)

for ciag in wynik:
    print(f"Długość ciągu '{ciag}' : {len(ciag)}")



def literyk(lista):
    for ciag in lista:
        ilosck=ciag.count('k')
        print(f"Ilość liter 'k' w '{ciag}': {ilosck}")

literyk(listaa(n,x))

def literykt(lista):
    for ciag in lista:
        ilosckt=ciag.count('kt')
        print(f"Ilość znaków 'kt' w '{ciag}': {ilosckt}")

literykt(listaa(n,x))

s=int(input("Podaj wartość s:"))

def dluzszy_niz_s(lista, s):
    dluzsze_ciagi=[ciag for ciag in lista if len(ciag)>s]
    if dluzsze_ciagi:
        print(f"Ciągi dłuższe od 's': {dluzsze_ciagi}")
    else:
        print("Nie ma dłuższych niż podana liczba")

dluzszy_niz_s(wynik,s)