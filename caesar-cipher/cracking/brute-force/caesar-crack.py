import sys

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caeser_brute_force(cipher_text):
    alphabet_size = len(ALPHABET)
    for key in range(len(ALPHABET)):
        plain_text = ''
        for c in cipher_text:
            cipher_index = ALPHABET.find(c)
            if cipher_index == -1:
                return -1

            index = (cipher_index - key) % alphabet_size
            # TO-DO: check if it is an english phrase
            plain_text = "{0}{1}".format(plain_text, ALPHABET[index])
        print("Using the key {0}, the plaintext is {1}".format(key, plain_text))

if __name__ == "__main__":
    cipher_text = sys.argv[1]
    caeser_brute_force(cipher_text)
