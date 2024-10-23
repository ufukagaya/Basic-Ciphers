import timeit
import argparse


def load_file_content(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None


def test_caesar(ciphertext):
    from breakers import break_caesar
    return timeit.timeit(lambda: break_caesar(ciphertext), number=1)


def test_affine(ciphertext):
    from breakers import break_affine
    return timeit.timeit(lambda: break_affine(ciphertext), number=1)


def test_mono(ciphertext, dictionary):
    from breakers import break_mono
    return timeit.timeit(lambda: break_mono(ciphertext, dictionary.splitlines()), number=1)


def main():
    parser = argparse.ArgumentParser(description="Cipher Breaking Time Efficiency Test")
    parser.add_argument("file", help="ciphertext file")
    parser.add_argument("dictionary", help="dictionary file")

    args = parser.parse_args()

    # load file content
    ciphertext = load_file_content(args.file)
    dictionary = load_file_content(args.dictionary)

    if ciphertext is None or dictionary is None:
        print("Files could not be loaded.")
        return

    # Caesar test
    caesar_time = test_caesar(ciphertext)
    print(f"Caesar cipher breaking average time: {caesar_time:.5f} seconds")

    # Affine test
    affine_time = test_affine(ciphertext)
    print(f"Affine cipher breaking average time: {affine_time:.5f} seconds")

    # Mono test
    mono_time = test_mono(ciphertext, dictionary)
    print(f"Monoalphabetic cipher breaking average time: {mono_time:.5f} seconds")


if __name__ == "__main__":
    main()
