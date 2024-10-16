from helsinki_algorithms_project.rsa import generate_rsa_keypairs
from helsinki_algorithms_project.encoding import encode_message, decode_message, double_encode_message, double_decode_message


BITS = 1024
CONFIDENTIALITY = 1
AUTHENTICITY = 2
BOTH = 3
ENCODING_METHODS = {
    CONFIDENTIALITY: "CONFIDENTIALITY (Encryption with the reciever's public key, decryption with their private key.)",
    AUTHENTICITY: "AUTHENTICITY (Encryption with the sender's private key, decryption with the sender's public key.)",
    BOTH: "BOTH (Encryption first with the sender's private key, then the reciever's public key."\
        "Decryption using first the reciever's private key, then the sender's public key. )"
}


def get_input_encoding_method() -> int:
    method = ""
    while True:
        print("Pick encoding method: ")
        for key, value in ENCODING_METHODS.items():
            print(f"{key}.) {value}")
        method = input("")
        if method.isnumeric() and int(method) in ENCODING_METHODS.keys():
            return int(method)
        print("Invalid choice.\n")
    

def print_keys(pub_key: tuple[int, int], priv_key: tuple[int, int], name: str):
    print("\n")
    print(f"({name}) - Public key - public exponent (e):", pub_key[0])
    print(f"({name}) - Private key - private exponent (d):", priv_key[0])
    print(f"({name}) - Both keys - modulus (n): ", pub_key[1])
    print("\n")
   

if __name__ == "__main__":
    print("Generating RSA keys...")
    sender_public_key, sender_private_key = generate_rsa_keypairs(BITS)
    reciever_public_key, reciever_private_key = generate_rsa_keypairs(BITS)
    print_keys(sender_public_key, sender_private_key, "SENDER")
    print_keys(reciever_public_key, reciever_private_key, "RECIEVER")

    message: str = input("\n\nEnter the message you want to encode:\n")
    method: int = get_input_encoding_method()

    cyphertext: int = 0
    if method == CONFIDENTIALITY:
        cyphertext = encode_message(message, reciever_public_key[0], reciever_public_key[1], BITS)
    elif method == AUTHENTICITY:
        cyphertext = encode_message(message, sender_private_key[0], sender_private_key[1], BITS)
    elif method == BOTH:
        cyphertext = double_encode_message(
            message, 
            reciever_public_key[0], 
            reciever_public_key[1], 
            sender_private_key[0], 
            sender_private_key[1], 
            BITS
        )
    
    print("Encoded message: \n", cyphertext)
    input("Press 'ENTER' to continue with decoding the message...\n")

    decoded_message = ""
    if method == CONFIDENTIALITY:
        decoded_message = decode_message(cyphertext, reciever_private_key[0], reciever_private_key[1])
    elif method == AUTHENTICITY:
        decoded_message = decode_message(cyphertext, sender_public_key[0], sender_public_key[1])
    elif method == BOTH:
        decoded_message = double_decode_message(
            cyphertext, 
            sender_public_key[0], 
            sender_public_key[1], 
            reciever_private_key[0], 
            reciever_private_key[1]
        )

    print("Decoded message: \n", decoded_message)
