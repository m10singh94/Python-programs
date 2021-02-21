import sys
import pytest
from Question_7 import smallest_greater_equal


def test_smallest_greater_numbers():
    message = "The smallest element of {} greater than {} is {}. Your function returned {}."

    true_tests = (((0, -1, -2, -3, 3, 4, 5, -6, -7, -8), -5, -3),
                  ((1.5, -21.9, 11.7, -101.14, 3.14159, 211.0), 3.15, 11.7),
                  ((-1, -1, -1, -1, -1, -1, -1, -1), -1, -1))

    for sequence, target, correct in true_tests:
        value = smallest_greater_equal(sequence, target)
        assert abs(value - correct) < 1e-6, message.format(sequence, target, correct, value)


def test_smallest_greater_strings():
    message = "The smallest element of \'{}\' greater than \'{}\' is \'{}\'. Your function returned \'{}\'."

    true_tests = (("Hello World", "a", "d"),
                  ("AbCdEfGhIjKlMnOpQrStUvWxYz", "H", "I"),
                  ("The quick brown fox jumped over the lazy dog", "A", "T"))

    for sequence, target, correct in true_tests:
        value = smallest_greater_equal(sequence, target)
        assert value == correct, message.format(sequence, target, correct, value)


if __name__ == '__main__':
    pytest.main(sys.argv)
