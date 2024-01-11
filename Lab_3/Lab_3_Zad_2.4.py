import random
a=random.randint(3,7)
b=random.randint(3,7)

X=set(random.randint(0,10) for _ in range(a))
Y=set(random.randint(0,10) for _ in range(b))

print(f"Zbiór X ({len(X)} elementów): {X}")
print(f"Zbiór Y ({len(Y)} elementów): {Y}")

if 5 in X:
    print("Zawiera liczbę 5.")
else:
    print("Nie zawiera liczby 5.")

if X <= Y:
    print("X jest podzbiorem Y.")
else:
    print("X nie jest podzbiorem Y")

if Y <= X:
    print("Y jest podzbiorem X.")
else:
    print("Y nie jest podzbiorem X.")

if X >= Y:
    print("Zbiór X jest nadzbiorem zbioru Y.")
else:
    print("Zbiór X nie jest nadzbiorem zbioru Y.")

if Y >= X:
    print("Zbiór Y jest nadzbiorem zbioru X.")
else:
    print("Zbiór Y nie jest nadzbiorem zbioru X.")

suma=X.union(Y)
print(f"Suma zbiorów X i Y: {suma}")

roznica=X-Y
print(f"Różnica zbiorów X i Y: {roznica}")

roznica2=Y-X
print(f"Różnica zbiorów Y i X: {roznica2}")

iloczyn=Y&X
print(f"Iloczyn zbiorów X i Y: {iloczyn}")

roznicasym=X^Y
print(f"Różnica symetryczna zbiorów X i Y: {roznicasym}")

najwyzszyX=max(X)
najwyzszyY=max(Y)

print(f"Najwyższy element w zbiorze X: {najwyzszyX}")
print(f"Najwyższy element w zbiorze Y: {najwyzszyY}")

usuniety=X.pop()
Y.add(usuniety)
print(f"Zbiór X po usunięciu pierwszego elementu: {X}")
print(f"Zbiór Y po dodaniu pierwszego elementu: {Y}")

Y.update(X)
print(Y)

X.clear()
Y.clear()

print(X)
print(Y)