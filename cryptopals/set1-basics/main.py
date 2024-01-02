from base64 import b64encode

def hex_to_b64(hex: str) -> str:
    return b64encode(bytes.fromhex(hex)).decode()


if __name__ == "__main__":
    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    assert hex_to_b64(hex_input) == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    