def fun(imie, wiek=20):
    """komentarz"""
    print(f"Nazywam się {imie}, i mam {wiek} lat.")

fun("Janusz",24)
print(fun.__doc__)
fun("Jarek")
