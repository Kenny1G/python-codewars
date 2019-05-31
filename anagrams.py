# What is an anagram? Well, two words are anagrams of each other if they both
# contain the same letters. For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words. You should return
# an array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    wordList = [a for a in word]
    wordList.sort()
    finalList = []
    for new_word in words:
        new_word_list = [l for l in new_word]
        new_word_list.sort()
        if wordList == new_word_list:
            finalList.append(new_word)
    return finalList

#codewars best answer:
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]

import unittest
class TestAnagram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    def test_2(self):
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

if __name__ == '__main__':
    unittest.main()
