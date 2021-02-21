"""
A short demonstration of reading and processing files in Python.
Was presented in Lecture 15.
"""

def print_with_line_numbers(file_name):
    """
    Prints out a code file with line numbers added at the beginning.
    Will only add print lines of code and blank lines - not comments or docstrings.
    :param file_name: the file name (or file path if in different directory) of the file to print
    """

    notes_file = open(file_name, mode="r")

    line_number = 1
    in_doc = False  # We need to keep track of whether we are in a docstring or not

    for line in notes_file:

        if line.strip() == "":  # We will print empty lines for readability
            print("")
        elif len(line.strip()) >= 3 and (line.strip()[:3] == '"""' or
                                         line.strip()[:3] == "'''"):  # Check first three characters
            in_doc = not in_doc
        elif not in_doc and line.strip()[0] != "#":
            print("{:<2}: ".format(line_number) + line, end="")
            line_number += 1

    notes_file.close()


print_with_line_numbers("longest_repeated_substring.py")
