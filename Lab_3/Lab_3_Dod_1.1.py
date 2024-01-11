zdanie=str(input("Podaj zdanie:"))
print(sorted(zdanie))

alfabet="abcdefghijklmnoprstuwxyz"

#brakujace=[litera for litera in alfabet if litera not in zdanie]
#print("Litery, których nie ma w zdaniu:", brakujace)

brakujace=set(alfabet)-set(zdanie)
print(brakujace)

