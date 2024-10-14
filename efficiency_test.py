import timeit
import argparse
from breakers import break_caesar, break_affine, break_mono


def load_file_content(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None


def test_caesar(ciphertext):
    break_caesar(ciphertext)
    setup_code = f"from breakers import break_caesar; ciphertext = '''{ciphertext}'''"
    test_code = "break_caesar(ciphertext)"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=10)


def test_affine(ciphertext):
    break_affine(ciphertext)
    setup_code = f"from breakers import break_affine; ciphertext = '''{ciphertext}'''"
    test_code = "break_affine(ciphertext)"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=10)


def test_mono(ciphertext, dictionary):
    break_mono(ciphertext, dictionary.splitlines())
    setup_code = f"from breakers import break_mono; ciphertext = '''{ciphertext}'''; dictionary = '''{dictionary}'''"
    test_code = "break_mono(ciphertext, dictionary.splitlines())"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=10)


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
