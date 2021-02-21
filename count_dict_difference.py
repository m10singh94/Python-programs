
# Implement the function count_dict_difference below.
# You can define other functions if it helps you decompose and solve
# the problem.
# Do not import any module that you do not use!

# Remember that if this were an exam problem, in order to be marked
# this file must meet certain requirements:
# - it must contain ONLY syntactically valid python code (any syntax
#   or indentation error that stops the file from running would result
#   in a mark of zero);
# - you MAY NOT use global variables; the function must use only the
#   input provided to it in its arguments.

def count_dict_difference(A, B):
    result_dict = {}
    for key in A.keys():
        if key in B.keys():
            if A[key] - B[key] > 0:
                result_dict[key] = A[key] - B[key]
        else:
            result_dict[key] = A[key]
    return result_dict


def test_count_dict_difference():
    """
    This function runs a number of tests of the count_dict_difference function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """

    assert count_dict_difference({'d': 3, 'e': 1, 'z': 1, 's': 1, 'i': 1, 'r': 1, 'a': 2, 'n': 1, 't': 1}, {'e': 2, 'x': 1, 'g': 1, 's': 1, 'p': 1, 'i': 1, 't': 1, 'a': 2, 'n': 1, 'r': 1}) == {'z': 1, 'd': 3}
    assert count_dict_difference({'m': 1, 'o': 1, 'c': 2, 'r': 1, 'i': 2, 't': 1, 'a': 2, 'n': 1, 'l': 2, 'u': 1}, {'m': 2, 'o': 2, 'c': 1, 'z': 1, 'a': 2, 'i': 5, 'u': 1, 'r': 2, 'n': 2, 's': 1, 't': 2}) == {'l': 2, 'c': 1}
    assert count_dict_difference({'g': 1, 'c': 1, 'a': 2, 'i': 2, 'u': 1, 'r': 1, 'n': 1, 'l': 1, 't': 2}, {'g': 1, 'c': 1, 's': 1, 'a': 2, 'i': 2, 't': 2, 'r': 2, 'l': 2, 'u': 2}) == {'n': 1}
    assert count_dict_difference({'o': 1, 's': 5, 'i': 2, 'a': 3, 'n': 2, 't': 1}, {'o': 1, 'c': 1, 'z': 1, 'i': 2, 't': 2, 'a': 3, 'n': 1, 'l': 1, 'u': 1}) == {'s': 5, 'n': 1}
    assert count_dict_difference({'o': 2, 'c': 1, 'e': 2, 's': 2, 'r': 2, 'n': 2, 't': 1}, {'d': 2, 'c': 1, 'e': 3, 'a': 1, 't': 1, 'r': 2, 'o': 2, 'v': 1}) == {'s': 2, 'n': 2}
    assert count_dict_difference({'e': 4, 'g': 2, 's': 5, 'a': 1, 'i': 1, 'r': 1, 'n': 1, 'v': 1}, {'o': 1, 'i': 1, 'g': 1, 'c': 2, 'e': 1, 'a': 2, 'k': 1, 'u': 1, 'r': 1, 'n': 2, 't': 3}) == {'s': 5, 'e': 3, 'g': 1, 'v': 1}
    
    assert count_dict_difference({0: 1, 17: 2, 2: 1, 19: 2, 4: 1, 8: 2, 18: 1, 13: 1, 14: 1, 15: 1}, {0: 2, 17: 1, 2: 1, 19: 2, 4: 1, 8: 2, 20: 1, 11: 1, 13: 1, 14: 1, 15: 1}) == {17: 1, 18: 1}
    assert count_dict_difference({0: 1, 17: 1, 18: 2, 19: 1, 4: 1, 8: 4, 11: 1, 12: 1}, {0: 1, 17: 2, 2: 1, 19: 1, 4: 2, 8: 1, 20: 1, 11: 2, 12: 1, 13: 1, 14: 1}) == {8: 3, 18: 2}
    assert count_dict_difference({0: 1, 17: 1, 18: 3, 3: 1, 4: 3, 6: 2, 13: 1}, {0: 2, 17: 1, 2: 1, 3: 1, 4: 1, 8: 1, 24: 1, 18: 1, 12: 1, 13: 1, 14: 1}) == {18: 2, 4: 2, 6: 2}
    assert count_dict_difference({0: 3, 3: 1, 4: 1, 6: 1, 11: 1, 13: 1, 14: 1, 18: 1, 19: 1, 20: 1, 21: 1, 24: 1}, {17: 1, 18: 1, 3: 1, 4: 2, 21: 1, 6: 1, 8: 1, 20: 1, 11: 1, 13: 1, 14: 1}) == {0: 3, 24: 1, 19: 1}
    assert count_dict_difference({17: 2, 2: 1, 3: 2, 4: 2, 13: 1, 18: 1, 14: 2, 15: 1}, {0: 1, 17: 2, 2: 1, 4: 2, 5: 1, 18: 1, 12: 1, 13: 3, 14: 2, 15: 1}) == {3: 2}
    assert count_dict_difference({0: 1, 18: 6, 4: 2, 11: 1, 12: 1, 13: 1}, {0: 1, 17: 1, 2: 1, 19: 1, 4: 2, 6: 1, 11: 1, 12: 1, 13: 1, 14: 2}) == {18: 6}

    assert count_dict_difference({'in': 1, 'ti': 1, 'iv': 1, 'se': 1, 've': 1, 'en': 1, 'ns': 2, 'it': 1, 'si': 1}, {'ve': 1, 'ti': 1, 'iv': 1, 'si': 1, 'it': 1, 'ns': 2, 'st': 1, 'ra': 1, 'tr': 1, 'in': 1, 'an': 1}) == {'se': 1, 'en': 1}
    assert count_dict_difference({'th': 1, 'gt': 1, 'le': 1, 'en': 2, 'ng': 1, 'he': 1, 'ed': 1, 'ne': 1}, {'th': 1, 'ed': 1, 'ng': 1, 'en': 2, 'gt': 1, 'st': 1, 'he': 1, 're': 1, 'tr': 1, 'ne': 1}) == {'le': 1}
    assert count_dict_difference({'sm': 2, 'ri': 1, 'me': 2, 'es': 1, 'is': 1, 'er': 1}, {'di': 1, 'er': 1, 'st': 1, 'is': 1, 're': 1, 'dn': 1, 'si': 1, 'ne': 1, 'in': 1, 'ed': 1, 'nt': 1, 'es': 3, 'se': 1, 'ss': 1, 'te': 2}) == {'me': 2, 'ri': 1, 'sm': 2}
    assert count_dict_difference({'iz': 1, 'on': 1, 'al': 1, 'ze': 1, 'li': 1, 'at': 1, 'na': 2, 'ti': 1, 'io': 1}, {'za': 1, 'ra': 1, 'on': 2, 'al': 1, 'li': 1, 'iz': 1, 'at': 2, 'na': 1, 'ti': 2, 'io': 2}) == {'ze': 1, 'na': 1}

    assert count_dict_difference({(0, 5, 6): 1, (0, 5): 1, (5, 5): 2, (5, 0): 1, (5, 6): 1, (5, 5, 0): 1, (6, 5, 5): 1, (5, 5, 5): 1, (6, 5): 1, (5, 6, 5): 1}, {(0, 5, 5): 1, (5, 5, 6): 1, (0, 5): 1, (5, 5): 2, (5, 0): 1, (5, 6): 1, (6, 5, 0): 1, (5, 5, 5): 1, (6, 5): 1, (5, 6, 5): 1}) == {(0, 5, 6): 1, (5, 5, 0): 1, (6, 5, 5): 1}
    assert count_dict_difference({(2, 0): 1, (7, 7, 7): 2, (8, 7): 1, (8, 7, 7): 1, (7, 2, 0): 1, (7, 7): 3, (7, 2): 1, (7, 7, 2): 1}, {(8, 7, 7): 1, (2, 0): 1, (7, 2, 0): 1, (8, 7): 1, (7, 8, 7): 1, (7, 7, 8): 1, (7, 8): 1, (7, 7): 2, (7, 2): 1, (7, 7, 2): 1}) == {(7, 7, 7): 2, (7, 7): 1}
    assert count_dict_difference({(8, 8, 5): 1, (0, 8, 8): 1, (8, 8): 1, (8, 5, 3): 1, (5, 3, 0): 1, (3, 0): 1, (3, 0, 8): 1, (0, 8): 2, (8, 5): 1, (5, 3): 1}, {(8, 8, 5): 1, (3, 0, 0): 1, (8, 8): 2, (8, 5, 3): 1, (5, 3, 0): 1, (3, 0): 1, (8, 8, 8): 1, (8, 5): 1, (0, 0): 1, (5, 3): 1}) == {(3, 0, 8): 1, (0, 8, 8): 1, (0, 8): 2}
    
    print("all tests passed")

