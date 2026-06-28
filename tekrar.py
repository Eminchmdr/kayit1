kullanici_adi = input("lütfen adınızı girin :")
print(f"Merhaba {kullanici_adi},sayfamıza hoşgeldin")

yasiniz = int(input("lütfen yaşınızı giriniz : "))
print(yasiniz)

print("-----------Yaş hesaplama sistemine hoşgeldiniz---------")
yas = int(input("lütfen doğum yılınızı girniz :"))
yaşınız = (2026 - yas)
print(f"Tebrikler bugün itibariyle yaşınız {yaşınız}")

yas = int(input("Lütfen yaşınızı giriniz :"))
if yas > 18:
    print("Yaşınız mekana girmek için uygun hoşgeldiniz")
elif yas == 18:
    print("Yaşınız mekana girmek için kılpayı olarak uygun hoşgeldiniz :)")
else:
    print("maalesef yaşınız mekana girmek için uygun değil")

for sayi in range(1, 6):
    print(sayi)

sayac = 1
while sayac <= 19:
    print(f"Sayaç şu an: {sayac}")
    sayac = sayac + 1

for sayim in range(10, 0, -1):
    print(f"roketin fırlatılmasına kalan {sayim}")
print("tebrikler roket fırlatıldı")

sepet = ["ekmek", "süt", "yumurta"]
sepet.append("kereviz")
print("------------ALINACAKALAR------------")
for marketten in sepet:
    print(f"{marketten}")


def kahve_yap(x):
    print(f"{x} kahveniz hemen hazırlanıyor....")
    print("bolca ısıtılıyor lütfen bekleyin....")
    print(f"{x} hazır afiyetle için")


menu = ["latte", "türk kahvesi", "mocha", "americano", "dibek kahve"]
print("-----MENü-----")

for içerik in menu:
    print(f"{içerik}")

secim = input("Menümüzden hangi kahveyi almak istersiniz :")

if secim in menu:
    kahve_yap(secim)
else:
    print("maalesef seçtiğiniz kahve menümüzde bulunmuyor")
