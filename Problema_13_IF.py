"""La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
rosie. """
x = int(input("Locul lui Ionel "))
if (x>0)and(x<=25):
    print("A primit tricou de culoare alba")
elif (x>25)and(x<=50):
    print("A primit tricou de culoare rosie")
elif (x>50)and(x<=75):
    print("A primit tricou de culoare albastra")
elif (x>75)and(x<=100):
    print("A primit tricou de culoare neagra")
elif(x<0)or(x>100):
    print("Nu a primit niciun tricou")