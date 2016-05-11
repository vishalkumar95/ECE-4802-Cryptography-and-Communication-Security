# Passwords are in the format found in /etc/shadow: $[hash_algorithm_id]$[hash_salt]$[hash_data]
#
# This format optionally allows changing the number of rounds each hash function is applied:
# $[hash_algorithm_id]$rounds=[# of rounds]$[hash_salt]$[hash_data]
#
# For this homework exercise, the salt is prepended to the password and is only applied in the
# first round. The input to the next round of hashing is a hex string of the previous hash digest.
#
# Hash algorithm IDs and default rounds:
# 1 MD5 (1000 rounds)
# 2 Blowfish (64 rounds)
# 5 SHA256 (5000 rounds)
# 6 SHA512 (5000 rounds)
#
# To verify your password hash function works correctly, you can use the following test vectors:
#
# # pw = 'ECE 4802 rocks!'
# $6$rounds=1$ESw6=oECkdYnvX=y$c86eb8420756e3dd900f142f106b798427456546a08b596888d6a15ec484aab153795832ceef34282fb50fe4c68ca0f39ba13c1458135abccefd83d96c0e2632
# $6$rounds=42$gfqTrX3hUUNjldVu$7ef910c021ad14c5c8f0b195384af61abf520635ad5efb136b0bd9f48849867a59eac5236c607ccc323ea259963752de7c994ca67c096a447921417bd05d6aa6
#
# Using the given wordlist and template code, write code to crack the given passwords, i.e.,
# implement crack_passwords(). Code will be graded on readability, correctness and efficiency.
#
# In your final code, the ONLY thing that ought to be printed to STDOUT is the list of plainword
# passwords, newline separated, in their original order.
# Points will be docked for failure to adhere to this.

# Import the hash and time modules
import time
import hashlib

def get_hash_value(text, salt, rounds):
    # Calculate the hash value
    hash_val = hashlib.sha512((salt + text).encode('utf-8')).hexdigest()
    # Decrement the round
    rounds = rounds - 1
    # Calculate the new hash value for all the rounds
    while rounds > 0:
        # Calculate the hash value
        hash_val = hashlib.sha512(hash_val.encode('utf-8')).hexdigest()
        # Decrement the rounds
        rounds = rounds - 1
    # Return the hash value
    return hash_val
    
# return list of plainword passwords in the same order as `passwords_from_file`
def crack_passwords(passwords_from_file):
    output = []
    # Open the dictionary with the passwords
    with open('dictionary.txt', 'r') as fh:
        wordlist = [line.rstrip('\r\n') for line in fh.readlines()]
    # Open a word file to save the output
    pwd = 1
    with open("R:\\ECE 4802\\Project 4\\Progress_final.txt", "a+") as ofile, open('passwords.txt', 'r') as ifile:
        for line in ifile:
            # See if pwd is between 1 and 5
            if pwd in range(1, 6):
                # Rounds are 5000
                rounds = 5000 
                # Get the hash password
                pwd_hash = line.strip().split("$")[3].strip()
                # Start the timer to keep track of the time
                tStart = time.clock()
                # Check all the words in the wordlist
                for word in wordlist:
                    # Get the hash value
                    hash_value = get_hash_value(word, line.strip().split("$")[2], rounds)
                    # If the hash value matched print the output; we found the password
                    if hash_value == pwd_hash:
                        # Calculate the time difference
                        tDiff = time.clock() - tStart
                        # Print statements to print the output
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff, file = ofile)
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff)
                        # Append the output
                        output.append(word)
                        # break the loop
                        break
            # See if pwd is between 6 and 15
            elif pwd in range(6, 16):
                # Rounds are 5000
                rounds = 5000
                # Get the hash password
                pwd_hash = line.strip().split("$")[3]
                 # Start the timer to keep track of the time 
                tStart = time.clock()
                 # Check all the words in the wordlist
                for word in wordlist:
                    # Get the hash value
                    hash_value = get_hash_value(word, "", rounds)
                     # If the hash value matched print the output; we found the password
                    if hash_value == pwd_hash:
                         # Calculate the time difference
                        tDiff = time.clock() - tStart
                         # Print statements to print the output
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff, file = ofile)
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff)
                        # Append the output
                        output.append(word)
                        # Break the loop
                        break
            # See if pwd is between 16 and 20
            else:
                # Rounds are 5000
                rounds = 25000
                # Get the hash password
                pwd_hash = line.strip().split("$")[4]
                # Start the timer
                tStart = time.clock()
                # Check all the words in the wordlist
                for word in wordlist:
                    # Get the hash value
                    hash_value = get_hash_value(word, line.strip().split("$")[3], rounds)
                    # If the hash value matched print the output; we found the password
                    if hash_value == pwd_hash:
                        # Calculate the time difference
                        tDiff = time.clock() - tStart
                        # Print statements to print the output
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff, file = ofile)
                        print("Pwd", pwd, " ", word, " timeTaken ", tDiff)
                        # Append the output
                        output.append(word)
                        # Break the loop
                        break
            # Increment pwd
            pwd = pwd + 1
    
    return output # return list of plainwords (edit this line)

with open('passwords.txt', 'r') as fh:
    plainwords = crack_passwords([line.rstrip('\r\n') for line in fh.readlines()])
    print(plainwords)
