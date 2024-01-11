
from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify


HOST = "socket.cryptohack.org"
PORT = 13377

response_template = {'decoded' : ''}

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(0, 101):
    server_data = json_recv()
    print(server_data)
    encoding = server_data['type']
    encoded_data = server_data['encoded']
    if encoding == "base64":
        decoded = base64.b64decode(encoded_data).decode() 
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded_data).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded_data, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(encoded_data.replace("0x", "")).decode('utf8').replace("'", '"')
        print(decoded)
    elif encoding == "utf-8":
        decoded = "".join([chr(b) for b in encoded_data])

    response_template['decoded'] = decoded

    print(response_template)

    json_send(response_template)




# print(r.readline())
# print(r.readline())
# print(r.readline())

# request = {
#     "buy": "flag"
# }
# json_send(request)

# response = json_recv()

# print(response)
