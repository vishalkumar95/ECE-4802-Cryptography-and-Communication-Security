# This function is an implementation of the Vigenere cipher algorithm.

def decryptVigenere(ciphertext, key):

    ciphertextbreak = []
    ciphertextbreakextra = []
    finalplaintext = ' '
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    smallLetters = 'abcdefghijklmnopqrstuvwxyz'
    keylength = len(key)
    ciphertextlength = len(ciphertext)

    modval = ciphertextlength % keylength
    if (modval == 0):
        for i in range(0, ciphertextlength, keylength):
            ciphertextbreak.append(ciphertext[i : i + keylength])

        for i in range(0, len(ciphertextbreak)):
            for j in range(0, keylength):
                indkey = smallLetters.index(key[j])
                indcipher = Letters.index(ciphertextbreak[i][j])
                newindcipher = indcipher - indkey
                modindcipher = newindcipher % 26
                finalplaintext = finalplaintext + Letters[modindcipher]

    elif (modval != 0):
        for i in range(0, ciphertextlength - modval, keylength):
            ciphertextbreak.append(ciphertext[i : i + keylength])

        for i in range(0, len(ciphertextbreak)):
            for j in range(0, keylength):
                indkey = smallLetters.index(key[j])
                indcipher = Letters.index(ciphertextbreak[i][j])
                newindcipher = indcipher - indkey
                modindcipher = newindcipher % 26
                finalplaintext = finalplaintext + Letters[modindcipher]

        ciphertextbreakextra.append(ciphertext[-modval:])
        for i in range(0, len(ciphertextbreakextra)):
            for j in range(0, modval):
                indkey = smallLetters.index(key[j])
                indcipher = Letters.index(ciphertextbreakextra[i][j])
                newindcipher = indcipher - indkey
                modindcipher = newindcipher % 26
                finalplaintext = finalplaintext + Letters[modindcipher]

    print (finalplaintext)
                
                                            
        
    
