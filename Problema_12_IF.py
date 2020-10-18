"""“Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: … de loc."""
x = int(input("Numarul de petale al margaretei "))
if x%5==0:
    print("...deloc")
elif x%4==0:
    print("...la nebunie")
elif x%3==0:
    print("... cu pasiune")
elif x%2==0:
    print("... mult")
else: print("...un pic")