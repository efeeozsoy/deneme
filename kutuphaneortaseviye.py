import os

kitapListe = list()

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış
"""


def KitapEkle(kitap: tuple, liste: list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı.")
    print("Ana menüye dönmek için 'enter'a basın.")


def kontrol(kitap: tuple, liste: list):
    if kitap in liste:
        return True
    else:
        return False


def kitapCikar(kitap: tuple, liste: list):
    if kontrol(kitap, liste):
        liste.remove(kitap)
        print("Kitap Çıkartıldı.")
        print("Ana menüye dönmek için 'enter'a basın.")
        input()
    else:
        print("Arattığınız kitap mevcut değil!")
        input()


def listele(liste: list):
    for i in liste:
        print("Kitap Adı:   {}     Yazar:    {} ".format(i[0], i[1]))
    print("Ana menüye dönmek için 'enter'a basın.")
    input()


while True:
    os.system("cls")
    print(menu)

    secim = input("İşleminizi seçiniz: ")

    if secim == "1":
        kitap_adi = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_adi, kitap_yazar)
        KitapEkle(kitap, kitapListe)


    elif secim == "2":
        kitap_adi = input("Kitabın Adı: ")
        kitap_yazar = input("Yazarın Adı: ")
        kitap = (kitap_adi, kitap_yazar)
        kitapCikar(kitap, kitapListe)

    elif secim == "3":
        listele(kitapListe)

    elif secim == "q" or secim == "Q":
        print("Yine bekleriz!")
        quit()
