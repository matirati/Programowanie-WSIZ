import random

Spalanie=float(input("Spalanie samochodu:"))
#Droga=float(input("Przebyta droga(km):"))
Droga=random.randint(1,100000)
print("Na" , Droga, "kilometrów:")
Cena=6.70

Zużycie=(Spalanie*Droga)/100
Koszt=Zużycie*Cena

#print("Zużyjesz", Zużycie, "litrów paliwa")
#print("Koszt podróży wyniesie" , Koszt,"złotych")

print( f"Zużyjesz {Zużycie} litrów paliwa")
print(f"Koszt podrózy wyniesie {Koszt} złotych")