# General 




## Encoding 

ASCII

ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Hex

If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.


Base64
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Bytes and Big Integers
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?
The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

```
message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487
```

Encoding Challenges



## XOR 

XOR Starter

XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.



XOR Properties
There are four main properties we should consider when we solve challenges using the XOR operator

```
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0
```

Commutative means that the order of the XOR operations is not important. 
Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing"
Something XOR'd with itself returns zero.

Favourite byte


## Mathematics 



## Data Formats 

Common Data Formats:

PEM
Popular format for sending keys, certificates, and other cryptographic material.
```
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKC... (a whole bunch of base64)
-----END RSA PUBLIC KEY-----
```

It wraps base64-encoded data by a one-line header and footer to indicate how to parse the data within. Perhaps unexpectedly, it's important for there to be the correct number of hyphens in the header and footer, otherwise cryptographic tools won't be able to recognise the file.


