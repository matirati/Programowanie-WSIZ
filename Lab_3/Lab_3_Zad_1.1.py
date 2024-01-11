Lista=["Andrzej", "Tomek", "Mateusz", "Joanna"]
posLista=sorted(Lista)
#print(posLista)

pos2=Lista.sort()

posLista.append("Adam")
posLista.append("Wojtek")
#print(posLista)

ostatnieImie=posLista.pop()
#print(ostatnieImie)
#print(posLista)

posLista.insert(3, "Filip")
#print(posLista)

odwr=posLista.reverse()
odwr=posLista*2
print(odwr)
