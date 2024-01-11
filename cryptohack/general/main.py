from base64 import b64encode
from Crypto.Util.number import *
from pwn import xor


def ascii_arr_to_text(arr: list) -> str:
	valid = ''
	for element in arr:
		valid += chr(element)
	return valid

def decode_hex(data: str) -> str:
	# Create a bytes object from a string of hexadecimal numbers
	hex = bytes.fromhex(data)
	# Decode the bytes using the codec registered for encoding and return.
	return hex.decode()

def decode_b64(data: str) -> str:
	hex = bytes.fromhex(data)
	return b64encode(hex).decode()

def decode_bytes_and_big_integers(data: int) -> str:
	return long_to_bytes(data).decode()


def encoding_challenges():
	pass

def xor_starter(data: str) -> str:
	new_text = ''
	for char in data:
		new_text += chr(ord(char) ^ 13)
	return new_text

def xor_properties() -> str:
	key1_raw = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
	key2_raw = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
	key3_raw = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
	flag_raw = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

	key2_solved = xor(bytes.fromhex(key2_raw), key1_raw)
	key3_solved = xor(bytes.fromhex(key3_raw), key2_solved)
	partial_flag = xor(bytes.fromhex(key2_raw), key3_solved)

	flag = xor(bytes.fromhex(flag_raw), partial_flag)
	return flag.decode()

def favourite_byte(data: str) -> str:
	bytearr = bytearray.fromhex(data)

	for byte_value in range(256):
		results = [chr(b ^ byte_value) for b in bytearr]
		flag = "".join(results)
		if flag.startswith("crypto"):
			return f"Byte {byte_value}: {flag}"

	pass

	
	


if __name__ == "__main__":
	int_arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
	print(ascii_arr_to_text(int_arr))
	hex_data = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
	print(decode_hex(hex_data))
	hex_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
	print(decode_b64(hex_data))
	message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
	print(decode_bytes_and_big_integers(message))
	message = "label"
	print(xor_starter(message))
	print(xor_properties())
	print(favourite_byte("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"))
	




