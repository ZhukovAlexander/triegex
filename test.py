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
        self.assertListEqual(self.findall(t, 'foo'), [], 'Should match nothing: {}'.format(t.render()))

    def test_multiple_words(self):
        # t = triegex.Triegex('Jon', 'Tyrion', 'Sam', 'Bran')
        t = triegex.Triegex('Jon', 'Sam')
        self.assertListEqual(self.findall(t, 'Jon & Sam'), ['Jon', 'Sam'])

    def test_word_boundary_is_handled(self):
        t = triegex.Triegex('TyrionLannister')
        self.assertListEqual(self.findall(t, 'Tyrion'), [])
        self.assertListEqual(self.findall(t, 'Lannister'), [])
        self.assertListEqual(self.findall(t, 'TyrionLannister'), ['TyrionLannister'])

    def test_iter(self):
        self.assertListEqual(list(triegex.Triegex('foo')), ['foo'])

    def test_contains(self):
        self.assertIn('Jaime', triegex.Triegex('Jaime', 'Lannister'))
        self.assertNotIn('Stannis', triegex.Triegex('Kings Landing'))

    def test_len(self):
        t = triegex.Triegex()
        self.assertEqual(len(t), 0)
        t.add('Sansa')
        self.assertEqual(len(t), 1)

    def test_optimized(self):
        t = triegex.Triegex('Jon', 'Jorah')
        self.assertEqual('(?:Jo(?:n|rah)|z^(?#match nothing))', t.render())
