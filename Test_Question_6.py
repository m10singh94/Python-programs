import sys
import pytest
from Question_6 import is_leap_year


def test_is_leap_year_simple():
    message = "{} is{} a leap year. Your function returned {}."

    true_tests = (4, 12, -24, -196, 2016, -2124, 21124)

    for year in true_tests:
        assert is_leap_year(year), message.format(year, "", is_leap_year(year))

    false_tests = (1, -1, 11, 2011, 2019, 21117, 2, 22, 1982, 2022, -21114)

    for year in false_tests:
        assert not is_leap_year(year), message.format(a, " not", is_leap_year(year))


def test_is_leap_year_hundred():
    message = "{} is not a leap year. Your function returned {}."
    false_tests = (-1500, -1100, -200, -100, 100, 1300, 2100, 21100)
    for year in false_tests:
        assert not is_leap_year(year), message.format(year, is_leap_year(year))


def test_is_leap_year_full():
    message = "{} is a leap year. Your function returned {}."
    true_tests = (-400, 0, 400, -12000, 1200, 1600, 2400, 22800)
    for year in true_tests:
        assert is_leap_year(year), message.format(year, is_leap_year(year))


def test_is_leap_year_return_type():
    message = "The return value of 'is_leap_year' must be type <class 'bool'>," +\
              "your function returned a value of type {}."
    for a in range(-1000, 1000, 23):
        result = type(is_leap_year(a))
        assert result == bool, message.format(result)


if __name__ == '__main__':
    pytest.main(sys.argv)
