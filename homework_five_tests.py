import sys
import pytest
from interpolate import interpolate


def test_interpolate():
    tests = (
        (((1, 3, 5), (1, 9, 25), 2), 5.0,
         'closest values: x[0] == 1 < 2.0 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 5.0'),
        (((1, 3, 5), (1, 9, 25), 4), 17.0,
         'closest values: x[1] == 3 < 4.0 < x[2] == 5; y[1] == 9 and y[2] == 25; a = 8.0, b = -15.0, answer = 17.0'),
        (((1, 3, 5), (1, 9, 25), 1.25), 2.0,
         'closest values: x[0] == 1 < 1.25 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 2.0'),
        (((1, 3, 5), (1, 9, 25), 1.5), 3.0,
         'closest values: x[0] == 1 < 1.5 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 3.0'),
        (((1, 3, 5), (1, 9, 25), 1.75), 4.0,
         'closest values: x[0] == 1 < 1.75 < x[1] == 3; y[0] == 1 and y[1] == 9; a = 4.0, b = -3.0, answer = 4.0'),
    )

    for (x, y, target), correct, message in tests:
        result = interpolate(x, y, target)
        assert abs(result - correct) < 1e-6, message

if __name__ == '__main__':
    pytest.main(sys.argv)
