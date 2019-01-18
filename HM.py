s1 = int(input(" İlk Reqem =>"))
s2 = int(input(" Ikinci Reqem =>"))
islem = input(" Hesab emellerinden birini secin (+,-,*,/)")
if islem == "+":
    sonuc = s1 + s2
    print(sonuc)

elif islem == "-":
    sonuc = s1 - s2
    print(sonuc)
elif islem == "*":
    sonuc = s1 * s2
    print(sonuc)
elif islem == "/":
    sonuc = s1 / s2
    print(sonuc)
else:
    print('xeta')
