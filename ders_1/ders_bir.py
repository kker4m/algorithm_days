# int - integer = tam sayilarimiz
# float = 3.14 , 2.6
# string - str = "ihsan", 'kerem'
# boolean - bool = True, False, 1, 0

print(3)
print("kerem")
print(True)
print(3.14)

pi_sayisi = 3.14
sayi = 5
print(pi_sayisi*sayi)

#Yanlis
f = 40
m = 2000

#String matematiksel islemler hata gosterimi
not_1 = input("notunu gir:")
#Hata verir!
#print(not_1 * 40 / 100)

#String ile matematiksel islemler
ad = "kerem"
soyad = "izmir"
print((ad + " ") * 3)
print(ad + " "+soyad)

#Islem onceligi
#   P arantez
#   U slu sayilara
#   B olme islemleri
#   C arpma
#   E kleme
#   C ikarma

#Int sayilarla matematiksel islemler
sayi = int(input("Sayini gir : "))
print(sayi / 2)
print(sayi * 30)


#type fonksiyonu
ad = str(input("Isiminizi giriniz:  "))
sayi = int(input("Sayi girinzi: "))
ondalikli_sayi = float(input("ondalikli sayi girinzi: "))

tam_sayi = str(20)

print(type(ad))
print(type(sayi))
print(type(ondalikli_sayi))
print(type(tam_sayi))

#String ve integer toplama islemi
tam_sayi = str(20)
ad = "kerem"
print(ad + tam_sayi)

#String metodlari devami
ad = "haci"
print(ad.upper())
isim = "FURKAN"
print(isim.lower())

isim = "Kerem Mert"
print(isim.capitalize())
print(isim.replace(" ",","))

# ==
# <
# >
# >=
# <=
# !=
# %
sayi_1 = 5
sayi_2 = 13
sayi_3 = 44
sayi_4 = 13

print(sayi_1 > sayi_2)
print(sayi_2 > sayi_1)
#Esit miidr
print(sayi_2 == sayi_4)
#esit degil midir
print(sayi_2 != sayi_4)

sayi_1 = 20
sayi_2 = 13
sayi_3 = 44
sayi_4 = 13
#and
#not
#or
    #False
if not (sayi_2 > sayi_1):
    print("if calisti")
else:
    print("herhangi bi sey")


sayi_1 = 20
sayi_2 = 40
sayi_3 = 44
sayi_4 = 13
sayi_5 = 160

if (sayi_2 > sayi_1):
    print("if calisti")
elif (sayi_3 > sayi_1):
    print("elif-1 calisti")
elif (sayi_4 > sayi_5):
    print("elif-2 calisti")
else:
    print("else calisti, program kapandi")