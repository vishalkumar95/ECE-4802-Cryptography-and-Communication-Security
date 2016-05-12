# Name: Vishal Rathi
##

from Crypto.Cipher import AES

key = b'Sixteen byte key'
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
out = b''
m1 = b'The quick brown fox jumps over the lazy dog'
m = b'The quick brown fox jumps over the lazy doh'

def tobits(s):
    """Change the value in s to its binary representation."""
    # Get the length of the input string
    length = len(s)
    # Create an empty list
    outputbits = [0] * length
    # Run the for loop
    for i in range(0, length):
        # Create an empty string
        stchar = ''
        # Run the loop for each character
        for char in s[i]:
            # Convert each character to bit
            stchar = stchar + format(ord(char), 'b')
        # Get the output 8 bits
        outputbits[i] = stchar.zfill(8)
    # Join everything and make it a multiple of 8 bits
    outputbits = ''.join(outputbits)
    # Return the output bits
    return outputbits


def frombits(bits):
    """change the value in bits to string."""
    # Create an empty string
    outputstring = ''
    # Get the length of bits
    length = len(bits)
    # Run the for loop
    for i in range(0, int(length / 8)):
        # Get the character for each 8 bits
        temp = chr(int(bits[8 * i:8 * i + 8], 2))
        # Append each character to a string
        outputstring = outputstring + temp
    # return the string
    return outputstring


def padding(message):
    """Append padding to message in order to
       become multiple of 16 in order to fit in
       AES input"""

    # Convert the string to bits by calling the tobits function
    mbits = tobits(message)
    # Get the length of bits
    length = len(mbits)
    # Calculate the strengthening vector length
    strengthmessage = (bin(int(length))[2:]).zfill(64 * ((len(bin(int(length))[2:]) + 63) // 64))

    # Create a padding which starts with 1
    padding = '1'
    # Get the number of zeroes to pad
    get_length = 128 - (length + 64) % 128
    # Run the for loop to append all 0's
    for i in range(0, get_length - 1):
        padding = padding + '0'

    # Make the entire pad    
    to_add_pad = padding + strengthmessage
    # Return the entire pad
    return to_add_pad

def CBCMACbasedOnAES(message, key):
    """This function computes the MAC of message using key.
       The MAC function is CBC-MAC with AES and both single-1
       padding and length strengthening provided by the
       padding function.
       key must be convertible to bytes of length 16
       messuge must be convertible to bytes type"""

    # Convert the message into bytes
    message1 = bytes(message)
    # Convert the key into bytes
    key1 = bytes(key)

    # Create the AES object
    aes_obj = AES.new(key1, AES.MODE_CBC, iv)
    # Encrypt the message
    MAC = aes_obj.encrypt(message1)
    # Return the MAC of the message
    return MAC

# Instantiate all the functions
def main():

    # First message
    
    # Get the bits of the message
    mbits = tobits(m)
    # Get the padding to add
    pad = padding(m)
    # Add the bits with the pad
    temp = mbits + pad
    # Convert the bits to string
    add_pad = frombits(temp)

    # Second message

    # Get the bits of the message
    mbits1 = tobits(m1)
    # Get the padding to add
    pad1 = padding(m1)
    # Add the bits with the pad
    temp1 = mbits1 + pad1
    # Convert the bits to string
    add_pad1 = frombits(temp1)

    # Get the MAC from the function
    MAC = CBCMACbasedOnAES(add_pad, key)

    # Get the MAC from the function
    MAC1 = CBCMACbasedOnAES(add_pad1, key)

    # Convert it back to bits
    convertbits = tobits(MAC)
    # Create an empty list
    bitlist = []
    # Get the length
    length = len(convertbits)
    # Convert bits back to string
    for i in range(0, int(length / 8)):
        bitlist.append(chr(int(convertbits[8 * i:8 * i + 8], 2)))

    # Convert it back to bits
    convertbits1 = tobits(MAC1)
    # Create an empty list
    bitlist1 = []
    # Get the length
    length1 = len(convertbits1)
    # Convert bits back to string
    for i in range(0, int(length1 / 8)):
        bitlist1.append(chr(int(convertbits1[8 * i:8 * i + 8], 2)))

    # Print the required vector
    print (bitlist[48:96])

    # Print the required vector
    print (bitlist1[48:96])


if __name__ == '__main__':
    main()
