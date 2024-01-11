import string

n=int(input("Podaj wartość 'n':"))

lista=(string.ascii_lowercase)

wynik=(lista[::n])

print(f"[{',' .join(wynik)}]")