# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers

def summer_69(ls):
    su = 0
    i = 0
    while i < len(ls):
        if(ls[i] == 6):
            while(ls[i] != 9):
                i += 1
            i += 1  # to skip the value 9
        if(i < len(ls)):
            su += ls[i]
        i += 1
    return su

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11, 6, 9]))