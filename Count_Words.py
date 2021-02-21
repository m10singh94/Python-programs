import string


def count_word_frequencies(file_name):
    """
    Counts the words in the given file - is case insensitive and will skip words that
    are only punctuation characters. Assumes each word is separated by a space or newline character.
    :param file_name: the file name (or file path) of the file to examine
    :return: dict - keys are words, values are the frequency of that word in the given file.
    """

    text_file = open(file_name, mode="r")

    frequency_dictionary = dict()

    for line in text_file:
        line = line.strip()
        split_line = line.split(" ")

        for word in split_line:
            word = word.lower()  # Convert everything to lower case
            word = word.strip(string.punctuation)  # Remove punctuation from beginning and end

            # If a word only consists of punctuation we should skip it.
            if not word:
                continue

            if word not in frequency_dictionary:
                frequency_dictionary[word] = 1
            else:
                frequency_dictionary[word] = frequency_dictionary[word] + 1

    text_file.close()
    return frequency_dictionary


word_frequencies = count_word_frequencies("Gettysburg_Address.txt")

sorted_frequencies = []

# Put the words in a list, but with frequency first, word second
for key, val in word_frequencies.items():
    sorted_frequencies.append((val, key))

sorted_frequencies.sort(reverse=True)

# Now print them back out, but word first, frequency second
for freq, word in sorted_frequencies:
    print("{} = {}".format(word, freq))
