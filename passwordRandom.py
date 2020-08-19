import argparse
import random

parola=[]
kucukHarfler = "abcdefghijklmnopqrstuvwxyz"
buyukHarfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "0123456789"
ozelKarakterler = "!@#$%&*._"

ap = argparse.ArgumentParser(description="Parola oluşturucu")
ap.add_argument("-u", "--uzunluk", help="Oluşturulacak parolanın karakter uzunluğu (Varsayılan=8)", default=8, type=int)
ap.add_argument("-t", "--tip", help="Oluşturulacak parolanın hangi karakter tiplerinden oluşacağı\n küçük harf: k ,büyük harf: b ,sayı: s , özel karakter : o (Varsayılan=kbso)",
                default="kbso")

a = ap.parse_args()

#print(''.join(random.choice(charaters[a.tip]) for i in range(int(a.uzunluk))))

while a.uzunluk > len(parola):
    if "k" in a.tip:
        parola.append(random.choice(kucukHarfler))
    if a.uzunluk == len(parola):
        break
    if "b" in a.tip:
        parola.append(random.choice(buyukHarfler))
    if a.uzunluk == len(parola):
        break
    if "s" in a.tip:
        parola.append(random.choice(sayilar))
    if a.uzunluk == len(parola):
        break
    if "o" in a.tip:
        parola.append(random.choice(ozelKarakterler))
    if a.uzunluk == len(parola):
        break

random.shuffle(parola)
listToStr = ''.join(map(str, parola))
print(listToStr)
