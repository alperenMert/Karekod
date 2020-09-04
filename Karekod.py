# Kullanıcın verdiği yazıyı karekoda dönüştürerek kayıt etmek

import urllib.parse
import urllib.request

try:
    # resim boyutu
    size = input("Resim boyutu girin: ")
    # kod içerisinde yer almasını istediğimiz veri
    veri = input("içerik: ")

    veriler = {
        'size': size + "x" + size,
        'data': veri
    }

    # verileri şifreledik
    parametre = urllib.parse.urlencode(veriler)

    # Api linki oluşturduk
    link = "http://api.qrserver.com/v1/create-qr-code/?" + parametre

    # resim dosyasının indirilmesi
    urllib.request.urlretrieve(link, "kare_kod.png")

    print("\n")
    print("Karekod başarıyla oluşturuldu")

except:
    print("Beklenmeyen bir hata oluştu.")
