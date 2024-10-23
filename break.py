import argparse
import math
from collections import Counter
from itertools import permutations
import re

from ciphers import decrypt_caesar, decrypt_affine

try:
    with open("dictionary.txt", "r") as f:
        dictionary = f.read()
except FileNotFoundError:
    print("Dictionary not found")


def break_caesar(ciphertext):
    potential_decryptions = []
    for shift in range(26):  # try from 0 to 25
        decrypted_text = decrypt_caesar(ciphertext, shift)
        potential_decryptions.append((shift, decrypted_text))
        words_set = set(decrypted_text.split())
        if all((word in dictionary) or (word.lower() in dictionary) for word in words_set if word.isalpha()):
            # Write the successful decryption to break_caesar.txt
            with open("break_caesar.txt", "w") as fw:
                fw.write(f"Shift = {shift}, Decrypted Text: \n{decrypted_text}\n")
            break
    return potential_decryptions


# BREAK AFFINE

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def get_valid_a_b_pairs(m):
    valid_pairs = [(a, b) for a in range(1, m) if math.gcd(a, m) == 1 for b in range(m)]
    return valid_pairs


def decrypt_pair(ciphertext, pairs):
    results = []
    for a, b in pairs:
        try:
            decrypted_text = decrypt_affine(ciphertext, a, b)
            results.append((a, b, decrypted_text))
            words_set = set(decrypted_text.split())
            if all((word in dictionary) or (word.lower() in dictionary) for word in words_set if word.isalpha()):
                break
        except ValueError:
            continue
    return results


def break_affine(ciphertext):
    m = 26
    valid_pairs = get_valid_a_b_pairs(m)  # Get valid (a, b) pairs

    # Attempt to decrypt using valid pairs
    results = decrypt_pair(ciphertext, valid_pairs)

    # Write the results to break_affine.txt
    with open("break_affine.txt", "w") as fw:
        a, b, decrypted_text = results[-1]
        fw.write(f"a = {a}, b = {b}, Decrypted Text: \n{decrypted_text}\n")

    # Return results
    return results


# BREAK MONO

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().upper() for word in file)


def analyze_letter_frequency(dictionary):
    try:
        with open(dictionary, "r") as f:
            dictionary = f.read()
    except FileNotFoundError:
        return

    frequency = {char: 0 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    for line in dictionary:
        for char in line.strip().upper():
            if char in frequency:
                frequency[char] += 1

    # sort letters by frequently used
    sorted_letters = sorted(frequency, key=lambda x: frequency[x], reverse=True)

    result = ''.join(sorted_letters)
    return result


def custom_match(word, regex):
    if len(regex) != len(word):
        return False
    for w_char, r_char in zip(word, regex):
        if r_char != '.' and r_char != w_char.upper():
            return False
    return True

def break_mono(ciphertext):
    common_letters = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    letter_freq = Counter(filter(str.isalpha, ciphertext.upper()))
    most_common = [pair[0] for pair in letter_freq.most_common()]
    # dictionary = load_dictionary(dictionary_file_path)
    key_guess = {
        # most_common[0]: "E",
        # most_common[-1]: "Z",
        # most_common[-2]: "Q",
        # most_common[-3]: "J",
    }
    three_letter_words = {

    }
    cwords = ciphertext.split()
    for w in cwords:
        w = w.upper()
        if len(w) == 3:
            if w in three_letter_words:
                three_letter_words[w] += 1
            else:
                three_letter_words[w] = 1
    sorted_three = {}
    sorted_three = dict(sorted(three_letter_words.items(), key=lambda x: x[1], reverse=True))
    sorted_three = list(sorted_three.keys())
    if sorted_three[0][2] == "E":
        key_guess[sorted_three[0][0]] = "T"
        key_guess[sorted_three[0][1]] = "H"
        key_guess[sorted_three[0][2]] = "E"
        key_guess[sorted_three[1][0]] = "A"
        key_guess[sorted_three[1][1]] = "N"
        key_guess[sorted_three[1][2]] = "D"
    else:
        key_guess[sorted_three[0][0]] = "A"
        key_guess[sorted_three[0][1]] = "N"
        key_guess[sorted_three[0][2]] = "D"
        key_guess[sorted_three[1][0]] = "T"
        key_guess[sorted_three[1][1]] = "H"
        key_guess[sorted_three[1][2]] = "E"
    split_dictionary = dictionary.split()
    for w in sorted(cwords, key=len, reverse=True):
        if any(char.upper() in key_guess for char in w):
            regex_string = ""
            unknown_chars = []
            for index, letter in enumerate(w):
                if letter.isalpha():
                    if letter.upper() in key_guess:
                        regex_string += key_guess[letter.upper()]
                    else:
                        regex_string += "."
                        unknown_chars.append(index)
                else:
                    break
            #real_regex = regex_string
            #regex_string = f"^{regex_string}$"
            #pattern = re.compile(regex_string, re.IGNORECASE)
            matching_words = [word for word in split_dictionary if custom_match(word, regex_string)]

            if len(matching_words) == 1:
                match_word = matching_words[0]
                for index in unknown_chars:
                    letter = match_word[index]
                    key_guess[w[index].upper()] = letter.upper()
            else:
                known_letters = set(key_guess.values())
                eligible_words = [
                    word for word in matching_words if
                    not any(word[index].upper() in known_letters for index in unknown_chars)
                ]
                if len(eligible_words) == 1:
                    match_word = eligible_words[0]
                    for index in unknown_chars:
                        letter = match_word[index]
                        key_guess[w[index].upper()] = letter.upper()

            if len(key_guess) == 26:
                break

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            char_upper = char.upper()
            if char_upper in key_guess:
                decrypted_text += key_guess[char_upper].lower() if char.islower() else key_guess[char_upper]
            else:
                decrypted_text += char
        else:
            decrypted_text += char

    # Write the decrypted text to break_mono.txt
    with open("break_mono.txt", "w") as output_file:
        output_file.write(decrypted_text)

    return decrypted_text


def main():
    parser = argparse.ArgumentParser(description="Cipher Breaking")
    parser.add_argument("cipher", choices=["caesar", "affine", "mono", "alphatest"])
    parser.add_argument("file", default=None)

    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            ciphertext = f.read()
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
        possible_decryptions = break_mono(ciphertext)
        print("Possible solutions:")
        print(possible_decryptions)
    elif args.cipher == "alphatest":
        sortedletters = analyze_letter_frequency(ciphertext)
        print(sortedletters)
    else:
        print("Invalid method")
        return


if __name__ == '__main__':
    main()
