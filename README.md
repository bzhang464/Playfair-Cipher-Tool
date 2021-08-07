# Playfair Cipher Tool

This program can encrypt or decrypt user-inputted messages using the Playfair Cipher. It can do so with a randomly generated cipher or a user-inputted custom cipher.

## Background

The Playfair Cipher is an encryption technique introduced by Charles Wheatstone in 1854. It works by first constructing a secret grid of letters. Messages are then split into letter pairs, which are then converted into new letter pairs with the help of the cipher grid. 

For more information on the Playfair Cipher, see this link: https://en.wikipedia.org/wiki/Playfair_cipher



## Usage

This program is written in Python 3, so make sure to have it installed.

To use, simply run PlayfairCipherTool.py on your interpreter.

```bash
Welcome to the Playfair Cipher Tool!
Would you like to use a custom cipher? y/n y
Enter row 0 of the cipher. QWERT
Enter row 1 of the cipher. YUIOP
Enter row 2 of the cipher. ASDFG
Enter row 3 of the cipher. HKLZX
Enter row 4 of the cipher. CVBNM
Would you like to encrypt or decrypt a message? e/d e
Please enter your plaintext message. Hello World!
Your encrypted message is LQZHURFOBL
Thank you for using the Playfair Cipher Tool!
```
