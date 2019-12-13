# plain text  ABCDEFGHIJKLMNOPQRSTUVWXYZ
# cipher text DEFGHIJKLMNOPQRSTUVWXYZABC

# so HELLO becomes KHOOR
"""
>>> str = "ABDCE"
>>> str.index('A')
0
>>> str.find('A')
0
"""

def ceasar():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_in = input("Enter string to encode: ")
    #n = len(str_in)
    str_out = ''
    shift = int(input('Shift value: '))

    for char in str_in.upper():
        loc = alpha.index(char)
        print(loc, char, end="")
        new_loc = (loc+shift) % 26
        str_out += alpha[new_loc]
        print(new_loc, str_out)
    print(str_out.title())

#ceasar()

import base64

def my_base_64():
    # A-Z  => 0-25
    # a-z  => 26-51
    """
    bin         oct dec hex 
    0100 0001	101	65	41	A
    0100 0010	102	66	42	B
    0100 0011	103	67	43	C
    """
    # Standard Base64 Encoding
    data = "abc123!?$*&()'-=@~"
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print(data, "\n", encodedStr)


    # Standard Base64 Decoding
    encodedStr = "aGVsbG8gd29ybGQxMjMhPyQ="
    decodedBytes = base64.b64decode(encodedStr)
    decodedStr = str(decodedBytes, "utf-8")
    print(encodedStr, "\n", decodedStr)

#my_base_64()

def for_loop():
    text = input("Enter text: ")
    key = input("Enter key: ")
    i = 0

    for char in text:
        k = key[i%len(key)]
        x = ord(k) ^ ord(char)
        i+=1

        print(f'In char: {char}, Key: {k}, XOR: {x}, Exit char: {chr(x)}')

for_loop()