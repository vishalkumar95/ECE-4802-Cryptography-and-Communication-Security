def generateVigenere(index, keyword, plaintext):
    if (index < len(keyword)):
        return keyword[index]
    else:
        return plaintext[index - len(keyword)]
