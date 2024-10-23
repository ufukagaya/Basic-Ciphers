import argparse
import math

# Caesar Cipher
"""def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # shift all letters
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # nay char without letter is added directly

    file_path = "coded_caesar.txt"
    with open(file_path, "w") as f:
        f.write(encrypted_text)

    return encrypted_text"""


def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    shift = shift % 26
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_english_alphabet = english_alphabet[-shift:] + english_alphabet[:-shift]
    for char in plaintext:
        char_upper = char.upper()
        if char_upper in english_alphabet:  # shift all letters
            index = english_alphabet.index(char_upper)
            if char.isupper():
                encrypted_text += shifted_english_alphabet[index]
            else:
                encrypted_text += shifted_english_alphabet[index].lower()
        else:
            encrypted_text += char  # nay char without letter is added directly

    file_path = "coded_caesar.txt"
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(encrypted_text)

    return encrypted_text


"""def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text"""

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    shift = -(shift % 26)
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_english_alphabet = english_alphabet[-shift:] + english_alphabet[:-shift]
    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in english_alphabet:  # shift all letters
            index = english_alphabet.index(char_upper)
            if char.isupper():
                decrypted_text += shifted_english_alphabet[index]
            else:
                decrypted_text += shifted_english_alphabet[index].lower()
        else:
            decrypted_text += char  # nay char without letter is added directly
    return decrypted_text

# Affine
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i


# Affine Cipher
"""def encrypt_affine(plaintext, a, b):
    if gcd(a, 26) != 1:  # check if a and 26 are prime along them.
=======
def encrypt_affine(plaintext, a, b):
    if math.gcd(a, 26) != 1:  # check if a and 26 are prime along them.
>>>>>>> Stashed changes
        raise ValueError("a and 26 must be prime along them.")

    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - shift_base
            encrypted_char = chr(((a * x + b) % 26) + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    file_path = "coded_affine.txt"
    with open(file_path, "w") as f:
        f.write(encrypted_text)

    return encrypted_text"""


def encrypt_affine(plaintext, a, b):
    if math.gcd(a, 26) != 1:  # check if a and 26 are prime along them.
        raise ValueError("a and 26 must be prime along them.")

    encrypted_text = ""
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in plaintext:
        char_upper = char.upper()
        if char_upper in english_alphabet:
            index = english_alphabet.index(char_upper)
            new_index = (a * index + b) % 26
            encrypted_char = english_alphabet[new_index]
            if char.isupper():
                encrypted_text += encrypted_char
            else:
                encrypted_text += encrypted_char.lower()
        else:
            encrypted_text += char

    file_path = "coded_affine.txt"
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(encrypted_text)

    return encrypted_text


"""def decrypt_affine(ciphertext, a, b):
    if gcd(a, 26) != 1:
=======
def decrypt_affine(ciphertext, a, b):
    if math.gcd(a, 26) != 1:
>>>>>>> Stashed changes
        raise ValueError("a and 26 must be prime along them.")

    decrypted_text = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - shift_base
            decrypted_char = chr(((a_inv * (y - b)) % 26) + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text"""


def decrypt_affine(ciphertext, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a and 26 must be prime along them.")

    decrypted_text = ""
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    a_inv = mod_inverse(a, 26)
    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in english_alphabet:
            index = english_alphabet.index(char_upper)
            new_index = (a_inv * (index - b)) % 26
            decrypted_char = english_alphabet[new_index]
            if char.isupper():
                decrypted_text += decrypted_char
            else:
                decrypted_text += decrypted_char.lower()
        else:
            decrypted_text += char
    return decrypted_text


"""def encrypt_mono(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')  # Finding index of the word
            encrypted_char = key[index].upper() if char.isupper() else key[index].lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Chars that is not word were added directly

    file_path = "coded_mono.txt"
    with open(file_path, "w") as f:
        f.write(encrypted_text)

    return encrypted_text"""

def encrypt_mono(plaintext, key):
    encrypted_text = ""
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in plaintext:
        char_upper = char.upper()
        if char_upper in english_alphabet:
            index = english_alphabet.index(char_upper)
            encrypted_char = key[index]
            if char.isupper():
                encrypted_text += encrypted_char
            else:
                encrypted_text += encrypted_char.lower()
        else:
            encrypted_text += char

    file_path = "coded_mono.txt"
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(encrypted_text)

    return encrypted_text


"""def decrypt_mono(ciphertext, key):
    decrypted_text = ""
    reverse_key = {key[i]: chr(i + ord('A')) for i in range(26)}  # reverse the key
    for char in ciphertext:
        if char.isalpha():
            original_char = reverse_key[char.upper()]
            decrypted_char = original_char if char.isupper() else original_char.lower()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text"""


def decrypt_mono(ciphertext, key):
    decrypted_text = ""
    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in ciphertext:
        char_upper = char.upper()
        if char_upper in english_alphabet:
            index = key.index(char_upper)
            decrypted_char = english_alphabet[index]
            if char.isupper():
                decrypted_text += decrypted_char
            else:
                decrypted_text += decrypted_char.lower()
        else:
            decrypted_text += char
    return decrypted_text


# Main function to parse command line arguments
def main():
    global result
    parser = argparse.ArgumentParser(description="Affine Cipher Encryption/Decryption")
    parser.add_argument("cipher", choices=["caesar", "affine", "mono", "show"])
    parser.add_argument("file")
    parser.add_argument("mode", choices=["e", "d", "s"])
    parser.add_argument("-s", "--shift", type=int)
    parser.add_argument("-a", "--a", type=int)
    parser.add_argument("-b", "--b", type=int)
    parser.add_argument("-k", "--key", type=str)

    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return

    # Encryption/Decryption
    if args.cipher == "caesar":
        if args.mode == "e":
            result = encrypt_caesar(text, args.shift)
        elif args.mode == "d":
            result = decrypt_caesar(text, args.shift)
        else:
            print("Invalid mode")
            return
    elif args.cipher == "affine":
        if args.mode == "e":
            result = encrypt_affine(text, args.a, args.b)
        elif args.mode == "d":
            result = decrypt_affine(text, args.a, args.b)
        else:
            print("Invalid mode")
            return
    elif args.cipher == "mono":
        if args.mode == "e":
            if args.key:
                result = encrypt_mono(text, args.key.upper())
            else:
                print("Key has not specified.")
                return
        elif args.mode == "d":
            if args.key:
                result = decrypt_mono(text, args.key.upper())
            else:
                print("Key has not specified.")
                return
    elif args.cipher == "show":
        if args.mode == "s":
            result = text
    print("Result:")
    print(result)


if __name__ == '__main__':
    main()
