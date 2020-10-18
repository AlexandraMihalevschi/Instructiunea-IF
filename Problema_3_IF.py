"""Să se verifice dacă o literă introdusă este vocală sau consoană. 
Exemplu : Date de intrare a Date de ieşire vocala."""
l = input("Dați o literă: ")
if (l=='A')or(l=='O')or(l=='U')or(l=='I')or(l=='E')or(l=='Ă')or(l=='Â')or(l=='Î')or(l=='a')or(l=='o')or(l=='u')or(l=='i')or(l=='e')or(l=='ă')or(l=='â')or(l=='î'): 
    print(l, "este o vocală")
elif (l=='Q')or(l=='W')or(l=='R')or(l=='T')or(l=='Y')or(l=='P')or(l=='S')or(l=='D')or(l=='F')or(l=='G')or(l=='H')or(l=='J')or(l=='K')or(l=='L')or(l=='Z')or(l=='X')or(l=='C')or(l=='V')or(l=='B')or(l=='N')or(l=='M')or(l=='q')or(l=='w')or(l=='r')or(l=='t')or(l=='y')or(l=='p')or(l=='s')or(l=='d')or(l=='f')or(l=='g')or(l=='h')or(l=='j')or(l=='k')or(l=='l')or(l=='z')or(l=='x')or(l=='c')or(l=='v')or(l=='b')or(l=='n')or(l=='m'):
    print(l, "este o consoană")
else: print("Eroare")