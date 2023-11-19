#listeler
listem = ["araba","kamyon","minibus","otoubs","tir"]
print(len(listem))
print(listem[-2])
listem.append("motor")
print(listem)
listem.pop()
print(listem)

birinci_liste = [1,2,3]
ikinci_liste = [4,5,6]

if birinci_liste[1] == 2:
    birinci_liste[1] = 10

birinci_liste.extend(ikinci_liste)
print(birinci_liste)

birinci_liste = [1,2,3]
ikinci_liste = birinci_liste

print(birinci_liste)
print(ikinci_liste)

birinci_liste[0] = "kerem"
print(birinci_liste)
print(ikinci_liste)

# [:]
listem = [1,2,3,4,5,6,7,8,9,10]
print(listem[0:2])
print(listem[0:5:2])

listem = [1,2,3,4,5,6,7,8,9,10]

listem_2 = listem[:]
print(listem_2)

listem = [1,2,3,4,5,6,7,8,9,10]
isim = "kerem"
print(len(isim))

for isim_index in range(len(isim)):
    if isim_index == 0:
        print(isim[isim_index].upper())
    else:
        print(isim[isim_index])


listem = ["araba","minibus","kamyon","motor"]
for i,eleman in enumerate(listem):
    print(i,eleman)

sayi_1 = 2
sayi_2 = 5

while True:
    for i in range(5):
        break
    print("Captcha bulund")
    break

listem = ["araba","minibus","kamyon","motor"]

print(listem[::-1])


def zam_hesapla(maas=100):
    if type(maas) == str:
        return False

    yeni_maas = maas + (maas * 40 / 100)
    return yeni_maas


yeni_maasim = zam_hesapla("asdasc")
print(yeni_maasim)


# Algorithm Challenge
# Faktoriyel hesaplayan fonksiyon, kullanicidan 1 sayi alir
# 6! = 6.5.4.3.2.1

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)


# n = 5, 5 * faktroriyel(4) -> 120
# n = 4, 4 * faktoriyel(3) -> 24
# n = 3, 3 * faktoriyel (2) -> 2
# n = 2 , 2 * faktoriyel(1) -> 1
# n = 1 -> 1

def faktoriyel_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)


print(faktoriyel(5))


# Asal sayi bulma
# Verilen sayiya kadar olan asal sayilari yazdiran fonksiyon
# sayi = 20 -> 1,3,5,7...
def asal_sayi_yazdir(sayi):
    pass

#Asal sayi bulma cozumu
def asal_mi(sayi):
    if sayi < 2:
        return False
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                return False
    return True

def asal_sayilari_yazdir(x):
    for sayi in range(2,x+1):
        if asal_mi(sayi) == True:
            print(sayi)

asal_sayilari_yazdir(20)


# Verilen metin tersten aynisi mi veren fonksiyon
# ama = ama -> return True
# kerem = merek -> return False
def tersten_metin(metin):
    if metin[::-1] == metin:
        return True
    return False


print(tersten_metin("ama"))
print(tersten_metin("kerem"))

