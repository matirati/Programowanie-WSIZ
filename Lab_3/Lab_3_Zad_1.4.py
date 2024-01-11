a=str(input("Podaj imię"))
print("Witaj",a)

b=int(input("Podaj wiek"))
print ("Twój wiek to: ",b)

c1=str(input("Podaj imię"))
c2=str(input("Podaj nazwisko"))
print("Twoje inicjały to:",c1[0]+c2[0])

d=str(input("Podaj łańcuch:"))
print(d*5)

e1=str(input("Podaj pierwszy łańcuch:"))
e2=str(input("Podaj drugi łańcuch:"))
e3=(e1+e2)
print(e3)

f1=str(input("Podaj pierwszy łańcuch:"))
f2=str(input("Podaj drugi łańcuch:"))
długośćf1=len(f1)
długośćf2=len(f2)
dzielenie=długośćf1//2
f3=f1[:dzielenie]+f2[dzielenie:]
print(f3)
