# Caesar Cipher - Encryption

text = input("Enter the message: ")
shift = int(input("Enter shift value: "))

result = ""

for char in text:
    if char.isalpha():   # check if it is a letter
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - base + shift) % 26 + base)
    else:
        result += char   # keep spaces/symbols as it is

print("Encrypted message:", result)
