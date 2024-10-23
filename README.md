# Basic-Ciphers
## BBM465 - Assignement 1 - Basic Ciphers
This project covers basic cipher concepts. There are some cipher methods used in this program: 
*Caesar Method
*Affine Method
*Mono-alphabetic Substitution method
 
## Features:
*Encryption: Encode messages using the Caesar, Affine, or Mono-alphabetic substitution cipher.

*Decryption: Decode messages encrypted using the above methods.

*Cryptanalysis: Basic techniques for breaking these ciphers such as brute force and frequency analysis.

*Efficiency Tests: Mechanism to evaluate the performance of the break operations.

## Installation:
```git clone https://github.com/ufukagaya/Basic-Ciphers.git```

```cd Basic-Ciphers```


## Usage:

### See the plaintext:

To show the first version of plaintext: 

```python ciphers.py show plain.txt s```

### Use of Caesar Method:

To encrypt the plaintext using the Caesar method by shifting amount 13. This command creates a txt file named coded_caesar.txt containing the encrypted text: 

```python ciphers.py caesar plain.txt e -s 13```

To decrypt the ciphertext using the same Caesar method by shifting amount 13: 

```python ciphers.py caesar coded_caesar.txt d -s 13```

To break the ciphertext using the Caesar method: 

```python breakers.py caesar coded_caesar.txt```

### Use of Affine Method:

To encrypt the plaintext using the Affine method by the function of 3x+5. This command creates a txt file named coded_affine.txt containing the encrypted text: 

```python ciphers.py affine plain.txt e -a 3 -b 5```

To decrypt the plaintext using the Affine method by the function of 3x+5: 

```python ciphers.py affine coded_affine.txt d -a 3 -b 5```

To break the ciphertext using the Affine method: 

```python breakers.py affine coded_affine.txt```

### Use of Mono-alphabetic Substitution Method:

To encrypt the plaintext using the Mono-alphabetic Substitution method by given key alphabet. This command creates a txt file named coded_mono.txt containing the encrypted text: 

```python ciphers.py mono plain.txt e -k QWERTYUIOPASDFGHJKLZXCVBNM```

To decrypt the plaintext using the Mono-alphabetic Substitution method by given key alphabet: 

```python ciphers.py mono coded_mono.txt d -k QWERTYUIOPASDFGHJKLZXCVBNM```

To analyze and show the frequency of letters of the given source file: 

```python breakers.py alphatest plain.txt ```

To break the ciphertext using the Mono-alphabetic Substitution method by calculating frequency analysis: 

```python breakers.py mono coded_mono.txt```

### Efficiency Test:

To calculate and show the time of the breaker functions using plain.txt: 

```python efficiency_test.py plain.txt```
