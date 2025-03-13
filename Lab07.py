import sys
from sys import exit

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'YIPPEE'
    # message = 'They mostly come at night. Mostly.'
    encrypted_list = []

    menu = [
        ['1) Encrypt', enc_menu, [key, alphabet, encrypted_list]],
        ['2) Decrypt', dec_menu, [key, alphabet, encrypted_list]],
        ['3) Dump Decrypt', dump_dec, [encrypted_list]],
        ['4) Quit', exit, [0]]
    ]

    while True:
        print("-"*80)
        for menu_item in menu:
            print(menu_item[0])
        try:
            choice = int(input("Make your choice: "))
            if not (0 < choice <= len(menu)):
                print("Improper choice!")
            else:
                menu[choice-1][1](*menu[choice-1][2])
        except TypeError:
            print("Improper choice! Ints only")
        except ValueError:
            print("Improper choice! Ints only")

def enc_menu(key, alphabet, encrypted_list):
    plaintext = input("Enter text to encrypt: ")
    encrypted_list.append(encrypt_vigenere(key, plaintext, alphabet))

def dec_menu(key, alphabet, encrypted_list):
    for ciphertext in encrypted_list:
        print(decrypt_vigenere(key, ciphertext, alphabet))

def dump_dec(encrypted_list):
    for ciphertext in encrypted_list:
        print(ciphertext)

def vigenere_header(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = [vigenere_header(alphabet)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f"{'|---' * len(row)}|")

def letter_to_index(letter, alphabet:str):
    # return alphabet.upper().find(letter.upper())
    return alphabet.find(letter)

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return index_to_letter(
        (letter_to_index(plaintext_letter,alphabet) +
         letter_to_index(key_letter,alphabet)) % len(alphabet), alphabet)

def non_vigenere_index(key_letter, ciphertext, alphabet):
    return index_to_letter(
        (letter_to_index(ciphertext,alphabet) -
         letter_to_index(key_letter,alphabet) + len(alphabet)) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text.append(' ')
        elif c in alphabet:
            cipher_text.append(vigenere_index(key[counter % len(key)], c, alphabet))
            counter += 1
    return ''.join(cipher_text)

def decrypt_vigenere(key, ciphertext, alphabet):
    plaintext = []
    counter = 0
    for c in ciphertext:
        if c == ' ' :
            plaintext.append(' ')
        elif c in alphabet:
            plaintext.append(non_vigenere_index(key[counter % len(key)], c, alphabet))
            counter += 1
    return ''.join(plaintext)

if __name__ == "__main__":
    main()