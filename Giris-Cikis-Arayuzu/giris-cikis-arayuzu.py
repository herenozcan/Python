def main():
    for deneme in range(2, -1, -1):
        sys_kullanici_adi = input("Kullanıcı Adı: ")
        if sys_kullanici_adi == "eren":
            print("Eşleşme Başarılı!")
            break
        else:
            if deneme == 0:
                print("Eşleşme Başarısız! Deneme hakkınız kalmadı. Sistemden çıkış yapılıyor...")
                quit()
            else:
                print(f"Eşleşme Başarısız! Lütfen tekrar deneyiniz. Kalan deneme hakkı: {deneme}")

    for deneme in range(2, -1, -1):
        sifre = input("Şifre: ")
        if sifre == "12345":
            print("Eşleşme Başarılı! Sistemden çıkış yapılıyor.")
            quit()
        else:
            if deneme == 0:
                print("Eşleşme Başarısız! Deneme hakkınız kalmadı. Sistemden çıkış yapılıyor...")
                quit()
            else:
                print(f"Eşleşme Başarısız! Lütfen tekrar deneyiniz. Kalan deneme hakkı: {deneme}")
main()