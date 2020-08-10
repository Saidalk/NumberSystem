
def main():
    print("This application will be converting Decimal numbers into Binary")

    decimal = valid()

    print("This is your number in binary:")
    Binary_conversion(decimal)


def valid():
    while True:
        z = int(input("Please enter the number:"))
        if (z <= 0):
            print("Your input must be a positive integer")
        else:
            return z
            break



def Binary_conversion(input): # this will convert using the divison method
    binary = []
    y = input
    while (True):
        if (y !=0 ):
            x_ = y // 2 # this gets the qoutient
            x = y % 2 # this gets the remainder (the binary value)
            y = x_
            binary.append(x)
        else:
            print(binary[::-1]) # this will reverse the array and therefore output the correct binary sequence
            break







main()




