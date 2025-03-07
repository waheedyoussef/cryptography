import string

# Function to create the 5x5 Playfair matrix
def create_playfair_matrix(keyword):
    # Remove duplicate letters from the keyword
    keyword = keyword.upper().replace("J", "I")
    keyword = "".join(dict.fromkeys(keyword))

    # Create the matrix
    matrix = []
    for char in keyword:
        if char not in matrix:
            matrix.append(char)

    # Fill the remaining spaces with the rest of the alphabet (excluding 'J')
    for char in string.ascii_uppercase:
        if char not in matrix and char != "J":
            matrix.append(char)

    # Reshape into a 5x5 matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

# Function to prepare the plaintext for encryption
def prepare_text(text):
    text = text.upper().replace(" ", "").replace("J", "I")
    # Insert 'X' between duplicate letters in the same pair
    prepared_text = ""
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                prepared_text += "X"
                i += 1
            else:
                prepared_text += text[i + 1]
                i += 2
        else:
            prepared_text += "X"  # Add 'X' if the last pair has an odd number of letters
            i += 1
    return prepared_text

# Function to find the position of a letter in the matrix
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return (row, col)
    return None  # Return None if the letter is not found

# Function to encrypt a pair of letters
def encrypt_pair(matrix, pair):
    pos1 = find_position(matrix, pair[0])
    pos2 = find_position(matrix, pair[1])

    if pos1 is None or pos2 is None:
        return pair  # Skip encryption if a character is not in the matrix

    (row1, col1), (row2, col2) = pos1, pos2

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle
        return matrix[row1][col2] + matrix[row2][col1]

# Function to decrypt a pair of letters
def decrypt_pair(matrix, pair):
    pos1 = find_position(matrix, pair[0])
    pos2 = find_position(matrix, pair[1])

    if pos1 is None or pos2 is None:
        return pair  # Skip decryption if a character is not in the matrix

    (row1, col1), (row2, col2) = pos1, pos2

    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle
        return matrix[row1][col2] + matrix[row2][col1]

# Function to encrypt plaintext
def encrypt(plaintext, matrix):
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        ciphertext += encrypt_pair(matrix, pair)
    return ciphertext

# Function to decrypt ciphertext
def decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        plaintext += decrypt_pair(matrix, pair)
    return plaintext

# Main function
def main():
    # Input the keyword
    keyword = input("Enter the keyword: ")

    # Create the Playfair matrix
    matrix = create_playfair_matrix(keyword)
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))

    # Choose encryption or decryption
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice == "E":
        plaintext = input("Enter the plaintext: ")
        ciphertext = encrypt(plaintext, matrix)
        print("Encrypted Text:", ciphertext)
    elif choice == "D":
        ciphertext = input("Enter the ciphertext: ")
        plaintext = decrypt(ciphertext, matrix)
        print("Decrypted Text:", plaintext)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()