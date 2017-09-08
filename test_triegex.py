from unittest import TestCase
import re

import triegex


class TriegexTest(TestCase):

    def findall(self, triegex, string):
        return re.findall(triegex.to_regex(), string)

    def test_basic(self):
        t = triegex.Triegex('Jon')
        self.assertListEqual(self.findall(t, 'Jon Snow'), ['Jon'])

    def test_empty_triegex_matches_nothing(self):
        t = triegex.Triegex()
        self.assertListEqual(self.findall(t, 'foo'), [], 'Should match nothing: {}'.format(t.to_regex()))

    def test_multiple_words(self):
        t = triegex.Triegex('Jon', 'Tyrion', 'Sam', 'Bran')
        self.assertListEqual(self.findall(t, 'Jon & Sam'), ['Jon', 'Sam'])

    def test_word_boundary_is_handled(self):
        t = triegex.Triegex('Sam')
        self.assertListEqual([], self.findall(t, 'Samwell'))
        self.assertListEqual(['Sam'], self.findall(t, 'Sam` Tarly'))

    def test_optimized(self):
        t = triegex.Triegex('Jon', 'Jorah')
        self.assertEqual(r'(?:Jo(?:n\b|rah\b)|~^(?#match nothing))', t.to_regex())


class TriegexMutableSetInterfaceTest(TestCase):
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

    def test_discart(self):
        t = triegex.Triegex()
        t.add('Hound')
        self.assertIn('Hound', t)
        t.discard('Hound')
        self.assertNotIn('Hound', t)
