from base64 import b64encode
from Crypto.Util.number import *





if __name__ == "__main__":
	# ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
	# Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
	int_arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
 	# In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
	valid = ''
	for element in int_arr:
		valid += chr(element)
		
	print(valid)

	decoder = bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")

	print(decoder.decode())


	decoder = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
	print(b64encode(decoder).decode())

	print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269).decode())

	lst = []
	thirteen_binary = bin(13).replace("0b", "") 
	new_text = ''


	for char in 'label':

		new_text += chr(ord(char) ^ 13)


	print(new_text)
	







	# e can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.



	



# When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

# Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

# Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.

# 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

#  In Python, the bytes.fromhex() function can be used to convert hex to bytes. The .hex() instance method can be called on byte strings to get the hex representation.
	

# 	Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

# Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

# Take the below hex string, decode it into bytes and then encode it into Base64.

# 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

#  In Python, after importing the base64 module with import base64, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.
	

# 	Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

# The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

# To illustrate:

# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487

#  Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). You will first have to install PyCryptodome and import it with from Crypto.Util.number import *. For more details check the FAQ.


# Convert the following integer back into a message:

# 11515195063862318899931685488813747395775516287289682636499965282714637259206269