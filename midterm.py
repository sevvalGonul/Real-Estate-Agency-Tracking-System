"""
Değikenin adının başında d_ ya da danisman_ olması o değişkenin sadece döngünün her dönüşünde değişen danışmanların
istatiksel verilerini hesaplamada kullanılacağını, top_ ya da toplam_ olması ise o değişkenin bütünü yani veri kümesini
ilgilendiren istatiksel hesaplamalarda kullanılacağını belirtmektedir. İç döngüden çıkıldıktan sonra dış döngüde bir
tur daha atmaya geçmeden önce yapılması gerekenler(iç döngüden çıkılır çıkılmaz yapılması gerekenler) danışmana ait
veriler ekrana yazdırıldıktan hemen sonra yapılmıştır.

"""

ASGARI_UCRET = 2324.70  # TL
KOTA_KATSAYISI = 10  # Danışmanın kotası, maaşının 10 katı ya da daha büyük olmalı
SATIS_KOMISYON_KATSAYISI = 0.04 # Emlak acentesi yapılan her satış için satış bedelinin %4'ü kadar ücret kazanır.(Satış için emlak komisyonu)
PRIM_KATSAYISI = 0.1 # Emlak acentesi danışmanlarının maaşlarına ek olarak kazandırdıkları emlak komisyonunun %10'u kadar prim öder.
IKRAMIYE = ASGARI_UCRET / 2  # Emlak acentesinin, danışmanlarının kotalarını doldurma durumunda ödediği ek ücret
HATA_UYARISI = "Hatalı veri, lütfen tekrardan giriniz: "

danisman_sayisi = int(input("Lütfen emlak acentesine bağlı olarak çalışan emlak danışmanı sayısını giriniz(0 ya da negatif olamaz): "))
while danisman_sayisi <= 0:
    danisman_sayisi = int(input(HATA_UYARISI))

top_satilan_konut_adedi = 0
top_satilan_arsa_adedi = 0
top_satilan_emlak_adedi = 0
top_kiralanan_emlak_adedi = 0
top_kiralanan_konut_adedi = 0
top_kiralanan_arsa_adedi = 0

top_satilan_arsa_bedeli = 0
top_satilan_konut_bedeli = 0
top_satilan_isyeri_bedeli = 0

max_satis_bedeli = 0 #O ay en yüksek bedelle satılan emlağın satış bedeli

max_konut_kira = 0 #O ay en yüksek bedelle kiralanan konutun kira bedeli

asgariden_yuksek_kiralik_konut_say = 0

hic_satis_yapamayan_danisman_say = 0

max_top_satis_adeti = 0 #O ay en çok sayıda satış yapan danışmanın toplam satış adeti
max_top_satis_bedeli = 0 #O ay satış bedeli olarak en çok satış yapan danışmanın toplam satış bedeli

top_kota_dolduran_danisman_say = 0

primi_maasindan_yuksek_say = 0  # Primi maaşından yüksek olan danışmanların sayısı

fazla_kiralayan_danisman_say = 0  # o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı

top_ucret_toplam = 0  # Emlak acentesinin danışmanlarına ödeyeceği toplam ücretlerin toplamı

toplam_komisyon = 0

max_prim = 0

