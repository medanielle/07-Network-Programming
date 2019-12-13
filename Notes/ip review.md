TCP vs UDP, darpa, OSI, asshole

8 bits = 1 byte
172 -> 10  1     0    1100
  1   0     1   0     1   1   0   0
128 | 64 | 32 | 16 || 8 | 4 | 2 | 1
128 + 32 + 8 + 4

Classes
A 0.0.0.0 - 127.255.255.255
B 128.0.0.0 - 191.255.255.255
C 192.0.0.0 - 223.255.255.255

Private
10.0.0.0-10.255.255.255
172.16.0.0
192.168.0.0

ipconfig
ifconfig
ipaddr

DHCP
DORA (Discover - Offer - Request - ACK)

NAT (Network address translation) - breaks ISP ip inot private space ips

65535 max
1024 common/reserved

base 10 

base 16 
45 hex => 69
 
256 16 1
5*1 + 4*16 = 64


BITWISE
~ = complement
& = AND
| = OR
^ = XOR
<< = Left Shift
>> = Right Shift

>>> ~12
-13 
1100

***  ~ x  ***
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

>>> ~12
-13 

def twos_complement(input_value: int, num_bits: int) -> int:
    """Calculates a two's complement integer from the given input value's bits."""
    mask = 2**(num_bits - 1)
    return -(input_value & mask) + (input_value & ~mask)

*** x & y ***
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

Truth tables
    AND
X   Y   XY
0   0   0
0   1   0
1   0   0
1   1   1

*** EX ***
>>> 12 & 13
12 

12 - 00001100
13 - 00001101 &
     ---------
     00001100  = 12


***  x | y  ***
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

    OR
X   Y   XY
0   0   0
0   1   1
1   0   1
1   1   1

*** EX ***
>>> 12 | 13
13 

12 - 00001100
13 - 00001101 |
     ---------
     00001101  = 13
***  x ^ y  ***
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

    XOR(^)
X   Y   XY
0   0   0
0   1   1
1   0   1
1   1   0

*** EX ***
>>> 12 ^ 13
1  

12 - 00001100
13 - 00001101 |
     ---------
     00000001  = 1

*** x << y ***
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

*** EX ***
>>> 10 << 2
40

1010 =(8+2)
101000 = (32+8) *** add 2 zeros ***

*** Review ***
XOR
Same = off = 0
diff = on  = 1

A = 01000001
B = 01000010
------------
XOR = 00000011 = 3

>>> ord('A') ^ ord('B')
3

Single Byte
-----------
"ABC" = 01000001|01000010|01000011
"B"   = 01000010|01000010|01000010 (aka = 'BBB')
-----------------------------------
XOR   = 00000011|00000000|00000000 (last two all zeros)

24
00011000
~24 = -25
11100111 => not a big number/ just negative somehow... magically


*** Endian ***
Most Sig Bit is first = Big Endian
least sig bit first = Little Endian

Network byte order is Big Endian
x86/x64 is Little endian

***  Networks and Ports ***

53 = DNS


tuple in python ("www.python.org", 80) 
                ()

IANA Internet Assigned Numbers Authority
 - in charge of ip addr/ and common ports