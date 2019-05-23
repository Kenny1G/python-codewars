# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
#
# Python: return a list;
#
# for example, a tower of 3 floors looks like below
#
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
# and a tower of 6 floors looks like below
#
# [
#   '     *     ',
#   '    ***    ',
#   '   *****   ',
#   '  *******  ',
#   ' ********* ',
#   '***********'
# ]

def tower_builder(n):
    tower = []
    i = 0
    while(n>=1):
        last = (n*2)-1
        spaces = ' ' * i
        stars = '*' * last
        row = spaces + stars + spaces
        tower.insert(0,row)
        n -= 1
        i += 1
    return tower
#attempting my solution with a for loop
def tower_builder3(n):
    tower = []
    for i in range(0, n):
        last = (n*2)-1
        spaces = ' ' * i
        stars = '*' * last
        row = spaces + stars + spaces
        tower.insert(0, row)
        n -= 1
    return tower

#code wars best solution
def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

import unittest
class TowerTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tower_builder(1), ['*', ])
    def test_2(self):
        self.assertEqual(tower_builder(2), [' * ', '***'])
    def test_3(self):
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])
if __name__ == '__main__':
    unittest.main()
