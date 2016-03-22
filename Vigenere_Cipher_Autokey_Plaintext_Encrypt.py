# This function is an implementation of the autokey Vigenere cipher algorithm.

def encryptVigenere(plaintext, key):

    ciphertext = plaintext
    ciphertextbreak = []
    ciphertextbreakextra = []
    plaintextbreak = []
    smallLetters = 'abcdefghijklmnopqrstuvwxyz'
    Letters = smallLetters
    keylength = len(key)
    ciphertextlength = len(ciphertext)
    diff = ciphertextlength - keylength
    finalplaintext = list('.' * ciphertextlength)

    ciphertextbreak.append(ciphertext[0 : keylength])
    ciphertextbreakextra.append(ciphertext[:diff])
    plaintextbreak.append(ciphertext[-diff:])

    for i in range(0, len(ciphertextbreak)):
        for j in range(0, keylength):
            indkey = smallLetters.index(key[j])
            indcipher = Letters.index(ciphertextbreak[i][j])
            newindcipher = indcipher + indkey
            modindcipher = newindcipher % 26
            finalplaintext[j] = smallLetters[modindcipher]

    for i in range(0, diff):
        indkey = Letters.index(ciphertextbreakextra[0][i])
        indcipher = Letters.index(plaintextbreak[0][i])
        newindcipher = indcipher + indkey
        modindcipher = newindcipher % 26
        finalplaintext[keylength + i] = smallLetters[modindcipher]

    plaintextfinal = "".join(finalplaintext)
    plaintextfinal = plaintextfinal.upper()
    print(plaintextfinal)
        

                                            
        
    
