"""Crypto Challenges
Challenge 1 – the Caesar cipher
Your challenge is to decipher this string: MYXQBKDEVKDSYXC
"""

def ceasar():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #str_in = input("Enter string to encode: ")
    str_in = 'MYXQBKDEVKDSYXC'
    #n = len(str_in)
    str_out = ''
    #shift = int(input('Shift value: '))

    for x in range(1, 27):
        for char in str_in.upper():
            loc = alpha.index(char)
            #print(loc, char, end="")
            new_loc = (loc+x) % 26
            str_out += alpha[new_loc]
            #print(new_loc, str_out)
        print(x, str_out.title())
        str_out = ''

#ceasar()
    #Output=
    # 1 Nzyrclefwletzyd
    # 2 Oazsdmfgxmfuaze
    # 3 Pbatenghyngvbaf
    # 4 Qcbufohizohwcbg
    # 5 Rdcvgpijapixdch
    # 6 Sedwhqjkbqjyedi
    # 7 Tfexirklcrkzfej
    # 8 Ugfyjslmdslagfk
    # 9 Vhgzktmnetmbhgl
    # 10 Wihalunofuncihm
    # 11 Xjibmvopgvodjin
    # 12 Ykjcnwpqhwpekjo
    # 13 Zlkdoxqrixqflkp
    # 14 Amlepyrsjyrgmlq
    # 15 Bnmfqzstkzshnmr
    # 16 Congratulations
    # 17 Dpohsbuvmbujpot
    # 18 Eqpitcvwncvkqpu
    # 19 Frqjudwxodwlrqv
    # 20 Gsrkvexypexmsrw
    # 21 Htslwfyzqfyntsx
    # 22 Iutmxgzargzouty
    # 23 Jvunyhabshapvuz
    # 24 Kwvozibctibqwva
    # 25 Lxwpajcdujcrxwb
    # 26 Myxqbkdevkdsyxc


    # 16 Congratulations
"""Challenge 2 – base64
Decode this: VGhpcyBpcyB0b28gZWFzeQ==

Challenge 2.1 - base64
Decode this: VWtkc2EwbEliSFprVTBjeFl6lZaMWxUUW5OaU1qbDNVSGM5UFFvPQo=

Hint: several rounds of Base64 were used.

"""
import base64
def decode_my_64():

    code = "VGhpcyBpcyB0b28gZWFzeQ=="
    try:
        for x in range(1, 21):
            code = base64.b64decode(code)
            print(x, code)
    except:
        print("The last one was it!")

#decode_my_64()
#code = "VGhpcyBpcyB0b28gZWFzeQ=="
#print(base64.b64decode(code))

code = "VWtkc2EwbEliSFprVTBjeFl6lZaMWxUUW5OaU1qbDNVSGM5UFFvPQo="
# print(len(code)/4)
def decode_my_64_2():
    x = 0
    code = "VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ=="
    try:
        while x < 50:
            code = base64.b64decode(code)
            x+=1
            print(x, code)
    except:
        print(f"The last one was it")  #{code:!r}
# decode_my_64_2()

"""Challenge 3 – XOR
The first challenge is here:
Decipher this: kquht}

Key is a single digit

Here's a longer example that is in a hexadecimal format:
Decipher this: 70155d5c45415d5011585446424c

Key is two digits of ASCII
"""

def alpha_XOR():
    text = 'kquht}'
    i = 0
    
    for key in range(10):
        encoded = ''
        for char in text:
            key = str(key)
            k = key[i%len(key)]
            x = ord(str(k)) ^ ord(char)
            i+=1
            encoded += chr(x)
            # print(f'In char: {char}, Key: {k}, XOR: {x}, Exit char: {chr(x)}')
        print(key, encoded)

# alpha_XOR()

# Output: 
# 0 [AEXDM
# 1 Z@DYEL
# 2 YCGZFO
# 3 XBF[GN
# 4 _EA\@I
# 5 ^D@]AH
# 6 ]GC^BK
# 7 \FB_CJ
# 8 SIMPLE
# 9 RHLQMD

# 8 SIMPLE


def hex_XOR():
    text = '70155d5c45415d5011585446424c'
    i = 0
    
    for key in range(16):
        encoded = ''
        for char in text:
            key = str(key)
            k = key[i%len(key)]
            k = int(k)
            print(k)
            char = int(char)
            print(str(char))
            #x = k ^ char
            i+=1
            #encoded += chr(x)
            # print(f'In char: {char}, Key: {k}, XOR: {x}, Exit char: {chr(x)}')
            print('-'*20)
        print(key, encoded)

#hex_XOR()
import codecs
import binascii

def teach():
    #texth = raw_input("Enter hex plantext: ")
    texth = r'70155d5c45415d5011585446424c'
    #string = binascii.hexlify(texth)
    text = str(binascii.unhexlify(texth))
    n = len(text)

    for k1 in "0123456789":
        for k2 in "0123456789":
            key = k1 + k2
            clear = ""
            for i in range(n):
                t = text[i]
                k = key[i%2]
                x = ord(k) ^ ord(t)
                clear += chr(x)
            print(key, clear)





 


teach()