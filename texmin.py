import random as r

sayi = r.randint(1,100)

print(" Texmin oyunu ")

print("Reqemi 0-100 arasi secin")
while True :
    print("================")
    tahmin = int(input("Reqemi texmin edin"))

    if tahmin == sayi :
        print("***************")
        for i in range(10):
            print("Duzgun texmin etdiniz")
        print("***************")
        break

    elif tahmin < sayi :
        print("===============")
        print("Daha boyuk")

    elif tahmin > sayi :
        print("===============")
        print("Daha kicik")
