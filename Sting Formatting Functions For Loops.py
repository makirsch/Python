"""
Text Justification and String Padding Program

By Michael Kirsch

For Professor Dr. Weimen He

This program creates justified text blocks of desired width for specific types 
of texts, those with a digit at the beginning of each line, and a possible string 
of words with single spaces in between each word.

The "main" function prompts the user for a text files and the desired length of 
line.  It then calls on a "get_and_strip_number function," which removes separates 
the number at the front of the line from the rest of the line.  The "main" function 
then calls another function, "pad_words," which determines the number of spaces in 
the line adds spaces between words as necessary to meet the desired line length.  
Part of "Pad_words" is to call on a fourth function, "get_and_strip_words," to 
to separate each word from the line.  The main function prints the words by 
calling on pad_words. 

"""


def get_and_strip_number(line):  # receives line from user input
    ints = "0123456789"
    ints_in_line = ""  # initial value of integer for for-loop
    for i in line:
        if i in ints:
            ints_in_line += i  # concatenation of integer value at front of text line
            len(ints_in_line)
            space_index = int(len(ints_in_line))  # required type of space index
        else:
            break
    if int(line[0]) == 0 and len(line) == 1:   # the line of text has only a "0"
        return 0, ""
    if line[space_index] == " ":  # the line meets the required type
        n = int(ints_in_line)
        words = line.strip("0123456789")  # strips the number digit(s) from line
        return n, words[1:]  # returns number and rest of string
    else:
        print("Not a valid file")
        main()


def get_and_strip_word(words):

    if words == "":  # no words
        return "", ""
    if not words[0] == " " and not "":  # line of words meet requirement
        word = words[0:words.find(" ")]  # separates first word
        s = words[words.find(" "):]  # the rest of the line after first word
        return word, s[1:]
    else:
        print("Not the right type of text.")
        main()


def pad_words(s, num_words, final_len):
    # This part of the program written was by Prof.
    if num_words <= 1:      # best we can do is fill out the line with spaces
        return s + ((final_len - len(s))*' ')

    # there are at least 2 words, so at least one pigeon hole to fill (with spaces)
    num_pigeon_holes = num_words - 1                        # the buckets (pigeon holes) are between words
    num_pigeons = final_len - (len(s) - num_pigeon_holes)   # my pigeons are spaces
    pad_num = num_pigeons // num_pigeon_holes
    extra_num = num_pigeons % num_pigeon_holes              # number of holes that get an extra pigeon
    working_str = ''
    
    # take care of the first num_pigeon_holes - extra_num holes
    for i in range(num_pigeon_holes - extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + (pad_num * ' ')   # insert pad_num spaces

    # take care of the last extra_num holes
    for i in range(extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + ((pad_num + 1) * ' ')

    working_str += s
    return working_str


def main():
    """Main program for testing some text formatting functions."""
    file_name = input("Enter the name of the input file: ")
    file_obj = open(file_name, "r")

    print("Line length should be as long as the longest line to print, or longer.") 
    line_len = int(input("Enter the desired line length: "))
    print()

    for line in file_obj:
        line = line.strip()                   # strip the trailing '\n'
        n, words = get_and_strip_number(line)
        print(pad_words(words, n, line_len))

    file_obj.close()

main()


