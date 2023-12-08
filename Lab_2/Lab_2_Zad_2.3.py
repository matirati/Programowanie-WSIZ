#liczbaG=int(input("Podaj liczbę gwiazdek w linii: "))

#for i in range(liczbaG):
   #print("*"*(i+1))
#if liczbaG<=0:
    #print("Błąd")

#to wyzej to brzydsza choinka

liczbaG=int(input("Podaj liczbę gwiazdek w linii: "))

for i in range(1,liczbaG+1):
    gwiazdki='* '*i
    spacje=' '*(liczbaG - i)
    print(spacje+gwiazdki)