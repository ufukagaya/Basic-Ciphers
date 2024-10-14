import argparse
from collections import Counter
from ciphers import decrypt_caesar, decrypt_affine


def break_caesar(ciphertext):
    potential_decryptions = []
    for shift in range(26):  # try from 0 to 25
        decrypted_text = decrypt_caesar(ciphertext, shift)
        potential_decryptions.append((shift, decrypted_text))
    return potential_decryptions


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def get_valid_a_b_pairs(m):
    valid_pairs = [(a, b) for a in range(1, m) if gcd(a, m) == 1 for b in range(m)]
    return valid_pairs


def decrypt_pair(ciphertext, pairs):
    results = []
    for a, b in pairs:
        try:
            decrypted_text = decrypt_affine(ciphertext, a, b)
            results.append((a, b, decrypted_text))
        except ValueError:
            continue
    return results


def break_affine(ciphertext):
    m = 26
    valid_pairs = get_valid_a_b_pairs(m)  # Get valid (a, b) pairs
    return decrypt_pair(ciphertext, valid_pairs)  # Decrypt using pairs


def analyze_letter_frequency(dictionary):
    frequency = {char: 0 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    for line in dictionary:
        for char in line.strip().upper():
            if char in frequency:
                frequency[char] += 1

    # sort letters by frequently used
    sorted_letters = sorted(frequency, key=lambda x: frequency[x], reverse=True)

    result = ''.join(sorted_letters)
    return result


def break_mono(ciphertext, dictionary):
    english_freq_order = analyze_letter_frequency(dictionary)  # letter frequency method
    letter_freq = Counter(filter(str.isalpha, ciphertext.upper()))
    most_common = [pair[0] for pair in letter_freq.most_common()]

    key_guess = {most_common[i]: english_freq_order[i] for i in range(len(most_common))}

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_char = key_guess.get(char.upper(), char).lower() if char.islower() else key_guess.get(
                char.upper(), char)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    parser = argparse.ArgumentParser(description="Cipher Breaking")
    parser.add_argument("cipher", choices=["caesar", "affine", "mono", "alphatest"])
    parser.add_argument("file", default=None)
    parser.add_argument("dictionary", default=None)

    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            ciphertext = f.read()
    except FileNotFoundError:
        return

    try:
        with open(args.dictionary, "r") as f:
            dictionary = f.read()
    except FileNotFoundError:
        return

    # code breaking process
    if args.cipher == "caesar":
        possible_decryptions = break_caesar(ciphertext)
        print("Possible solutions:")
        for shift, decrypted_text in possible_decryptions:
            print(f"Shift {shift}: {decrypted_text}")
    elif args.cipher == "affine":
        possible_decryptions = break_affine(ciphertext)
        print("Possible solutions:")
        for a, b, decrypted_text in possible_decryptions:
            print(f"a={a}, b={b}: {decrypted_text}")
    elif args.cipher == "mono":
        possible_decryptions = break_mono(ciphertext, dictionary)
        print("Possible solutions:")
        print(possible_decryptions)
    elif args.cipher == "alphatest":
        sortedletters = analyze_letter_frequency(dictionary)
        print(sortedletters)
    else:
        print("Invalid method")
        return


if __name__ == '__main__':
    main()
