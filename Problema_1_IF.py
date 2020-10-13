"""Se introduc trei date de forma număr curent elev, punctaj. 
Afişaţi numărul elevului cu cel mai mare punctaj. 
Exemplu: Date de intrare  nr crt  7  punctaj 120  nr crt  3  punctaj 100 nr crt 4 punctaj 119  
Date de ieşire  punctaj maxim areelevul cu nr crt 7."""
n1 = int(input("Numarul elevului curent: "))
n2 = int(input("Numarul elevului curent: "))
n3 = int(input("Numarul elevului curent: "))
p1 = int(input("Punctajul 1: "))
p2 = int(input("Punctajul 2: "))
p3 = int(input("Punctajul 3: "))
if (p1>p2)and(p1>p3) :
    print("Punctaj maxim la elevul", n1)
elif (p2>p3)and(p2>p1) :
    print("Punctaj maxim la elevul", n2)
elif (p3>p1)and(p3>p2) :
    print("Punctaj maxim la elevul", n3)
elif (p1==p2)and(p1==p3)and(p2==p3):
    print("Elevii au punctaje egale")