# Function to encrypt the plaintext using the Monoalphabetic Substitution Cipher
def encrypt(plaintext, key):
    # Define the plaintext alphabet
    plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Create a dictionary to map plaintext characters to ciphertext characters
    encryption_map = dict(zip(plaintext_alphabet, key))

    # Convert the plaintext to uppercase and replace each character using the encryption map
    ciphertext = ''.join([encryption_map[char] if char != ' ' else ' ' for char in plaintext.upper()])
    
    return ciphertext

# Function to decrypt the ciphertext using the Monoalphabetic Substitution Cipher
def decrypt(ciphertext, key):
    # Define the plaintext alphabet
    plaintext_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Create a dictionary to map ciphertext characters back to plaintext characters
    decryption_map = dict(zip(key, plaintext_alphabet))

    # Convert the ciphertext to uppercase and replace each character using the decryption map
    plaintext = ''.join([decryption_map[char] if char != ' ' else ' ' for char in ciphertext.upper()])
    
    return plaintext

# Main function to drive the program
def main():
    # Ask the user to input the operation (Encrypt or Decrypt)
    operation = input("Do you want to encrypt or decrypt? (E/D): ").strip().lower()

    # Ask the user to input the cipher key (should be 26 characters, no duplicates)
    key = input("Enter the 26-character key (Ciphertext Alphabet): ").strip().upper()
    
    # Check if the key is valid (26 characters, no duplicates)
    if len(key) != 26 or len(set(key)) != 26:
        print("Invalid key! The key must be 26 characters long with no duplicates.")
        return

    # Ask for the message to encrypt or decrypt
    message = input("Enter your message: ").strip()

    # Perform the chosen operation
    if operation == 'e':
        encrypted_message = encrypt(message, key)
        print(f"Encrypted message: {encrypted_message}")
    elif operation == 'd':
        decrypted_message = decrypt(message, key)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid operation! Please choose either 'E' for encrypt or 'D' for decrypt.")

# Run the program
if __name__ == "__main__":
    main()




