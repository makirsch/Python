import math

"""
*** Integer, Binary String Converter Program *** 

This program converts integers into binary numbers and subsequently 
back into integers.

The first part of the program converts the integer into a binary strings using 
a two-part while-loop. The integer is divided by two and each successive remainder 
is stored in a new variable: remainder_str. The remainders are also converted 
into strings such that the completed concatenation of all the remainders can be 
printed backwards after the while-loop. This is done using the palindrome 
technique, generating the binary string. 

In the second part, each digit of the binary string is assigned a value of 0 or 
2^x, where the power depends on the digits position in the string. The last digit 
receives a value of 2^0, the preceding digit receives a value of 2^1, and so on.  

In order to step through the binary string backwards and assign the correct 
power-of-two values, the code reverses the initial binary string, and uses the 
index feature of the enumerate statement. Applying the palindrome approach here 
makes it possible to obtain an index equal to the correct power-of-two value 
starting at index 0, rather having than to convert negative index values, starting 
at -1, into the correct power-of-two. 
"""

# 1. Generate a binary string for an integer
print("Let's convert an integer into binary.")
integer_str = input("Enter an integer:")
integer_int = int(integer_str)
remainder_str = ""  # Initial value for the while loop below
if integer_int == 0:
    print("Your integer is 0.")
elif integer_int < 0:
    print("Your integer is negative.")
else:
    while integer_int > 0:  # Runs until integer is zero
        binary_digit = integer_int % 2  # Find remainder for initial value
        remainder_str = remainder_str + str(binary_digit)  # Convert remainder to str; add to total
        integer_int //= 2  # Find quotient for next integer to put through loop

    binary_str = remainder_str[::-1]  # Reverse the order of binary string
    print("The binary of", integer_str, "is", binary_str)
    print()

# 2. Convert the binary string into an integer
    print("Now let's convert the binary back into an integer.")
    integer = 0
    binary_str_back = binary_str[::-1]  # Reverse the order of str for evaluation
    for index, digit in enumerate(binary_str_back):  # Evaluate each digit with its index
        if digit == "0":
            pass  # Do nothing
        else:
            integer += 2 ** int(index)  # Use index values as powers of two

    print("The integer value of", binary_str, "is:", integer)

    print("Thanks for playing.")


