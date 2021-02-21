import sys
import pytest
from max_relative_frequency import max_relative_frequency


message = "the most frequent letter(s) in the string \'{}\' is/are {}, which occur(s) {} times (each); the total number of letters is {}."


def test_basic():

    cases = (
        ('''sufficit''', 0.25, ['f', 'i'], 2, 8),
        ('''mississippi''', 0.36363, ['i', 's'], 4, 11),
        ('''nullius in verba''', 0.14286, ['i', 'l', 'n', 'u'], 2, 14),
        ('''quantum sufficit''', 0.20000, ['u'], 3, 15),
        ('''semper ad meliora''', 0.20000, ['e'], 3, 15),
        ('''si tacuisses philosophus mansisses''', 0.32258, ['s'], 10, 31),
        ('''quam bene non quantum''', 0.22222, ['n'], 4, 18),
        ('''pecunia si uti scis ancilla est si nescis domina''', 0.20000, ['i'], 8, 40)
    )
    
    for s, f, letters, c, length in cases:
        assert abs(max_relative_frequency(s) - f) < 0.00001, message.format(s, letters, c, length)


def test_case():

    cases = (
        ('''Nullius In Verba''', 0.14286, ['i', 'l', 'n', 'u'], 2, 14),
        ('''qUaNtuM sUffiCit''', 0.20000, ['u'], 3, 15),
        ('''semper ad MELIORA''', 0.20000, ['e'], 3, 15),
        ('''si TACUISSES philoSOPHUS Mansisses''', 0.32258, ['s'], 10, 31),
        ('''quam BENE NON QUANTUM''', 0.22222, ['n'], 4, 18)
    )

    for s, f, letters, c, length in cases:
        assert abs(max_relative_frequency(s) - f) < 0.00001, message.format(s, letters, c, length)


def test_punctuation():
    cases = (
        ('''pecunia, si uti scis, ancilla est; si nescis, domina''', 0.20000, ['i'], 8, 40),
        ('''In fact, it is difficult to construct a solitary thought
without using that most common symbol. It is slow going at first, but
with caution and hours of training you can gradually gain facility.''', 0.14013, ['t'], 22, 157),
        ('''Preheat oven to 350 degrees F (175 degrees C). Grease a 9x9 inch baking pan.''', 0.22000, ['e'], 11, 50),
        ('''42 minutes and 42 seconds?''', 0.17647, ['n', 's'], 3, 17),
        ('''void splurf { i++;
  if ([i % 5] = 5) { splurf(); }''', 0.20000, ['i'], 4, 20),
        ('''53mper ad m3l10ra''', 0.20000, ['a', 'm', 'r'], 2, 10),
        ('''qu4m b3n3 n0n quan7um''', 0.30769, ['n'], 4, 13),
        ('''si tacui55es ph1los0phus m4nsi55es''', 0.25000, ['s'], 6, 24),
        ('''1437746094.5735958''', 0.00000, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 0, 0),
        ('''mea navis aëricumbens anguillis abundat''', 0.17647, ['a'], 6, 34)
        )

    for s, f, letters, c, length in cases:
        assert abs(max_relative_frequency(s) - f) < 0.00001, message.format(s, letters, c, length)


if __name__ == '__main__':
    pytest.main(sys.argv)

