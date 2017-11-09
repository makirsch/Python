
"""
Line Index and Text Comparison Program

By Michael Kirsch

For Dr. Weimen He

This program uses the dictionary and set functions to create a dictionary from
the Gettysburg address and a comparison of two sets from the Gettysburg Address and
the Declaration of Independence.  It consists of a "main" function with two parts,
and four other functions that are used in the main function.

First, the main function opens a text file and passes the file object to "print
index" for processing and printing. "Print index" creates dictionary of processed
words from the file object, where the keys are the words and the key values are
line numbers. Two for loops, one for the line in file and one for the word in line,
are used. A line counter is used to achieve a line assignment to each word. Two
helper functions are called in "print index": get_words to compare the initial
file object's words with a second file object's words, and a second, "pretty
print dict" to print the completed dictionary so that the key values are sorted.

Second, the main function opens two text files and sends their file objects to the
compare_files function. "Compare files" obtains two sets of words by calling the
get_words function and then uses two set methods, set.union and set.intersection
to obtain information about the sets.

"""


import string


# Functions used in the Main Program
def pretty_print_dict(index_dict):  # Used in print_index function
    index_lst = [item for item in index_dict.items()]  # Create a tuple from dictionary items
    index_lst.sort()  # Sort the tuple
    for word, line_set in index_lst:
        line_lst = [l for l in line_set]  # Collect the line values
        line_lst.sort()  # Sort the line values (ints)
        line_str = str(line_lst[0])  # Turn line ints into strings for printing
        for line_no in line_lst[1:]:
            line_str += ", {}".format(line_no)
        print("{:12s}:".format(word), line_str)


def get_words(file_obj):  # Passes set of words back to print_index and compare_files
    result_set = set()  # Initial word set value
    for line in file_obj:  # Formats each line and word of text file
        line = line.strip()
        word_lst = line.split()
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        for w in word_lst:  # Puts each formatted word into the set
            if w:
                result_set.add(w)
    return result_set


def print_index(file_obj1):  # Prints word, line number index
    index_dict = {}  # Initial dictionary
    line_no = 0  # Initial line value for word keys
    for line in file_obj1:  # Search through each line of text file
        line = line.strip()  # Remove white space
        line = line.split()  # Split lines into individual words
        line_no += 1
        for word in line:
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            file_obj2 = open("mainWords.txt", "r")
            main_words = get_words(file_obj2)  # Create word comparison list
            file_obj2.close()
            if word in main_words:  # Check if word in line in main words collection
                if word in index_dict:
                    index_dict[word].add(line_no)  # Add additional line appearance to key (word) value (line)
                else:
                    index_dict[word] = {line_no}  # Add key to dictionary with value of first line appearance

    pretty_print_dict(index_dict)  # Passes completed dictionary for formatted printing


def compare_files(f1, f2):
        gba_set = get_words(f1)  # Obtain word set for Gettys. Adr.
        doi_set = get_words(f2)  # Obtain word set for Dec.Ind.
        print('{} {}'.format('The total number of words:', len(gba_set.union(doi_set))))  # Union
        print('{} {}'.format('Words in common:', len(gba_set.intersection(doi_set))))  # Intersection


#  Main Program
def main():

    # Calls the print_index function
    print("Main Words, Lines in Gettysburg Address")
    print('-' * 40)
    file_obj1 = open("gettysBurg.txt")
    print_index(file_obj1)
    file_obj1.close()
    print()

    #  Calls the compare files function
    print("Comparing Gettysburg Address and\nDeclaration of Independence")
    print('-' * 32)
    f1 = open("gettysBurg.txt")
    f2 = open("declarationOfInd.txt")
    compare_files(f1, f2)
    f1.close()
    f2.close()

main()

