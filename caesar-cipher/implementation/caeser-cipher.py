import sys
import getopt

# The space is only included for the cipher
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caeser_encrypt(plain_text, key):
    cipher_text = ''
    plain_text = plain_text.upper()
    alphabet_size = len(ALPHABET)

    for c in plain_text:
        index = ALPHABET.find(c)
        if index == -1:
            return -1

        cipher_index = (index + key) % alphabet_size
        cipher_text = "{0}{1}".format(cipher_text, ALPHABET[cipher_index])

    return cipher_text

def caeser_decrypt(cipher_text, key):
    plain_text = ''
    plain_text = plain_text.upper()
    alphabet_size = len(ALPHABET)

    for c in cipher_text:
        cipher_index = ALPHABET.find(c)
        if cipher_index == -1:
            return -1

        index = (cipher_index - key) % alphabet_size
        plain_text = "{0}{1}".format(plain_text, ALPHABET[index])

    return plain_text

def usage():
    print("Usage: python caeser-cipher [-k number_shift] [OPTION] [TEXT]")
    print("Script that performs encryption and decryption using the caeser cipher.")
    print("The text must contain only letters and spaces.\n")
    print("Options available:")
    print("-d                   decrypt the ciphertext")
    print("-e                   encrypt the plaintext")
    print("  --help    display this help and exit\n")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        exit()

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "k:de", ["help"])
    except:
        print("dsadas")
        usage()
        exit()

    encrypt = False
    decrypt = False
    key = -1
    for opt, arg in opts:
        if opt == "-d":
            decrypt = True
        elif opt == "-e":
            encrypt = True
        elif opt == "-k":
            key = arg
        else:
            usage()
            exit()

    try:
        key = int(key)
    except:
        usage()
        exit()

    text = " ".join(args)
    cipher_text = ""
    if encrypt:
        cipher_text = caeser_encrypt(text, key)
        if cipher_text == -1:
            print("The text must contain only letters and spaces.\n")
            exit()
        print("-------- Encryption --------")
        print("Plaintext: {}".format(text))
        print("Ciphertext: {}\n".format(cipher_text))
        text = cipher_text

    if decrypt:
        plain_text = caeser_decrypt(text, key)
        if cipher_text == -1:
            print("The text must contain only letters and spaces.\n")
            exit()
        print("-------- Decryption --------")
        print("Ciphertext: {}".format(text))
        print("Plaintext: {}\n".format(plain_text))
