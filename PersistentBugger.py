# Write a function, persistence, that takes in a positive parameter num and returns
# its multiplicative persistence, which is the number of times you must multiply
# the digits in num until you reach a single digit.
from functools import reduce
import operator


def persistence(n):
    # Recursive method could not be tested.
    # y = 1
    # list = [int(x) for x in str(n)]
    # if (len(list) == 1):
    #     return counter
    # else:
    #     for i in list:
    #         y *= i
    #     counter += 1
    #     persistence(y, counter)
    list = [int(x) for x in str(n)]
    counter = 0
    while (len(list) != 1):
        y = 1
        for i in list:
            y *= i
        counter += 1
        list = [int(x) for x in str(y)]
    return counter


# With reduce
def persistence2(n):
    list = [int(x) for x in str(n)]
    counter = 0
    while (len(list) != 1):
        # reduce makes the multiplying of list process easier :)
        v = reduce(operator.mul, list)
        counter += 1
        list = [int(x) for x in str(v)]
    return counter


import unittest


class TestPersistence(unittest.TestCase):

    def test_1(self):
        self.assertEqual(persistence2(39), 3)

    def test_2(self):
        self.assertEqual(persistence2(4), 0)

    def test_3(self):
        self.assertEqual(persistence2(25), 2)

    def test_4(self):
        self.assertEqual(persistence2(999), 4)


if __name__ == '__main__':
    unittest.main()
