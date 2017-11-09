import math

import string


"""
Program to Calculate the Surface Area and Volume of Cone

Student: Michael Kirsch
Professor: Dr. Weimen He

This program is separated into three parts. The first part consists of functions 
that ensure that user correctly enters input.  The first function, get_nneg_float 
gets user input and passes the input to another function, is_neg_float. This 
second function runs the value through a series of if and else statements 
to verify that the entry is a non-negative float. String methods find and indigit
to check input that contains decimal places and text. If the values are return False
the first function, get_nneg_float prompts the user again, repeating the process as 
many times as is required to get a proper entry.

The second part of the program employs two functions, one each to calculate the area
and volume of a cone based on a value passed from get_nneg_float. 

The third part of the program sets the above functions into action, calling them in 
order to obtain the area and volume of a cone, then printing theses values after they
are calculated.

"""


# 1. Functions to Prompt and Check User Input for Errors

def is_nneg_float(my_str):  # Function verifies if input is non-negative float
    if my_str.isdigit():  # String is an integer
        return True
    else:  # String is not an integer
            decimal = my_str.find(".")
            if decimal == -1:  # String has text and no decimal point
                return False
            else:  # String has one decimal place
                '''Scans left and right side of decimal point'''
                if decimal == 0 and my_str[decimal+1:].isdigit():
                    return True
                if not my_str[0:decimal].isdigit() or not my_str[decimal+1:].isdigit():
                    return False
                else:
                    return True  # String is non-negative float


def get_nneg_float():  # Function prompts user and returns cone parameters
    my_str = (input("Enter a number:"))
    while not is_nneg_float(my_str):  # Repeatedly prompts user for correct input
        print("Not a non-negative float.")
        my_str = (input("Enter a number:"))
    parameter = float(my_str)  # Convert string to float
    return parameter  # Input is verified non-negative float


# 2. Functions to Calculate Area and Volume

def surface_function(r, h):
    return math.pi * (r ** 2) + math.pi * r * math.sqrt(r**2 + h**2)


def volume_function(r, h):
    return (math.pi * (r ** 2) * h) / 3


# 3. Calling Functions to Prompt and Calculate, Prints Output

print("Select a radius in feet")
r = get_nneg_float()  # Prompts user and verifies correct radius entry
print("Select a height in feet")
h = get_nneg_float()  # Prompts user and verifies correct height entry
area = surface_function(r, h)
volume = volume_function(r, h)
print("Cone radius is:", round(r, 3), "ft.")
print("Cone height is:", round(h, 3), "ft.")
print("Cone surface area is:", round(area, 2), "sq. ft.")
print("Cone volume is:", round(volume, 2), "cu. ft.")


