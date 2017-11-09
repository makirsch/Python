"""

Writing File and Making Dictionary Program:
Exercise in Exceptions

By Michael Kirsch

For Dr. Weimen He

This Program is made up of two programs that work independently and also together.

The first program main1, opens a file and prompts the user for two space separated
integers. A comprehension is used to define the characteristic of the two integers.
A try-except block is used to repeatedly prompt the user for this input and then
write a valid entry to the opened file, or give an error message for invalid entry.

The second program, main2, uses the two-integer comprehension in a more complicated
series of try-except blocks, geared toward creating a dictionary of proper user
entries. Any file, including the file just written, is read line by line using a
for loop and a valid line, one of two space separated integers, is added to a
dictionary.  Invalid lines are not added and an error message is given.
The final dictionary is printed. The program uses three nested try-except blocks.

A unique feature of the two programs put together is that if the user opens the
file that was written to by the first program, then the second program will not
flag any lines as invalid lines, and no error messages will be given.  The dictionary
printed will then be exactly what was written to the first file.

"""

# Program 1: Writing space separated integers to file


def main1():

    input_file = input("Input a file to open:")
    text = open(input_file, "w")

    while True:
            try:
                integers = input("Enter two integers (separated by space):")
                """ Comprehension defining proper user entry as space separated
                integers"""
                a, b = [int(s) for s in integers.split()]

                if a < 0:  # Loop quits when first integer entered is negative
                    break
                else:
                    text.write(str(integers))  # Valid entry is written to file
                    text.write("\n")

            except ValueError:  # Non-integer value, too many/too few values
                    print("Bad input", integers)

    text.close()

main1()



""" Program 2 """


def main2():

    while True:

        try:
            input_file = input("File to open is:")
            text = open(input_file, "r")

            dictionary = {}

            while True:
                counter = 1
                for line in text:  # Reads each line of the file

                    try:
                        a, b = [int(s) for s in line.split()]  # Check for valid line

                    except ValueError:
                        print("Bad line [{}]: {}".format(counter, line))  # Invalid line
                    else:
                        try:
                            if dictionary[a]:  # If integer(key) is in dict., add value to key
                                dictionary[a] += b

                        except KeyError:
                            dictionary[a] = b  # If integer does not yet exist in dict., add, set value
                    counter += 1
                print("Final dictionary:")
                for i in dictionary:
                    print(i, ":", dictionary[i])  # Prints key and value
                text.close()
                break
            break
        except IOError:  # Checks for invalid file to open
            print("Bad file name. Try again.")

main2()


