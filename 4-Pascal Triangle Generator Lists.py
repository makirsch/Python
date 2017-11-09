"""
Pascal Triangle Program

By Michael Kirsch

For Dr. Weimen He

This program creates Pascal's triangle for any height.  It is executed with one
function and two For-loops.

The function, "make new row(old_row)," employs a For-loop to turn each row of
Pascals triangle, as lists, into the next row, starting with the first row, [1].
The For-loop achieves this by appending to the previous row numbers that are
additions of two numbers of the old row. This is achieved correctly by setting
the range of the For loop equal to the range of the starting row.

The second For-loop executes the program.  Its range is equal to the user's input,
and it generates each next row in one loop of the For-loop by calling on the
"make new row" function. This is achieved by having the initial value of "old row"
equal to a blank list, and then resetting its value at the end of the For-loop to
the new row just created.  The loop thus starts over with the next row of Pascal's
triangle and runs till the end of the range, set by the user input as the desired
height of the triangle.

"""


# 1. Make New Row Function

def make_new_row(old_row):

    if old_row == []:  # Value not appropriate for loop
        return [1]
    if old_row == [1]:  # Value not appropriate for loop
        return [1, 1]
    n = len(old_row) - 1  # For-loop range equal to old row range
    new_row = [1]  # Starting value of list
    for i in range(n):
        new_row.append(old_row[i] + old_row[i+1])  # Value of each new row index
    new_row.append(1)
    return new_row


# 2. Main Program

n = int((input("Enter the desired height of Pascal's Triangle:")))
print()
print("Printing list of lists, one list at a time:")

list_of_lists = []
old_row = []  # Initial value for loop

for i in range(n):
    new_row = make_new_row(old_row)  # Makes a row with input of old row
    print(new_row)
    list_of_lists += [new_row]  # Concatenates each list together
    old_row = new_row  # Sets up next list for function to transform

print()
print("Printing whole list of lists:")
print(list_of_lists)
