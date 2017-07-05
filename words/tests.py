""" tests for the word function """
import unittest
from words import words

class Test(unittest.TestCase):
    """tests for the word function """
    def test_word_occurance1(self):
        """should count one word"""
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )

    def test_word_occurance2(self):
        """test should count one of each"""
        self.assertDictEqual(
            {'one': 1, 'of': 1, 'each': 1},
            words("one of each"),
            msg='should count one of each'
        )

    def test_word_occurance3(self):
        """test should count multiple occurrences"""
        self.assertDictEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            words("one fish two fish red fish blue fish"),
            msg='should count multiple occurrences'
        )

    def test_word_occurance4(self):
        """ test should include punctuation """
        self.assertDictEqual(
            {'car': 1,
             ":": 2,
             'carpet': 1,
             'as': 1,
             'java': 1,
             'javascript!!&@$%^&': 1
            },
            words('car : carpet as java : javascript!!&@$%^&'),
            msg='should include punctuation'
        )

    def test_word_occurance5(self):
        """test should include numbers"""
        self.assertDictEqual(
            {'testing': 2, 1: 1, 2: 1},
            words('testing 1 2 testing'),
            msg='should include numbers'
        )

    def test_word_occurance6(self):
        """ test should respect case"""
        self.assertDictEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            words('go Go GO'),
            msg='should respect case'
        )
    def test_word_occurance8(self):
        """test should not count multilines"""
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\nworld'),
            msg='should not count multilines'
        )

    def test_word_occurance9(self):
        """ test not to count tabs"""
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\tworld'),
            msg='should not count tabs'
        )

    def test_word_occurance0(self):
        """ test count multiple spaces as one"""
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello  world'),
            msg='should count multiple spaces as one'
        )
unittest.main()
