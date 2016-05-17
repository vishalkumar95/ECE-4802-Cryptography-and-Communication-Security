# Import the modules
import hashlib
import random
# import gensafeprime

# pseudo random generator; initialize it with a seed
random.seed(12345)

# Generate a 1024 bit prime number using gensafeprime library and using the generate function
# prime = gensafeprime.generate(1024)

# A prime number generated
prime = 154414168805347049188850715197940467801734973695006969238084857051240537697580848852652051539793786088058491229128108120906237426172602889034305837706920078172655507087739400430915580515529379434654679195256613650390809208260711964864592461305677216596334443114090579486055540684795004994486535998079578373339

# Find the safe prime
p = (prime - 1) / 2

# Generate random parameters
g = random.randint(2, prime - 2)
A = random.randint(2, prime - 2)
B = random.randint(2, prime - 2)

# Calculate the key 
k_A = pow(g, A*B, prime)

# use sha256 to encode the key
final = hashlib.sha256(hex(k_A).encode('utf-8'))

# Print the key
print(k_A)

# Print the sha256 hashed key
print("\nThe final key is ", final.hexdigest());

'''from binascii import hexlify
print("The final key in hex is ", hexlify(final.hexdigest()).decode('utf-8'))'''
