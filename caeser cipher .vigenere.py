import string

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char3
    return result

def vigenere_cipher(text, key, encrypt=True):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            shift = shift if encrypt else -shift
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

def caesar_brute_force(ciphertext):
    print("Attempting to brute-force Caesar Cipher:")
    for shift in range(1, 26):
        print(f"Shift {shift}: {caesar_cipher(ciphertext, shift, encrypt=False)}")

def vigenere_break(ciphertext):
    print("Breaking Vigenere Cipher requires frequency analysis or a known-plaintext attack, which is complex.")
    print("Consider using a frequency analysis tool like Kasiski Examination or Index of Coincidence.")

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    cipher_type = input("Choose encryption method: Caesar (c) or Vigenere (v): ").strip().lower()
    
    if cipher_type == 'c':
        if choice == 'e':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: ")) #write as key better than shift
            print("Encrypted text:", caesar_cipher(text, shift))
        elif choice == 'd':
            text = input("Enter text to decrypt: ")
            shift = input("Enter shift value (leave blank to brute-force): ")
            if shift:
                print("Decrypted text:", caesar_cipher(text, int(shift), encrypt=False))
            else:
                caesar_brute_force(text)
    
    elif cipher_type == 'v':
        if choice == 'e':
            text = input("Enter text to encrypt: ")
            key = input("Enter key: ")
            print("Encrypted text:", vigenere_cipher(text, key))
        elif choice == 'd':
            text = input("Enter text to decrypt: ")
            key = input("Enter key (leave blank if unknown): ")
            if key:
                print("Decrypted text:", vigenere_cipher(text, key, encrypt=False))
            else:
                vigenere_break(text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
