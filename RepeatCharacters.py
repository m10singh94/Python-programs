# return a string having every letter repeated thrice
def repeat_character(st):
    s = ""
    for letter in st:
        s += letter * 3
    return s
print(repeat_character('Hello'))
print(repeat_character('Mississippi'))