for sayac in range(1,danisman_sayisi+1):
    ad_soyad = input(str(sayac) + ". emlak danışmanının adını ve soyadını giriniz: ")
    maas = float(input(str(sayac) + ". emlak danışmanının maaşını TL cinsinden giriniz(Asgari ücret veya daha fazla olmalı): "))
    while maas < ASGARI_UCRET:
        maas = float(input(HATA_UYARISI))
    kota = float(input("Kotayı TL cinsinden giriniz(Danışmanın maaşının 10 katı ya da daha büyük olmalı): "))
    while kota < maas * KOTA_KATSAYISI:
        kota = float(input(HATA_UYARISI))

    d_max_konut_kira = 0 #Danışmanın o ay en yüksek bedelle kiraladığı konutun kira bedeli
    danisman_top_kira_bedeli = 0 #Danışmanın o ay kiraladığı bütün emlaklardan acenteye kazandırdığı bedel
    d_satilan_konut_bedeli = d_satilan_is_yeri_bedeli = d_satilan_arsa_bedeli = 0 #Bir danışmanın bu emlak tiplerini satarak kazandırdığı TOPLAM BEDELLER
    d_satilan_emlak_adedi = 0 #Danışmanın sattığı toplam emlak adedi
    d_kiralanan_emlak_adedi = 0 #Danışmanın kiraladığı toplam emlak adedi
    d_top_konut_kira_bedeli = 0 #Danışmanın bu ay kiraladığı konutların toplam bedeli
    d_kiralik_konut_say = 0 #Danışmanın bu ay kiraladığı konut sayısı
    satis_yapti_mi = False

    devam = "e"
    while devam == "e" or devam == "E":
        emlak_tipi = input("Satılan ya da kiralanan emlak tipini giriniz(Konut:K/k, İş yeri:İ/i, Arsa:A/a): ")
        while emlak_tipi not in ["K","k","İ","i","A","a"]:
            emlak_tipi = input(HATA_UYARISI)

        islem_turu = input("İşlem türünü giriniz(Satış:S/s, Kiralama:K/k): ")
        while islem_turu not in ["S","s","K","k"]:
            islem_turu = input(HATA_UYARISI)

        satis_kira_bedeli = float(input("Satılan veya kiralanan emlağın TL cinsinden bedelini giriniz(O'dan büyük): "))
        while satis_kira_bedeli <= 0:
            satis_kira_bedeli = float(input(HATA_UYARISI))

        # Bu if'e girerse emlak satılmıştır ve satis_kira_bedeli aslında satış bedelidir.
        if islem_turu == "S" or islem_turu == "s": # Satılan emlak ise:
            satis_yapti_mi = True
            d_satilan_emlak_adedi += 1
            #  O ay en yüksek bedelle satılan emlağın tipini, bedelini, satışı yapan danışmanın adını soyadını bulma
            if satis_kira_bedeli > max_satis_bedeli:
                max_satis_bedeli = satis_kira_bedeli
                max_satis_emlak_tipi = emlak_tipi
                max_satis_danisman = ad_soyad

            if emlak_tipi == "K" or emlak_tipi == "k":  # Satılan bir konut ise:
                d_satilan_konut_bedeli += satis_kira_bedeli
                top_satilan_konut_adedi += 1
            elif emlak_tipi == "İ" or emlak_tipi == "i":  # Satılan bir iş yeri ise:
                d_satilan_is_yeri_bedeli += satis_kira_bedeli
            else:  # Satılan bir arsa ise:
                d_satilan_arsa_bedeli += satis_kira_bedeli
                top_satilan_arsa_adedi += 1

        # else'e girerse emlak kiralanmıştır ve satis_kira_bedeli aslında kira bedelidir.
        else:  # Kiralanan emlak ise:
            d_kiralanan_emlak_adedi += 1
            danisman_top_kira_bedeli += satis_kira_bedeli
            # Bu if'e girerse satis_kira_bedeli aslında kiralanan bir konutun kira bedelidir.
            if emlak_tipi == "K" or emlak_tipi == "k": #Kiralanan bir konut ise:
                d_top_konut_kira_bedeli += satis_kira_bedeli
                d_kiralik_konut_say += 1

                # Danışmanın o ay en yüksek bedelle kiraladığı konutun kira bedelini bulma:
                if satis_kira_bedeli > d_max_konut_kira:
                    d_max_konut_kira = satis_kira_bedeli

                 # O ay kiralanan konutlardan kira bedeli asgari ücretten büyük olanların sayısını bulma:
                if satis_kira_bedeli > ASGARI_UCRET:
                    asgariden_yuksek_kiralik_konut_say += 1

            elif emlak_tipi == "A" or emlak_tipi == "a": #Kiralanan bir arsa ise:
                top_kiralanan_arsa_adedi += 1


        devam = input(str(sayac) + ".danışmanın bu ay sattığı veya kiraladığı başka emlak var mı? (Evet:E/e, Hayır:H/h): ")
        while devam not in ["E","e","H","h"]:
            devam = input(HATA_UYARISI)


    danisman_top_satis_bedeli = d_satilan_konut_bedeli + d_satilan_is_yeri_bedeli + d_satilan_arsa_bedeli
    danisman_emlak_komisyonu = danisman_top_satis_bedeli * SATIS_KOMISYON_KATSAYISI + danisman_top_kira_bedeli
    prim = danisman_emlak_komisyonu * PRIM_KATSAYISI
    d_toplam_emlak_adeti = d_satilan_emlak_adedi + d_kiralanan_emlak_adedi

    print("Emlak danışmanının adı soyadı:", ad_soyad)
    print("Bu ay sattığı emlak adedi: {}, kiraladığı emlak adedi: {}, satilan emlakların oranı: %{}, kiralanan emlakların oranı: %{}"
        .format(d_satilan_emlak_adedi, d_kiralanan_emlak_adedi,
                format(d_satilan_emlak_adedi*100/d_toplam_emlak_adeti,".2f"), format(d_kiralanan_emlak_adedi*100/d_toplam_emlak_adeti,".2f")))
    print("Bu ay sattığı konutların toplam bedeli:", format(d_satilan_konut_bedeli, ",.2f"), "TL")
    print("Bu ay sattığı arsaların toplam bedeli:", format(d_satilan_arsa_bedeli, ",.2f"), "TL")
    print("Bu ay sattığı iş yerlerinin toplam bedeli:", format(d_satilan_is_yeri_bedeli,",.2f"),"TL")
    print("Bu ay kiraladığı konutların ortalama kira bedeli:", format(d_top_konut_kira_bedeli/d_kiralik_konut_say,",.2f"),"TL")
    print("Bu ay en yüksek bedelle kiraladığı konutun kira bedeli:", format(d_max_konut_kira,",.2f"), "TL")
    print("Emlak danışmanının bu ayki maaşı:", format(maas,",.2f"), "TL")
    print("Emlak danışmanının bu ayki primi:", format(prim,",.2f"), "Tl")
    print("Emlak danışmanının bu ayki kotası:", format(kota, ",.2f"), "TL")
    print("Emlak danışmanının bu ay acentaya kazandırdığı toplam komisyon tutarı:", format(danisman_emlak_komisyonu,",.2f"), "TL")
    if danisman_emlak_komisyonu >= kota:  # Emlak danışmanı kotasını doldurmuşsa:
        top_kota_dolduran_danisman_say += 1
        d_aylik_top_ucret = maas + prim + IKRAMIYE
        print("Emlak danışmanı kotasını doldurdu ve alacağı ikramiye:", format(IKRAMIYE, ",.2f"), "TL")
        print("Emlak danışmanının bu ay alacağı toplam ücret:", format(d_aylik_top_ucret, ",.2f"), "TL")
    else:  # Emlak danışmanı kotasını dolduramamışsa:
        d_aylik_top_ucret = maas + prim
        print("Emlak danışmanı kotasını dolduramadı.")
        print("Emlak danışmanının bu ay alacağı toplam ücret:", format(d_aylik_top_ucret, ",.2f"), "TL")

    top_satilan_emlak_adedi += d_satilan_emlak_adedi
    top_kiralanan_emlak_adedi += d_kiralanan_emlak_adedi
    top_kiralanan_konut_adedi += d_kiralik_konut_say

    top_satilan_arsa_bedeli += d_satilan_arsa_bedeli
    top_satilan_konut_bedeli += d_satilan_konut_bedeli
    top_satilan_isyeri_bedeli += d_satilan_is_yeri_bedeli

    # Tüm veriler için o ay en yüksek bedelle kiralanan konutun kira bedeli ve kiralayan danışmanın adı soyadı
    if d_max_konut_kira > max_konut_kira:
        max_konut_kira = d_max_konut_kira
        max_bedelli_konut_kiralayan = ad_soyad

    if satis_yapti_mi == False:
        hic_satis_yapamayan_danisman_say += 1

    # Tüm veriler için en çok adette satış yapan danışman için:
    if d_satilan_emlak_adedi > max_top_satis_adeti:
        max_top_satis_adeti = d_satilan_emlak_adedi
        satis_adeti_max_danisman = ad_soyad
        satis_adeti_max_danismanin_top_satis_bedeli = danisman_top_satis_bedeli

    # Tüm veriler için en çok satış bedeli kazandıran danışman için:
    if danisman_top_satis_bedeli > max_top_satis_bedeli:
        max_top_satis_bedeli = danisman_top_satis_bedeli
        satis_bedeli_max_danisman = ad_soyad
        satis_bedeli_max_danismanin_top_satis_adeti = d_satilan_emlak_adedi

    if prim > maas:
        primi_maasindan_yuksek_say += 1

    if d_kiralanan_emlak_adedi >= 10 or danisman_top_kira_bedeli >= 25000:
        fazla_kiralayan_danisman_say += 1

    # Primin alabileceği en büyük değeri bilmediğim için min_prim'e kafadan değer atamak doğru olmazdı.
    # Bu yüzden ilk danışmanın prim değerini min değişkenine atadım.
    if sayac == 1:
        min_prim = prim
        min_prim_ad_soyad = ad_soyad
        min_prim_maas = maas
        min_prim_top_ucret = d_aylik_top_ucret

    if prim > max_prim:
        max_prim = prim
        max_prim_ad_soyad = ad_soyad
        max_prim_maas = maas
        max_prim_top_ucret = d_aylik_top_ucret
    elif prim < min_prim:
        min_prim = prim
        min_prim_ad_soyad = ad_soyad
        min_prim_maas = maas
        min_prim_top_ucret = d_aylik_top_ucret

    top_ucret_toplam += d_aylik_top_ucret  # O ay tüm satış danışmanlarına ödenecek toplam ücretlerin toplamı
    toplam_komisyon += danisman_emlak_komisyonu  # Emlak acentesinin kazandığı toplam komisyon tutarı


