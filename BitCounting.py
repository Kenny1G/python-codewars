# Write a function that takes an integer as input,
# and returns the number of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def base10ToBase2(n):
    arrayOfRemainders = []
    while n > 0:
        arrayOfRemainders.append(n%2)
        n = int(n/2)
    arrayOfRemainders.reverse()
    return arrayOfRemainders

def countBits(n):
    base2 = base10ToBase2(n)
    finale = 0
    for i in base2:
        if i == 1:
            finale += 1
    print(finale)
    return finale


import unittest


class TestKata(unittest.TestCase):
    def test_1(self):
        self.assertEqual(countBits(0), 0);
    def test_2(self):
        self.assertEqual(countBits(4), 1);
    def test_3(self):
        self.assertEqual(countBits(7), 3);
    def test_4(self):
        self.assertEqual(countBits(9), 2);
    def test_5(self):
        self.assertEqual(countBits(10), 2);

        
if __name__ == '__main__':
    unittest.main()
