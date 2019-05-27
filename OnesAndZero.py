# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
#
# Examples:
#
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

def binary_array_to_number(arr):
    binary = ''.join([str(x) for x in arr])
    final = int(binary,2)
    return final


import unittest
class TestClass(unittest.TestCase):

    def test_1(self):
        self.assertEqual(binary_array_to_number([0,0,0,1]), 1)
    def test_2(self):
        self.assertEqual(binary_array_to_number([0,0,1,0]), 2)
    def test_3(self):
        self.assertEqual(binary_array_to_number([1,1,1,1]), 15)
    def test_4(self):
        self.assertEqual(binary_array_to_number([0,1,1,0]), 6)

if __name__ == '__main__':
    unittest.main()
