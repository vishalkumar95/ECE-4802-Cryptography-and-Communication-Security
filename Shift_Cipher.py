# This python function implements the brute force method for the shift cipher

def decryptShift(ciphertext):
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(Letters)):
        newstring = ' '
        for j in ciphertext:
            if j in Letters:
                val = Letters.find(j)
                val = val - i
                val = val % 26
                newstring = newstring + Letters[val]

            else:
                newstring = newstring + j
        print (newstring)
            

                
            
                
                
