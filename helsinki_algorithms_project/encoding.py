ENCODING = "utf-8"

def message_to_integer(msg: str, bits: int) -> int:
    """Converts the message string to integer value, if it fits into the set bits."""
    if bits // 8 <= len(msg):
        raise ValueError(f"Message too long. With the current settings, a strlen of a maximum of {bits // 8} characters is supported.")
    
    message_bytes: bytes = msg.encode(ENCODING)
    return int.from_bytes(message_bytes, byteorder='big')


def integer_to_message(msg_int):
    """Conerts integer value to string."""
    bytes_length: int = (msg_int.bit_length() + 7) // 8
    original_bytes: bytes = msg_int.to_bytes(bytes_length, byteorder='big')
    
    return original_bytes.decode(ENCODING)


def encode_message(msg: str, e: int, mod: int, bits: int) -> int:
    """Encodes the message using the public/private exponent and the modulus."""
    message_int = message_to_integer(msg, bits)
    return pow(message_int, e, mod)


def decode_message(cyphertext: int, e: int, mod: int) -> str:
    """Decodes the message using the public/private exponent and the modulus."""
    original_message_int: int = pow(cyphertext, e, mod)
    return integer_to_message(original_message_int)


def double_encode_message(
        msg: str, 
        public_key_exponent: int, 
        public_key_mod: int,
        private_key_exponent: int, 
        private_key_mod: int, 
        bits: int
    ):
    """
    Uses the sender's private key and the reciver's public key to encode the message.
    This way the message is both confidential and signed by the sender.
    """
    signed_int = encode_message(msg, private_key_exponent, private_key_mod, bits)
    return pow(signed_int, public_key_exponent, public_key_mod)
    

def double_decode_message(
        cyphertext: int, 
        public_key_exponent: int, 
        public_key_mod: int, 
        private_key_exponent: int,
        private_key_mod: int
    ):
    """
    Uses the reciever's private key and the sender's public key to decode the message.
    """
    verified_int = pow(cyphertext, private_key_exponent, private_key_mod)
    return decode_message(verified_int, public_key_exponent, public_key_mod)
