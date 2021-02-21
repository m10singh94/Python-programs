# COMP1730/6730 S1 2020 - Homework 4
# Due date: 11:55pm, Thursday, 30 April, 2020.

# YOUR ANU ID: u7075106
# YOUR NAME: Maitreyi Singh


def max_relative_frequency(string):
    ''' Input - This function takes in a string.
        Fuctionality - This function calculates the maximum relative frequency
            of characters in a given string. The maximum relative frequency is 
            equal to the ratio of frequency of letter occurring the maximum 
            number of times to the total number of letters present in the 
            string. 
        Output - The function returns the maximum relative frequency in float.
            If the string doesn't have any letter, the function returns 0.0.'''
        
    frequency = 0.0  # maximum relative frequency
    total_letters = num_of_alphabets(string.lower())
    if total_letters == 0:
        return frequency
    ls_counts = [] # this list stores the frequency of each letter of string
    ls_values = [] # this list stores the characters in string already checked 
    index = 0
    while index < len(string):
        if string[index].lower() >= 'a' and string[index].lower() <= 'z':
            if (string[index].lower() not in ls_values):
                count = string.lower().count(string[index].lower())
            ls_counts.append(count)
            ls_values.append(string[index].lower())
        index += 1
    frequency = max(ls_counts)/total_letters    
    return frequency


def num_of_alphabets(string):
    ''' Input - This function takes in a string.
        Fuctionality - This function calculates the count of letters present 
            in the string.
        Output - If the string does not contain any letter, it returns 0 
            otherwise returns the count of letters in that string.'''
        
    count = 0
    for ch in string:
        if ch >= 'a' and ch <= 'z':
            count += 1
    return count


# REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
# OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
# use docstrings to document your functions, but a docstring should only
# be used inside a function definition, and then only at the very beginning
# of the function suite. Everywhere else you should use comments.

# You may define other functions to help you solve sub-problems if you wish.

# YOU MAY NOT USE IMPORT STATEMENTS FOR THIS HOMEWORK.

# IF YOUR FILE DOES NOT SATISFY THESE REQUIREMENTS IT WILL NOT BE MARKED.
