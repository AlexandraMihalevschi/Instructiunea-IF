"""Se introduc vârstele a 3 persoane. Afişaţi vârstele cuprinse între 18 şi 60 de ani. 
Exemplu : Date de intrare 56 34 12 Date de ieşire 56 34."""
a = int(input("Varsta primei persoane: "))
b = int(input("Varsta persoanei a doua: "))
c = int(input("Varsta persoanei a treia: "))
if (a>=18)and(a<=60):
    print(a)
if (b>=18)and(b<=60):
    print(b)
if (c>=18)and(c<=60):
    print(c)
if (a<=18)and(a>=60)and(b<=18)and(b>=60)and(c<=18)and(c>=60):
    print("Toate persoanele nu sunt de varsta potrivita")