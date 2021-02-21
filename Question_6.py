# THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
# FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can define
# functions other than the one that is required, if you want to break
# the problem down into several functions. You can use docstrings, but
# only inside a function definition, and then only at the very beginning
# of the function suite.

# Modify the following function definition so that it computes and
# returns the correct answer to the problem. (The statement "return False"
# is just a placeholder: you should replace it.)


def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
