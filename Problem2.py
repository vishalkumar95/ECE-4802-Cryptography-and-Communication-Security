""" Computes b^e mod m using the square and multiply algorithm"""
def my_pow(b, e, m):
    # Index for the reference
    i = -1
    # List to store all the results including intermediate steps
    output = []
    # Run the loop as long as e is greater than 0
    while e > 0:
        # e mod 2 should be 1
        if (e % 2 == 1):
            # If index is initialized i.e. -1
            if i == -1:
                # Append the result to the output list by taking the first element 
                output.append((1 * b) % m)
            # If index i is not -1, take the previous output and compute and then append it to the list
            else:
                # Append the result to the output list
                output.append((output[i] * b) % m)
            # Increment the index
            i += 1
        # compute b
        b = (b * b) % m
        # bit shift e
        e >>= 1
    # return the output
    return output

# Instantiate the function with first input
output1 = my_pow(235973, 456789, 583903)
# print the output
print (output1)

# Instantiate the function with second input
output2 = my_pow(984327457683, 2153489582, 994348472629)
# print the output
print (output2)
