# Monoalphabetic Cipher - Encryption

plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter the message: ").upper()
result = ""

for ch in text:
    if ch.isalpha():
        index = plain.index(ch)
        result += cipher[index]
    else:
        result += ch

print("Encrypted message:", result)
