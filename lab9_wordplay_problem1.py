
## Lab 9, programming problem "wordplay".
## This is a solution to the first question of that problem only.
## You can use this as a starting point to solve the other questions.

## Remember that you need to download the text file with the list
## of words to be able to run this code.


def count_word_lengths(wordlist):
    '''
    wordlist is a list of strings (assumed to be words). Returns
    a dictionary mapping word lengths (integers) to the number of
    words of that length. For example,
    
    lengths = count_word_lengths(my_word_list)
    print("there are", lengths[3], "words of length 3 in the list")

    Note that the dictionary will only contain as keys lengths such
    that there is at least one word of that length. For example,

    lengths[1000]

    will result in a KeyError, because there is no word of 1000 letters
    in the list.
    '''
    # create an empty dictionary
    counts = dict()
    for word in wordlist:
        l = len(word)
        # if l is already in the dictionary, increase the count:
        if l in counts:
            counts[l] = counts[l] + 1
        else:
            # otherwise, it's the first time we see l, so set count to 1
            counts[l] = 1
    return counts

if __name__ == '__main__':

    # Load the wordlist into a list:
    with open("wordlist.txt") as wordfile:
        # use strip to get rid of the newline at the end of each line
        my_word_list = [ line.strip() for line in wordfile ]

    # Count!
    counts = count_word_lengths(my_word_list)

    # How many different word lengths did we find?
    # Taking len() of a dictionary returns the number of keys it has:
    print("There are", len(counts), "different word lengths")

    # Question: What are the 10 most frequent word lengths?

    # To answer this, we need to sort the (length, count) pairs by count.
    # First, make a list:
    list_of_pairs = []
    # iterate over the keys in the dictionary (which are different word lengths):
    for length in counts.keys():
        # for each length, add to the list a pair (count, length)
        list_of_pairs.append((counts[length], length))

    # Note: instead of the loop above, we could also use a list
    # comprehension to create the same list:
    # list_of_pairs = [ (counts[length], length) for length in counts.keys() ]

    # Why did put the count first and the length second in every pair?
    # Because when we sort a list of tuples (or a list of lists), the
    # default sorting comparison is lexicographic, meaning that the tuples
    # are compared on their first element first (on the second only if the
    # first are equal, and so on). So by putting the count first in each
    # pair, we get the list sorted by count.
    # The default sort order is increasing, but we want it to be decreasing
    # (so that we have the biggest counts first); we can do this by passing
    # the optional argument reverse = True to the sort method.
    list_of_pairs.sort(reverse = True)

    # Now, we just have to print the 10 first pairs in the list:
    print("The 10 most common word lengths:")
    for pair in list_of_pairs[:10]:
        length = pair[1]
        count_for_that_length = pair[0]
        print("There are",count_for_that_length,"words of length",length)


    # Bonus Question: What are the 10 LEAST frequent word lengths?

    # To answer this, we just have to print the 10 last pairs in the list:
    print("The 10 least common word lengths:")
    for pair in list_of_pairs[-10:]:
        length = pair[1]
        count_for_that_length = pair[0]
        print("There are",count_for_that_length,"words of length",length)


    # Bonus Question: What is the smallest word length that does not appear
    # in the list?

    # To answer this question, we can simply start counting up from 1 and
    # stop when we reach a number that is not a key in the dictionary:
    length = 1
    # How do we know this loop will terminate?
    while length in counts:
        length = length + 1
    print("There is no word of length", length, "in the list!")