top_satilan_isyeri_adedi = top_satilan_emlak_adedi - (top_satilan_arsa_adedi + top_satilan_konut_adedi)
top_kiralanan_isyeri_adedi = top_kiralanan_emlak_adedi - (top_kiralanan_konut_adedi + top_kiralanan_arsa_adedi)

print("Bu ay satılan toplam arsa sayısı:", top_satilan_arsa_adedi, ", kiralanan arsa sayısı:", top_kiralanan_arsa_adedi,
      "ve arsaların satılma oranı: %", format(top_satilan_arsa_adedi*100/(top_satilan_arsa_adedi+top_kiralanan_arsa_adedi),".2f"))
print("Bu satılan toplam konut sayısı:", top_satilan_konut_adedi,", kiralanan konut sayısı:", top_kiralanan_konut_adedi,
      "ve konutların satılma oranı: %", format(top_satilan_konut_adedi*100/(top_satilan_konut_adedi+top_kiralanan_konut_adedi),".2f"))
print("Bu ay satılan toplam iş yeri sayısı:", top_satilan_isyeri_adedi, ", kiralanan iş yeri sayısı:", top_kiralanan_isyeri_adedi,
      "ve iş yerlerinin satılma oranı: %", format(top_satilan_isyeri_adedi*100/(top_satilan_isyeri_adedi+top_kiralanan_isyeri_adedi),".2f"))

