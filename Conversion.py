# Function to convert a Binary string to Decimal number
def Binary_to_Decimal(binary):
    length = len(binary)
    mysum = 0
    for i in range(length):
        a = int(binary[i])
        if a==1:
            mysum += 2**(length-i-1)
    return mysum


# Function to convert Decimal number to a binary string
def Decimal_to_Binary(decimal):
    binary = ""
    while (decimal >= 1):
        binary += str(decimal % 2)
        decimal = decimal // 2

    return binary[::-1]







