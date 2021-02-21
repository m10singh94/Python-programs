"""
Programming demonstration from lecture 9 - strings.
Find the longest repeated substring in a word.
"""


def longest_repeated_substring(word):
    """
    Finds the longest repeated sub-sequence of characters in a string
    :param word: string - the word to search in
    :return: string - the longest repeated substring.
    If there are two or more substrings tied for the longest - the one with the first
    instance in word will be returned.
    """

    # Since we are looking for the longest - start searching at the maximum possible length
    length = len(word) // 2
    while length > 0:
        index = 0
        # Go through the possible starting indexes and check whether the string appears later in word.
        while index + length < len(word):
            if word[index: index + length] in word[index + length:]:
                return word[index: index + length]

            index = index + 1
        length = length - 1

    # If we didn't find any repeated substring - even of length 1, return an empty string
    return ""


print(longest_repeated_substring("programming"))
print(longest_repeated_substring("independent"))
print(longest_repeated_substring("problem"))
