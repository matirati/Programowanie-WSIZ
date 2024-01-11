zdanie=str(input("Wpisz zdanie:"))
wyrazy=zdanie.split()

duze=[wyraz.capitalize() for wyraz in wyrazy]
noweZdanie=' '.join(duze)
print(noweZdanie)