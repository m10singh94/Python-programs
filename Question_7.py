# THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
# FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can define
# functions other than the one that is required, if you want to break
# the problem down into several functions. You can use docstrings, but
# only inside a function definition, and then only at the very beginning
# of the function suite.

# Modify the following function definition so that it computes and
# returns the correct answer to the problem. (The statement "return None"
# is just a placeholder: you should replace it.)


def smallest_greater_equal(sequence, target):
    greater_or_equal = sequence[0]
    smallest_greater_or_equal = max(sequence)
    for ch in sequence:
        if ch > target:
            greater_or_equal = ch
            if greater_or_equal < smallest_greater_or_equal:
                smallest_greater_or_equal = greater_or_equal
               
    return smallest_greater_or_equal
