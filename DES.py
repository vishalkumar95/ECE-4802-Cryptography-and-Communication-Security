# Define all the Bits
BIT0 = 0x01
BIT1 = 0x02
BIT2 = 0x04
BIT3 = 0x08
BIT4 = 0x10
BIT5 = 0x20

# This function would take an input and return an output according to the DES S-box 
def sBox(mystring):
    # Find the required row and column
    row = ((mystring & BIT5) >> 4) + (mystring & BIT0)
    column = (mystring & (BIT1 | BIT2 | BIT3 | BIT4)) >> 1

    # Define the S-Box table for lookup
    Table = [
	[0x07, 0x0D, 0x0E, 0x03, 0x00, 0x06, 0x09, 0x0A, 0x01, 0x02, 0x08, 0x05, 0x0B, 0x0C, 0x04, 0x0F],
	[0x0D, 0x08, 0x0B, 0x05, 0x06, 0x0F, 0x00, 0x03, 0x04, 0x07, 0x02, 0x0C, 0x01, 0x0A, 0x0E, 0x09],
	[0x0A, 0x06, 0x09, 0x00, 0x0C, 0x0B, 0x07, 0x0D, 0x0F, 0x01, 0x03, 0x0E, 0x05, 0x02, 0x08, 0x04],
	[0x03, 0x0F, 0x00, 0x06, 0x0A, 0x01, 0x0D, 0x08, 0x09, 0x04, 0x05, 0x0B, 0x0C, 0x07, 0x02, 0x0E]
	]

    # Return the output from the table
    return Table[row][column]

# This function computes the SAC based on the above implementation of the S-box.
def computefunction():
    # Initialize the 2-D array
    myinput = [[] for x in range(6)]
    # Make it all 0's 2D array
    for i in range(0, 6):
        for j in range(0, 4):
            myinput[i].append(0)

    # Compute the SAC in this loop
    for i in range(0, 64):
        for j in range(0, 6):
            sum1 = sBox(i) ^ sBox(i ^ (BIT0 << j))
            for k in range(0, 4):
                myinput[j][k] = myinput[j][k] + ((sum1 >> k) & BIT0)

    # return the output
    return myinput

# Call the computeFunction
arr = computefunction()
for r in range(0, 6):
    # Print the output
    print (arr[r])
