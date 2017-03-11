# Vigenere

####A python script for easy ciphering small bits of text, to write messages more secretly.

---

+ **Fun experiment**  
Viginere ciphers and deciphers text using the same key. You can either have an agreed upon key beforehand

+ **Made to be breakable. Hack away!**  
This script can be used for practicing reverse engineering. Try making a script that finds the key using an original text and a ciphered text!

---

### How to use:

    python viginere.py [-e FILE | -d FILE | -k KEY | -o OUTPUT]

---

### How does it work? *(Spoilers)*

Do not read this section if you want to reverse engineer the hard way.

To understand the algorithm, first you'll need to understand [caesar shift ciphering]().

The Vigenere algorithm, instead of shifting every character the same amount of steps (for example Caesar +9 shifts a to j, b to k, c to l, and so on), shifts every letter a different amount, according to another letter in the key.

Explained using an example:

Imagining there is a file named notEncripted.txt containing:

    sample phrase
