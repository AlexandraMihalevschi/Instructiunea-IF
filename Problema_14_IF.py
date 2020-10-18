"""Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
Exemplu : date de intrare : n=69 date de ieşire : casuta 17."""
n = int(input("Numarul de ordine a lui Ionel "))
if n>0:
    print("El a fost cazat in casuta a", n//4)
else: print(" Ionel nu a fost la tabara")