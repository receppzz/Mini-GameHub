import random

# ------------------------------
# Oyun 1: Sayı Tahmin
# ------------------------------
def sayi_tahmin():
    sayi = random.randint(1, 100)
    hak = 5
    print("\n🎯 1-100 arası sayıyı tahmin et!")

    while hak > 0:
        try:
            tahmin = int(input("Tahminin: "))
        except ValueError:
            print("Lütfen sayı gir!")
            continue

        if tahmin == sayi:
            print("🎉 Doğru tahmin!")
            return
        elif tahmin < sayi:
            print("Daha büyük söyle!")
        else:
            print("Daha küçük söyle!")
        hak -= 1

    print(f"❌ Hakkın bitti! Sayı: {sayi}")

# ------------------------------
# Oyun 2: Yazı-Tura
# ------------------------------
def yazi_tura():
    secim = input("\nYazı mı Tura mı?: ").lower()
    if secim not in ["yazı", "tura"]:
        print("Geçersiz seçim!")
        return

    sonuc = random.choice(["yazı", "tura"])
    print("Sonuç:", sonuc)
    if secim == sonuc:
        print("Kazandın 🎉")
    else:
        print("Kaybettin 😅")

# ------------------------------
# Oyun 3: Zar Atma
# ------------------------------
def zar_atma():
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    print(f"🎲 Zarlar: {zar1} - {zar2}")

# ------------------------------
# Oyun 4: Hesap Makinesi
# ------------------------------
def hesap_makinesi():
    try:
        a = float(input("1. sayı: "))
        b = float(input("2. sayı: "))
    except ValueError:
        print("Lütfen sayı gir!")
        return

    islem = input("İşlem (+ - * /): ")

    if islem == "+":
        print("Sonuç:", a + b)
    elif islem == "-":
        print("Sonuç:", a - b)
    elif islem == "*":
        print("Sonuç:", a * b)
    elif islem == "/":
        if b != 0:
            print("Sonuç:", a / b)
        else:
            print("❌ Sıfıra bölünemez!")
    else:
        print("Geçersiz işlem!")

# ------------------------------
# Ana Menü
# ------------------------------
def menu():
    while True:
        print("\n🎮 Python Oyun Paketi")
        print("1 - Sayı Tahmin Oyunu")
        print("2 - Yazı Tura")
        print("3 - Zar Atma")
        print("4 - Hesap Makinesi")
        print("q - Çıkış")

        secim = input("Seçimin: ")

        if secim == "1":
            sayi_tahmin()
        elif secim == "2":
            yazi_tura()
        elif secim == "3":
            zar_atma()
        elif secim == "4":
            hesap_makinesi()
        elif secim == "q":
            print("Oyun paketi kapatılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    menu()
