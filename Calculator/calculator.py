giriş="""
Hesap makinesi uygulamasına hoş geldiniz.
"""
print(giriş)

calculate="""
1-) Toplama

2-) Çıkarma

3-) Çarpma

4-) Bölme

5-) Kuvvet Bulma

6-) Karekök Bulma
"""
print(calculate)

while True:
    soru=input("Lütfen yapmak istediğiniz işlem numarasını yazınız(Çıkmak için Q): ")
    if soru=="Q":
        print("Uygulamadan çıkış yapılıyor.")
        break
    elif soru=="1":
        t1=input("İlk sayıyı giriniz: ")
        t2=input("İkinci sayıyı giriniz: ")
        try:
            t_1=int(t1)
            t_2=int(t2)
            print(t_1+t_2)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")
    elif soru=="2":
        c1=input("İlk sayıyı giriniz: ")
        c2=input("İkinci sayıyı giriniz: ")
        try:
            c_1=int(c1)
            c_2=int(c2)
            print(c_1-c_2)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")
    elif soru=="3":
        p1=input("İlk sayıyı giriniz: ")
        p2=input("İkinci sayıyı giriniz: ")
        try:
            p_1=int(p1)
            p_2=int(p2)
            print(p_1*p_2)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")
    elif soru=="4":
        b1=input("Bölünen sayıyı giriniz: ")
        b2=input("Bölen sayıyı giriniz: ")
        try:
            b_1=int(b1)
            b_2=int(b2)
            print(b_1/b_2)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")
        except ZeroDivisionError:
            print("Sıfır Bölüm Hatası : Sayıları sıfıra bölemezsiniz!!!")
    elif soru=="5":
        k1=input("Hesaplanacak sayıyı giriniz: ")
        k2=input("Hesaplanacak kuvveti giriniz: ")
        try:
            k_1=int(k1)
            k_2=int(k2)
            print(k_1**k_2)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")
    elif soru=="6":
        r1=input("Hesaplanacak sayıyı giriniz: ")
        try:
            r_1=int(r1)
            print(r_1**0.5)
        except ValueError:
            print("Sadece sayı girebilirsiniz.")