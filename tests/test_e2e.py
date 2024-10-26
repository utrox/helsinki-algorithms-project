from helsinki_algorithms_project.rsa import generate_rsa_keypairs
from helsinki_algorithms_project.encoding import encode_message, decode_message, double_encode_message, double_decode_message

BITS = 1024

def test__end_to_end_authenticity_confidentiality():
    """
    Test encoding and decoding a message with the reciever's 
    public key for encryption reciever's private key for decryption.
    """
    TEST_MESSAGE = "Hello world!"
    public_key, private_key = generate_rsa_keypairs(1024)
    encoded = encode_message(TEST_MESSAGE, public_key[0], public_key[1], 1024)
    decoded = decode_message(encoded, private_key[0], private_key[1])
    assert TEST_MESSAGE == decoded, "The two messages do not match."


def test__end_to_end_authenticity():
    """
    Test the encoding and decoding of a message with the sender's
    private key for encryption and the sender's public key for decryption.
    """
    TEST_MESSAGE = "Hello world!"
    public_key, private_key = generate_rsa_keypairs(1024)
    encoded = encode_message(TEST_MESSAGE, private_key[0], private_key[1], 1024)
    decoded = decode_message(encoded, public_key[0], public_key[1])
    assert TEST_MESSAGE == decoded, "The two messages do not match."


def test__end_to_end_both():
    """
    Test the encoding and decoding of a message with the sender's
    private key and the reciever's public key for encryption and
    the reciever's private key and the sender's public key for decryption.
    """
    TEST_MESSAGE = "Hello world!"
    sender_public_key, sender_private_key = generate_rsa_keypairs(1024)
    reciever_public_key, reciever_private_key = generate_rsa_keypairs(1024)
    encoded = double_encode_message(
        TEST_MESSAGE, 
        reciever_public_key[0], 
        reciever_public_key[1], 
        sender_private_key[0], 
        sender_private_key[1], 
        1024
    )
    decoded = double_decode_message(
        encoded,
        sender_public_key[0], 
        sender_public_key[1], 
        reciever_private_key[0], 
        reciever_private_key[1]
    )
    assert TEST_MESSAGE == decoded, "The two messages do not match."
