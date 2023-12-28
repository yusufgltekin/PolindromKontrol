'''
Girilen metnin tersten okunabilir olup olmadığını kontrol eder.
Parametre: metin; Polindrom kontrolü yapılacak metin
Döndürülen değerler:
True: Metin polindrom ise döndürülür
False: Metin polindrom değilse döndürülür.
'''

def polindromKontrol(metin):
    metin = metin.lower() #Büyük/küçük harf duyarlılığı giderilir.
    metin = metin.replace(" ","") #boşluklar temizlenir
    return metin == metin[::-1]

metin = ""
while metin != "-1":
    metin = input("Kontrol yapacağınız metni girin. Çıkmak için -1 girişi yapın: ")
    if(metin == "-1"):
        break
    polindromKontrol(metin)
    if polindromKontrol(metin):
        print(f"{metin}: Polindromdur.")
    else:
        print(f"{metin}: Polindrom değildir.")