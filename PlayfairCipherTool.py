import random

def encrypt(plaintext, CIPHER):
    letters = ''.join([i for i in plaintext if i.isalpha()])
    letters = letters.replace("j","i")
    if len(letters) % 2 != 0:
        letters = letters + "X"
    letters = letters.upper()
    pairs = [letters[i:i+2] for i in range(0, len(letters), 2)]
    result = ""
    for pair in pairs:
        result = result + new_cipher_pair(pair, CIPHER)
    return result


def new_cipher_pair(pair, CIPHER):
    first = pair[0]
    second = pair[1]
    if first == second:
        second = "X"
    firstcoord = None
    secondcoord = None
    for x in range(5):
        for y in range(5):
            if CIPHER[x][y] == first:
                firstcoord = [x, y]
            if CIPHER[x][y] == second:
                secondcoord = [x, y]
    if firstcoord[0] == secondcoord[0]:
        first = CIPHER[firstcoord[0]][(firstcoord[1]+1) % 5]
        second = CIPHER[secondcoord[0]][(secondcoord[1]+1) % 5]
    elif firstcoord[1] == secondcoord[1]:
        first = CIPHER[(firstcoord[0]+1) % 5][firstcoord[1]]
        second = CIPHER[(secondcoord[0]+1) % 5][secondcoord[1]]
    else:
        first = CIPHER[firstcoord[0]][secondcoord[1]]
        second = CIPHER[secondcoord[0]][firstcoord[1]]
    return first + second


def new_plain_pair(pair, CIPHER):
    first = pair[0]
    second = pair[1]
    firstcoord = None
    secondcoord = None
    for x in range(5):
        for y in range(5):
            if CIPHER[x][y] == first:
                firstcoord = [x, y]
            if CIPHER[x][y] == second:
                secondcoord = [x, y]
    if firstcoord[0] == secondcoord[0]:
        first = CIPHER[firstcoord[0]][(firstcoord[1] - 1) % 5]
        second = CIPHER[secondcoord[0]][(secondcoord[1] - 1) % 5]
    elif firstcoord[1] == secondcoord[1]:
        first = CIPHER[(firstcoord[0] - 1) % 5][firstcoord[1]]
        second = CIPHER[(secondcoord[0] - 1) % 5][secondcoord[1]]
    else:
        first = CIPHER[firstcoord[0]][secondcoord[1]]
        second = CIPHER[secondcoord[0]][firstcoord[1]]
    return first + second


def decrypt(ciphertext, CIPHER):
    ciphertext = ciphertext.upper()
    pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    result = ""
    for pair in pairs:
        result = result + new_plain_pair(pair, CIPHER)
    return result


def cipher_maker(custom):
    if custom == "y":
        result = []
        for x in range(5):
            row = []
            letters = input("Enter row {} of the cipher. ".format(x))
            letters = letters.strip()
            for letter in letters:
                row.append(letter.upper())
            result.append(row)
        return result
    else:
        letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        random.shuffle(letters)
        return [letters[:5], letters[5:10], letters[10:15], letters[15:20], letters[20:25]]


if __name__ == "__main__":
    print("Welcome to the Playfair Cipher Tool!")
    custom = input("Would you like to use a custom cipher? y/n ")
    cipher = cipher_maker(custom.strip().lower())
    direction = input("Would you like to encrypt or decrypt a message? e/d ")
    direction = direction.strip().lower()
    if direction == "e":
        plaintext = input("Please enter your plaintext message. ")
        print("Your encrypted message is " + encrypt(plaintext, cipher))
    if direction == "d":
        ciphertext = input("Please enter your ciphertext message.")
        print("Your decrypted message is " + decrypt(ciphertext, cipher))
    print("Thank you for using the Playfair Cipher Tool!")
