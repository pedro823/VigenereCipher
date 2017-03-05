#!/usr/bin/env python3
import random
import sys
from optparse import OptionParser

class Vigenere:
    def asciify(text):
        newtext = ''
        for char in text.lower().encode("ascii", "ignore"):
            if char <= 122 and char >= 97:
                newtext += chr(char)
        return newtext

    def encode(text, keyword):
        keyword = Vigenere.asciify(keyword)
        output, key, maxkey = '', 0, len(keyword)
        for letter in Vigenere.asciify(text):
            if key == maxkey:
                key = 0
            cipher_char = (ord(letter) + ord(keyword[key]) - 194) % 26 + 97
            output += chr(cipher_char)
            key += 1
        return output

    def decode(text, keyword):
        keyword = Vigenere.asciify(keyword)
        output, key, maxkey = '', 0, len(keyword)
        for letter in Vigenere.asciify(text):
            if key == maxkey:
                key = 0
            decipher_char = (ord(letter) - ord(keyword[key]) - 194) % 26 + 97
            output += chr(cipher_char)
            key += 1
        return output

    # creates a random_key with about the size said by est_size.
    def create_random_key(est_size):
        if(est_size < 11):
            est_size = 11
        r = random.SystemRandom()
        key = ''
        possible_range = (est_size - r.randint(2, 10), est_size + r.randint(2,10))
        for i in range(r.randint(possible_range[0], possible_range[1])):
            key += chr(r.randint(97, 122))
        return key

def __errorVigenere(arg):
    if arg == 0:
        msg = "No encode or decode archive provided. type " + sys.argv[0] + "--help for options."
    elif arg == 1:
        msg = "Both encoding and decoding set."
    elif arg == 2:
        msg = "No key provided to decode ciphered output. Use -k KEY or --key=KEY."
    else:
        msg = "Unknown error occurred."

    sys.exit(sys.argv[0] + ': error: ' + msg)


if(__name__ == "__main__"):
    parser = OptionParser()

    # Parser options
    parser.add_option("-e", "--encode",
        action = "store",
        dest = "encode_filename",
        type = "string",
        help = "Encodes Vigenere to FILE. If no key is specified, generates one at random.",
        metavar = "FILE")

    parser.add_option("-d", "--decode",
        action = "store",
        dest = "decode_filename",
        type = "string",
        help = "Decodes Vigenere cipher from FILE.",
        metavar = "FILE")

    parser.add_option("-k", "--key",
        action = "store",
        dest = "key",
        type = "string",
        help = "Specifies key to cipher/decipher Vigenere from. This flag is NEEDED to decipher.",
        metavar = "KEY")

    parser.add_option("-o", "--out",
        action = "store",
        dest = "outfile",
        type = "string",
        default = "vigenere_out.vig",
        help = "Sets ciphered output to FILE. Defaults to 'vigenere_out.vig'.",
        metavar = "FILE")

    parser.add_option("--keyout",
        action = "store",
        dest = "keyfile",
        type = "string",
        help = "Do not print the generated key. Instead, write to FILE.",
        metavar = "FILE")

    (flags, args) = parser.parse_args()

    # Initial Error Checking
    if flags.decode_filename == None and flags.decode_filename == None:
        __errorVigenere(0)
    if flags.encode_filename != None and flags.decode_filename != None:
        __errorVigenere(1)
    if flags.decode_filename != None and flags.key == None:
        __errorVigenere(2)

    # Encode process
    if flags.encode_filename:
        
