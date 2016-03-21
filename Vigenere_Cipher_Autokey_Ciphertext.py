# This function is an implementation of the autokey Vigenere cipher algorithm.

def decryptVigenere(ciphertext, key):

    ciphertextbreak = []
    ciphertextbreakextra = []
    ciphertextbreakkey = []
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smallLetters = 'abcdefghijklmnopqrstuvwxyz'
    keylength = len(key)
    ciphertextlength = len(ciphertext)
    diff = ciphertextlength - keylength
    finalplaintext = list('.' * ciphertextlength)

    ciphertextbreak.append(ciphertext[0 : keylength])
    ciphertextbreakextra.append(ciphertext[-diff:])
    ciphertextbreakkey.append(ciphertext[:diff])

    for i in range(0, len(ciphertextbreak)):
        for j in range(0, keylength):
            indkey = smallLetters.index(key[j])
            indcipher = Letters.index(ciphertextbreak[i][j])
            newindcipher = indcipher - indkey
            modindcipher = newindcipher % 26
            finalplaintext[j] = smallLetters[modindcipher]

    for i in range(0, diff):
        indkey = Letters.index(ciphertextbreakkey[0][i])
        indcipher = Letters.index(ciphertextbreakextra[0][i])
        newindcipher = indcipher - indkey
        modindcipher = newindcipher % 26
        finalplaintext[keylength + i] = smallLetters[modindcipher]

    plaintext = "".join(finalplaintext)
    plaintext = plaintext.upper()
    print(plaintext)
        

                                            
        
    
