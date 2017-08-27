from unittest import TestCase
import re

import triegex


class TriegexTest(TestCase):

    def findall(self, triegex, string):
        return re.findall(triegex.render(), string)

    def test_basic(self):
        t = triegex.Triegex('Jon')
        self.assertListEqual(self.findall(t, 'Jon Snow'), ['Jon'])

    def test_empty_triegex_matches_nothing(self):
        t = triegex.Triegex()
        self.assertListEqual(self.findall(t, 'foo'), [], 'Should match nothing')

    def test_multiple_words(self):
        t = triegex.Triegex('Jon', 'Tyrion', 'Sam', 'Bran')
        self.assertListEqual(self.findall(t, 'Jon & Sam'), ['Jon', 'Sam'])

    def test_word_boundary_is_handled(self):
        t = triegex.Triegex('TyrionLannister')
        self.assertListEqual(self.findall(t, 'Tyrion'), [])
        self.assertListEqual(self.findall(t, 'Lannister'), [])
        self.assertListEqual(self.findall(t, 'TyrionLannister'), ['TyrionLannister'])