print("Bu ay satılan arsaların toplam bedelleri:", format(top_satilan_arsa_bedeli, ",.2f"),
      "TL ve satılan arsaların ortalama satış bedelleri:",
      format(top_satilan_arsa_bedeli/top_satilan_arsa_adedi, ",.2f"), "TL")

print("Bu ay satılan konutların toplam bedelleri:", format(top_satilan_konut_bedeli, ",.2f"),
      "TL ve satılan konutların ortalama satış bedelleri:",
      format(top_satilan_konut_bedeli/top_satilan_konut_adedi, ",.2f"), "TL")

print("Bu ay satılan iş yerlerinin toplam bedelleri:", format(top_satilan_isyeri_bedeli, ",.2f"),
      "TL ve satılan iş yerlerinin ortalama satış bedelleri:",
      format(top_satilan_isyeri_bedeli/top_satilan_isyeri_adedi, ",.2f"), "TL")

print("Bu ay en yüksek bedelle satılan emlağın tipi: ", end="")
if max_satis_emlak_tipi == "i" or max_satis_emlak_tipi == "İ":
    print("İş Yeri", end=" ")
elif max_satis_emlak_tipi == "K" or max_satis_emlak_tipi == "k":
    print("Konut", end=" ")
else:
    print("Arsa", end=" ")
