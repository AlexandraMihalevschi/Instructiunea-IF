"""Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. 
Exemplu : Date de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani."""
ac = int(input("Anul curent "))
lc = int(input("Luna curenta "))
zc = int(input("Ziua curenta "))
an = int(input("Anul nasterii "))
ln = int(input("Luna nasterii "))
zn = int(input("Ziua nasterii "))
if ln>lc :
    print((ac-an)-1)
elif (ln==lc)and(zn>zc):
    print((ac-an)-1)
elif (ln==lc)and(zn<=zc):
    print(ac-an)
elif ln>lc:
    print(ac-an)
elif ac>an:
    print(ac-an)
elif (ac==an)and(lc==ln)and(zc==zn):
    print("Persoana s-a nascut azi")
elif ac<an:
    print("Anul curent este mai mic decat anul nasterii")