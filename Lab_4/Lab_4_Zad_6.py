def poletrojkata(a,b,c):
    try:
        if a<=0 or b<=0 or c<=0:
            raise ValueError("Długości boków muszą być dodatnie")
        if a+b<=c or a+c<=b or b+c<=a:
            raise ValueError("Długości boków nie spełniają warunku trójkąta")

        s=(a+b+c)/2
        pole=(s*(s-a)*(s-b)*(s-c))**0.5
        return pole

    except ValueError as e:
        print(f"Błąd: {e}")
        return None

a=float(input("Podaj długość boku a: "))
b=float(input("Podaj długość boku b: "))
c=float(input("Podaj długość boku c: "))

pole=poletrojkata(a, b, c)

if pole is not None:
    print(f"Pole trójkąta o bokach {a},{b},{c} wynosi: {pole}")