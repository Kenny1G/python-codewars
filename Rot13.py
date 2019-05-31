# ROT13 is a simple letter substitution cipher that replaces a letter with the letter
# 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should
# be returned as they are. Only letters from the latin/english alphabet should be
# shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    newList = []
    lowercase = [chr(i) for i in range(97,123)]
    uppercase = [chr(i) for i in range(65,91)]
    text = [l for l in message]
    for letter in text:
        if letter in lowercase:
            b = newIndex(letter,lowercase)
            print(b)
            newList.append(lowercase[b])
        elif letter in uppercase:
            b = newIndex(letter,uppercase)
            newList.append(uppercase[b])
        else:
            newList.append(letter)
    return ''.join(newList)

def newIndex(letter, list):
    p = list.index(letter)
    n = p + 13
    if n >= 26:
        b = n-26
    else:
        b = n
    return b


import unittest
class TestCipher(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rot13("test"),"grfg")
    def test_2(self):
        self.assertEqual(rot13("Test"),"Grfg")
    def test_3(self):
        self.assertEqual(rot13('n'),'a')
if __name__ == '__main__':
    unittest.main()
