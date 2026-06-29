bakiye = 1000
while True:
    print("\n--- ATM İşlemleri ---")
    print("1. Para Yatırma")
    print("2. Para Çekme")
    print("3. Bakiye Sorgulama")
    print("4. Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == "1":
        miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
        bakiye += miktar
        print(f"{miktar} TL yatırıldı. Güncel bakiye: {bakiye} TL")
    elif secim == "2":
        miktar = float(input("Çekmek istediğiniz miktarı girin: "))
        if miktar <= bakiye:
            bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {bakiye} TL")
        else:
            print("Yetersiz bakiye.")
    elif secim == "3":
        print(f"Güncel bakiyeniz: {bakiye} TL")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")

öğrenci_listesi = []
while True:
    print("\n--- Öğrenci Kayıt Sistemi ---")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrenci Listesi")
    print("4. Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == "1":
        isim = str(input("Öğrencinin adını girin: "))
        if isim in öğrenci_listesi:
            print(f"{isim} adlı öğrenci zaten listede mevcut.")
        else:
            öğrenci_listesi.append(isim)

    elif secim == "2":
        isim = str(input("Silmek istediğiniz öğrencinin adını girin: "))
        if isim in öğrenci_listesi:
            öğrenci_listesi.remove(isim)
            print(f"{isim} adlı öğrenci silindi.")
        else:
            print(f"{isim} adlı öğrenci bulunamadı.")

    elif secim == "3":
        print("Öğrenci Listesi:")
        for öğrenci in öğrenci_listesi:
            print(f"- {öğrenci}")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
