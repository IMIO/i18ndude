# -*- coding: utf-8 -*-
import unittest

from i18ndude.utils import wrapString, MAX_WIDTH


class TestUtils(unittest.TestCase):

    def test_wrapString(self):
        # This all fits on one line.
        self.assertEqual(wrapString(''), [''])
        self.assertEqual(wrapString('a'), ['a'])
        self.assertEqual(wrapString('a b'), ['a b'])

        # This no longer fits.
        line = 'a'*20 + ' ' + 'b'*50 + ' ' + 'c'*20+ ' ' + 'd'*50
        self.assertEqual(wrapString(line),
                         ['',
                          'a'*20 + ' ' + 'b'*50 + ' ',
                          'c'*20+ ' ' + 'd'*50])

        # Look for the maximum that can fit on a single line.  This is
        # the maximum width, minus a starting and ending quote.
        max_one_line = MAX_WIDTH - 2
        line = 'a'*40 + ' ' + 'b'*36
        self.assertEqual(len(line), max_one_line)
        self.assertEqual(wrapString(line), [line])

        # With one extra character we must split.
        line += 'b'
        self.assertEqual(wrapString(line),
                         ['',
                          'a'*40 + ' ',
                          'b'*37])

        # So, what happens when some words are really too long?
        A = 'a'*99
        B = 'b'*99
        C = 'c'*99
        self.assertEqual(wrapString(A), ['', A])
        line = ' '.join((A, B))
        self.assertEqual(wrapString(line), ['', A + ' ', B])
        line = ' '.join((A, B, C))
        self.assertEqual(wrapString(line), ['', A + ' ', B + ' ', C])


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestUtils))
    return suite
