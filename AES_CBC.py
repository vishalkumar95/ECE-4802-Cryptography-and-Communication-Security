# Template for Project 3:
# Name: Vishal Rathi
# Date: 4th April 2016
# Mailbox number:   270

# This is a simple Python (2) or sage program to open, read and write a .bmp file.
# Your task is to modify it so that the payload (but not the header) of
# the .bmp file is encrypted. 

# NOTE: in Sage, first upload the file >Gompei.bmp< onto the server using
# Data... --> Upload or create file  and then choosing the file from your machine
# next, use "Data... --> Upload or create file" to create the empty file 
# >Gompei_enc.bmp<. After you have your program working, you can download the modified
# >Gompei_enc.bmp< by clicking on "Data... --> Gompei_enc.bmp" and then choosing and
# downloading from the provided link to the file.

# Import the module
from Crypto.Cipher import AES

# opening the source file (a .bmp file)
with open('Gompei.bmp','rb') as in_file:
    # Playing a bit with the .BMP file format:

    # get size info:
    in_file.seek(2)
    # size = int.from_bytes(in_file.read(4),'little') # python 3
    size = int(in_file.read(4)[::-1].encode('hex'),16) # [::-1] fixes the endianness
    print('The file has ',size,' bytes.')

    # get to where the bit map begins
    in_file.seek(10)
    # offset = int.from_bytes(in_file.read(4),'little')
    offset = int(in_file.read(4)[::-1].encode('hex'),16) # [::-1] fixes the endianness
    print('Data starts at: ',offset)

    ## read data in chunks, encrypt and write to new file
    #open new file for writing
    with open('Gompei_enc.bmp','wb') as out_file:

        # read/write header
        in_file.seek(0)
        header = in_file.read(offset)
        out_file.write(header)

        # AES Encryption in the ECB mode
        key = '0' * AES.block_size
        IV = key
        AES_obj = AES.new(key, AES.MODE_CBC, IV)

        # read data in chunks of 64 bit
        buf = in_file.read(16)
        
        # Encrypt the buffer
        buf = AES_obj.encrypt(buf)

        while len(buf)==16:
            # write data in chunks of 64 bit:
            out_file.write(buf)

            # read data in chunks
            buf = in_file.read(16)
            
            # Encrypt the buffer
            buf = AES_obj.encrypt(buf)

        
        # write final chunk of data (not necessary since size is multiple of 16)
        out_file.write(buf)

    # files are automatically closed after leaving the "with"


