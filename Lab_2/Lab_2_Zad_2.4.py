n=int(input("Liczba elementów ciągu: "))
a=int(input("Podaj pierwszy wyraz ciągu: "))
r=int(input("Podaj różnicę ciągu: "))

w=0

for i in range(1,n+1):
    w=a+(i-1)*r
    print(w)
if r>0:
    k=a+(n-1)*r-1
elif r<0:
    k=a+(n-1)*r+1
else:
    print("Ciąg jest stały.")

for i in range(a,k,r):
    print(i)
