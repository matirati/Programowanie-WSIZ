
x=float(input("Wprowadź liczbę x:"))
y=float(input("Wprowadź liczbę y:"))
z=float(input("Wprowadź liczbę z:"))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print("Uporządkowane liczby:", x, y, z )