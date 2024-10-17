# User guide

### Setting up the project:
1. Clone the repo to your local machine
2. Run `poetry install` to create a virtual environment with the required dependencies
3. Run `poetry shell` to enter the virtual environment
4. Run `python main.py` to run the demo application

### Using the demo application:
- Once you start the application, a two RSA keypairs will be generated.
  - Data about the keys (both the "Sender's" and "Reciever's" public and private keys) is printed to the terminal.
- You can enter a message you want to encode.
  - This message cannot be longer than the key's max byte value. (If you're using a 1024 bit key, you can encode a 128 char long message)
  - If it is longer, you'll see an error message, and the program will close.
- After entering the message, you're able to pick and a mode:
  - 1.) CONFIDENTIALITY (Encryption with the reciever's public key, decryption with their private key.)
  - 2.) AUTHENTICITY (Encryption with the sender's private key, decryption with the sender's public key.)
  - 3.) BOTH (Encryption first with the sender's private key, then the reciever's public key.Decryption 
using first the reciever's private key, then the sender's public key.)
- After you made your choice, the program encodes your message using the chosen method, and prints the ciphertext to the terminal.
- If you press enter again, the program decodes the ciphertext and displays the decoded message. The application terminates.
