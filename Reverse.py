def reverse_words(text):
    newWords = []
    words = text.split(' ')
    for word in words:
        letters = [char for char in word]
        letters.reverse()
        newWords.append(''.join(letters))
    return ' '.join(newWords)


# codewar best solution
def reverse_words2(text):
    return ' '.join(s[::-1] for s in str.split(' '))


import unittest


class TestReverse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')

    def test_2(self):
        self.assertEqual(reverse_words('apple'), 'elppa')

    def test_3(self):
        self.assertEqual(reverse_words('a b c d'), 'a b c d')

    def test_4(self):
        self.assertEqual(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')


if __name__ == '__main__':
    unittest.main()
