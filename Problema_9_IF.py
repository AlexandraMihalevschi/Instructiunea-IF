"""Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
bilelor: 17 Mari: 11 bile Verzi: 7 bile ."""
xa = int(input("Bile albe mici "))
ya = int(input("Bile albe mari "))
xr = int(input("Bile rosii mici "))
yr = int(input("Bile rosii mari "))
xv = int(input("Bile verzi mici "))
yv = int(input("Bile verzi mari "))
tx = xa+xr+xv
ty = ya+yr+yv 
print("In total bile sunt", tx+ty)
if tx>ty: print(tx, " mici")
elif tx<ty: print(ty, " mari")
elif tx==ty: print("sunt in numar egale", tx)
if (xa+ya>xr+yr)and(xa+ya>xv+yv):
    print(xa+ya, "albe")
elif (xr+yr>xa+ya)and(xr+yr>xv+yv):
    print(xr+yr, "rosii")
elif (xv+yv>xa+ya)and(xv+yv>xr+yr):
    print(xv+yv, "verzi")
elif (xa+ya==xr+yr)and(xa+ya>xv+yv)and(xr+yr>xv+yv):
    print("albe si rosii sunt egale", xa+ya)
elif (xa+ya==xv+yv)and(xa+ya>xr+yr)and(xv+yv>xr+yr):
    print("albe si verzi sunt egale", xa+ya)
elif (xv+yv==xr+yr)and(xv+yv>xa+ya)and(xr+yr>xa+ya):
    print("verzi si rosii sunt egale", xr+yr)
elif (xa+ya==xv+yv)and(xa+ya==xr+yr)and(xv+yv==xr+yr):
    print("toate sunt egale", xa+ya)