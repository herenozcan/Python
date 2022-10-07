import random
def hangman():

    words = random.choice(["zeynep", "windows", "linux", "debian", "ubuntu", "fedora", "arch", "python", "javascript", "whatsapp" ])
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Hak = 10
    tahmininiz = ''

    while len(words) > 0:
        kelime = ""
        hatalitahmin = 0

        for harf in words:
            if harf in tahmininiz:
                kelime = kelime + harf
            else:
                kelime = kelime + "_" + " "
        if kelime == words:
            print(kelime)
            print("Tebrikler kazandınız")
            break

        print("Kelimeyi tahmin ediniz:" , kelime)
        tahmin = input()

        if tahmin in alphabet:
            tahmininiz = tahmininiz + tahmin
        else:
            print("girdiğiniz harfi kontrol edin")
            tahmin = input()

        if tahmin not in words:
            Hak = Hak - 1
            if Hak == 9:
                print("9 hakkınız kaldı")
                print("  --------  ")
            if Hak == 8:
                print("8 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
            if Hak == 7:
                print("7 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if Hak == 6:
                print("6 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if Hak == 5:
                print("5 hakkınız kaldı")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if Hak == 4:
                print("4 hakkınız kaldı")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if Hak == 3:
                print("3 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if Hak == 2:
                print("2 hakkınız kaldı")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if Hak == 1:
                print("1 hakkınız kaldı")
                print("Dikkatli kullanın")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if Hak == 0:
                print("Oyun bitti")
                print("bilemediniz ve kaybettiniz")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


print("Kelimeyi bulabilmek için 10 hakkınız var")
hangman()
print()