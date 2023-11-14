a=float(input("a= "))
b=float(input("b= "))
if a == 0:
    if b == 0:
        print("Jest to równanie tożsamościowe")
    else:
        print("Równanie sprzeczne")
else:
    x = -b/a
    print(f"x= {x}")