# Implement a method that accepts 3 integer values a, b, c. The method should
# return true if a triangle can be built with the sides of given length and false
# in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).
def is_triangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
import unittest
class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
    def test_2(self):
        self.assertEqual(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
    def test_3(self):
        self.assertEqual(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
    def test_4(self):
        self.assertEqual(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
    def test_5(self):
        self.assertEqual(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
    def test_6(self):
        self.assertEqual(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
    def test_7(self):
        self.assertEqual(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
    def test_8(self):
        self.assertEqual(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
    def test_9(self):
        self.assertEqual(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
    def test_10(self):
        self.assertEqual(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
    def test_11(self):
        self.assertEqual(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
    def test_12(self):
        self.assertEqual(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
    def test_13(self):
        self.assertEqual(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
    def test_14(self):
        self.assertEqual(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")


if __name__ == '__main__':
    unittest.main()
