def decrypt_message(ciphertext, shift):
    """
    Decrypts the ciphertext using a Caesar cipher shift.
    """
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back by the given shift value
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def brute_force_caesar(ciphertext):
    """
    Attempts to break a Caesar cipher using a brute-force approach.
    """
    print("Ciphertext:", ciphertext)
    print("Starting brute-force attack with all 26 possible shifts...")
    
    for shift in range(26):
        decrypted_text = decrypt_message(ciphertext, shift)
        print(f"Shift: {shift} -> Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    # Prompt the user to enter an encrypted message
    encrypted_message = input("Enter the encrypted message: ")
    
    # Remove spaces and non-alphabetic characters for simplicity
    encrypted_message = ''.join(filter(str.isalpha, encrypted_message))
    
    # Perform brute-force attack
    brute_force_caesar(encrypted_message)