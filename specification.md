# Project specifications

###  What programming language are you using?
I'm going to be using Python, as that is the language I'm most familiar with. 

For peer reviews I sufficiently know my way around Java, C# and JavaScript.

### What algorithms and data structures are you implementing in your work?
I'm going to be implementing: 
- the Miller-Rabin prime test, to find large prime numbers
- algorithm to encode the message using the public key
- another to decode the message using the private key

### What problem are you solving?
Symmetrical encoding (meaning that the same key is used to encode and decode the secret message) algorithms are not really suited for applications like communicating through the internet, because to read the encrypted data, first you would somehow need to send the shared key to the reciever.\

Because that message would need to be unencrypted, the message could be easily intecepted and the key would be compromised. 

RSA solves this problem by each person having a public and private key. The public key is accessible to anyone, and the private key is only accessible to the owner.
For example, if someone wants to send me an encoded message through the internet, they would use my public key to encode their message, and only me with my private key would be able to decode it.

Another application for RSA is verification. Let's say I want to be able to prove that the message sent out is indeed sent by me. In this application, I would encode the message using my private key, and then anyone (because my public key is public of course) would be able to decrypt my message using my public key, thus proving that it was encoded by me, proving it's origin.

If we use both keys to encode the message, (meaning that when I'm sending the message, I'll first use my private key to encrypt it, then the reciever's public key to encrypt it once more) we can be sure that only the intended recipient can read the message, and also that it is from the expected source.

### What inputs does your program take, and how are these used?
The program takes a message as an input, then encodes the message, "sends it to the recipient" and then decryption happens. 

### Other neccessary information
The language of the documentation is English.

Bachelor of Science in Computer Science (CS)
