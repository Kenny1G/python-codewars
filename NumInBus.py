# Number of people in the bus
# There is a bus moving in the city, and it takes and drop some
# people in each bus stop.
#
# You are provided with a list (or array) of integer arrays
# (or tuples). Each integer array has two items which represent
# number of people get into bus (The first item) and number of people
# get off the bus (The second item) in a bus stop.
#
# Your task is to return number of people who are still in the bus
# after the last bus station (after the last array). Even though it
# is the last bus stop, the bus is not empty and some people are
# still in the bus, and they are probably sleeping there :D
#
# Take a look on the test cases.
#
# Please keep in mind that the test cases ensure that the number of
# people in the bus is always >= 0. So the return integer can't be
# negative.
#
# The second value in the first integer array is 0, since the bus
# is empty in the first bus stop.

import operator
from functools import reduce
def number(bus_stops):
    #list of people entering the bus
    listEntered = []
    # list of people leaving the bus
    listLeft = []
    for arr in bus_stops:
        listEntered.append(arr[0])
        listLeft.append(arr[1])
    totalEntered = reduce(operator.add, listEntered)
    totalLeft = reduce(operator.add, listLeft)

    return totalEntered - totalLeft
#best answer on codewars
def number2(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)
    
import unittest
class TestKata(unittest.TestCase):
    def test_1(self):
        self.assertEqual(number2([[10,0],[3,5],[5,8]]),5)
    def test_2(self):
        self.assertEqual(number2([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
    def test_3(self):
        self.assertEqual(number2([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)

if __name__ == '__main__':
    unittest.main()
