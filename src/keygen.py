import enum
import base64
from typing import Tuple

from pyasn1.codec.der import encoder, decoder
from pyasn1.type import univ, namedtype


MODULUS = "modulus"
PUBLIC_EXPONENT = "publicExponent"
PRIVATE_EXPONENT = "privateExponent"
ENCODING = "utf-8"


class RSAPublicKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(MODULUS, univ.Integer()),
        namedtype.NamedType(PUBLIC_EXPONENT, univ.Integer()),
    )


class RSAPrivateKey(univ.Sequence):
    # Can be extended with values like primes, exponents, coefficient 
    # to make computing faster.
    componentType = namedtype.NamedTypes(
        namedtype.NamedType(MODULUS, univ.Integer()),
        namedtype.NamedType(PRIVATE_EXPONENT, univ.Integer()),
    )


class RSAKeyType(enum.Enum):
    PUBLIC = RSAPublicKey
    PRIVATE = RSAPrivateKey


def get_base64_key(exponent: int, modulus: int, keyType: RSAKeyType) -> str:
    """
    Encodes the RSA key (containing the exponent and the modulus)
    using ASN.1 structure in DER format to a base64 string.
    
    Format: \n
    ```
    RSAKey ::= SEQUENCE {
        modulus         INTEGER,  -- n
        exponent        INTEGER   -- e
    }
    ```
    """
    if keyType not in RSAKeyType:
        raise ValueError("keyType has to be either RSAPublicKey or RSAPrivateKey.")
    
    rsa_key_class: RSAPublicKey | RSAPrivateKey = keyType.value
    rsa_key = rsa_key_class()
    rsa_key.setComponentByName(MODULUS, modulus)
    rsa_key.setComponentByName(PUBLIC_EXPONENT if isinstance(rsa_key, RSAPublicKey) else PRIVATE_EXPONENT, exponent)

    der_encoded_key = encoder.encode(rsa_key)
    return base64.b64encode(der_encoded_key).decode(ENCODING)


def write_key_to_file(filename: str, base64_encoded_key: str, keyType: RSAKeyType) -> None:
    """Writes the key to the given filepath."""
    if keyType not in RSAKeyType:
        raise ValueError("keyType has to be either RSAPublicKey or RSAPrivateKey.")
    
    keytype_string = 'PUBLIC' if keyType.value == RSAPublicKey else 'PRIVATE'
    der_key = f"-----BEGIN {keytype_string} KEY-----\n{base64_encoded_key}\n-----END {keytype_string} KEY-----"
    with open(filename, "wb") as der_file:
        der_file.write(der_key.encode(ENCODING))
    

def read_key_from_file(filename: str) -> bytes:
    """Reads the key from the given filepath, removing unneccessary formatting and returning the base64 decoded string."""
    with open(filename, "r") as f:
        der_key: str = f.read()
    
    substrings = [
        "-----BEGIN PUBLIC KEY-----",
        "-----END PUBLIC KEY-----",
        "-----BEGIN PRIVATE KEY-----",
        "-----END PRIVATE KEY-----",
        "\n", 
        "\r"
    ]
    for ss in substrings:
        der_key = der_key.replace(ss, "")
    
    der_key = base64.b64decode(der_key)
    return der_key


def decode_base64_key(base64_str: bytes, keyType: RSAKeyType) -> Tuple[int, int]:
    """
    From the base64 string, the function decodes the exponent and the modulus.
    Returns a tuple containing the exponent and the modulus.
    """
    if keyType not in RSAKeyType:
        raise ValueError("keyType has to be either RSAPublicKey or RSAPrivateKey.")

    asn1_key, _ = decoder.decode(base64_str, asn1Spec=keyType.value())
    exponent_type = PUBLIC_EXPONENT if keyType == RSAKeyType.PUBLIC else PRIVATE_EXPONENT
    return (int(asn1_key[exponent_type]), int(asn1_key[MODULUS]))
