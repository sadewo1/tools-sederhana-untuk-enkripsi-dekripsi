#!/usr/bin/env python3
# SimpleEncryptor: Edukasi Enkripsi & Dekripsi
# Bisa dijalankan di Termux dan Linux

def encrypt(text, key):
    """Enkripsi sederhana (Caesar Cipher)"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

def decrypt(cipher, key):
    """Dekripsi sederhana (Caesar Cipher)"""
    result = ""
    for char in cipher:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("=== SimpleEncryptor ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    choice = input("Pilih (1/2): ")

    text = input("Masukkan teks: ")
    key = int(input("Masukkan key (angka): "))

    if choice == "1":
        cipher = encrypt(text, key)
        print("Hasil Enkripsi:", cipher)
    elif choice == "2":
        plain = decrypt(text, key)
        print("Hasil Dekripsi:", plain)
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