print(", satış bedeli:", format(max_satis_bedeli,",.2f"),"TL ve bu satışı yapan danışmanın adı soyadı:", max_satis_danisman)

print("Bu ay en yüksek bedelle kiralanan konutun kira bedeli:", format(max_konut_kira, ",.2f"),
      "TL ve kiralamayı yapan danışmanın adı soyadı:", max_bedelli_konut_kiralayan)

print("Bu ay kiralanan konutlardan kira bedeli, aylık net asgari ücretten yüksek olan konutların sayısı:",
      asgariden_yuksek_kiralik_konut_say, "ve kiralanan konutlar içindeki oranı: %",
      format(asgariden_yuksek_kiralik_konut_say*100/top_kiralanan_konut_adedi, ".2f"))

print("Bu ay hiç satış yapamayan danışmanların sayısı:", hic_satis_yapamayan_danisman_say, "ve tüm danışmanlar içindeki oranı: %",
      format(hic_satis_yapamayan_danisman_say*100/danisman_sayisi,".2f"))

print("Toplam satış adedi en çok olan danışmanın adı soyadı:", satis_adeti_max_danisman, ",sattığı emlak sayısı:",
      max_top_satis_adeti,"ve toplam satış bedeli:", format(satis_adeti_max_danismanin_top_satis_bedeli,",.2f"),"TL")

print("Toplam satış bedeli en çok olan danışmanın adı soyadı:", satis_bedeli_max_danisman, ",sattığı emlak sayısı:",
      satis_bedeli_max_danismanin_top_satis_adeti, "ve toplam satış bedeli:", format(max_top_satis_bedeli,",.2f"), "TL")

print("Bu ay kotasını dolduran danışmanların sayısı:", top_kota_dolduran_danisman_say, "ve tüm danışmanlar içindeki oranı: %",
      format(top_kota_dolduran_danisman_say*100/danisman_sayisi, ".2f"))

print("Bu ay primi maaşından yüksek olan danışmanların sayısı:", primi_maasindan_yuksek_say, "ve tüm danışmanlar içindeki oranı: %",
      format(primi_maasindan_yuksek_say*100/danisman_sayisi, ".2f"))

print("Bu ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:", fazla_kiralayan_danisman_say)

print("Bu ay en yüksek prim alan danışmanın adı soyadı:", max_prim_ad_soyad, ", maaşı:", format(max_prim_maas, ",.2f",),
      "TL, primi:", format(max_prim, ",.2f"), "TL ve aylık toplam ücreti:", format(max_prim_top_ucret, ",.2f"), "TL")
print("Bu ay en düşük prim alan danışmanın adı soyadı:", min_prim_ad_soyad, ", maaşı:", format(min_prim_maas,",.2f",),
      "TL, primi:", format(min_prim, ",.2f"), "TL ve aylık toplam ücreti:", format(min_prim_top_ucret,",.2f"), "TL")

print("Bu ay tüm satış danışmanlarına ödenecek toplam ücretlerin toplamı:", format(top_ucret_toplam, ",.2f"),
      "TL ve ortalaması:", format(top_ucret_toplam/danisman_sayisi, ",.2f"), "TL")

print("Bu ay acentenin kazandığı toplam komisyon:", format(toplam_komisyon, ",.2f"), "TL")







