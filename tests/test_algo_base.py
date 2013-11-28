# -*- coding: UTF-8 -*-

import unittest
import algos.base as b

class TestAlgosBase(unittest.TestCase):

    def setUp(self):
        b.ALGOS = {}
        def f():
            pass
        self.fun = f
        self.l = ['foo', 'bar']

    # - register - #

    def test_register(self):
        self.assertEqual(len(b.ALGOS.keys()), 0)
        b.register(self.fun, "foo")
        self.assertEqual(len(b.ALGOS.keys()), 1)

    def test_register_name(self):
        b.register(self.fun, "foo")
        k = list(b.ALGOS.keys())[0]
        self.assertEqual(k, 'f')

    def test_register_val(self):
        doc = 'foo'
        b.register(self.fun, doc)
        self.assertEqual(b.ALGOS['f'][1], doc)

    # - get_algos - #

    def test_get_algo(self):
        doc = 'foo'
        b.register(self.fun, doc)
        self.assertEqual(b.get_algos()['f'][1], doc)

    # - simple_line_justifying - #

    def test_sljustify_empty_line(self):
        self.assertEqual(b.simple_line_justifying([],  0), [])
        self.assertEqual(b.simple_line_justifying([], 42), [])

    def test_sljustify_negative_width(self):
        self.assertEqual(b.simple_line_justifying(self.l, -42), self.l)

    def test_sljustify_no_width(self):
        self.assertEqual(b.simple_line_justifying(self.l, 0), self.l)

    def test_sljustify_too_small_width(self):
        self.assertEqual(b.simple_line_justifying(self.l, 1), self.l)
        self.assertEqual(b.simple_line_justifying(self.l, 6), self.l)

    def test_sljustify_exact_width(self):
        self.assertEqual(b.simple_line_justifying(self.l, 7), self.l)

    def test_sljustify_one_word(self):
        l = ['foo']
        self.assertEqual(b.simple_line_justifying(l, 20), l)

    def test_sljustify_one_more_space(self):
        l = self.l
        l[0] += ' '
        self.assertEqual(b.simple_line_justifying(self.l, 8), l)

    def test_sljustify_one_space_per_word(self):
        l = self.l
        l[0] += '  '
        self.assertEqual(b.simple_line_justifying(self.l, 9), l)

    def test_sljustify(self):
        l1 = ['foo', 'x', 'bar', 'zzzz']
        l2 = [l1[0] + '  ', l1[1] + '  ', l1[2] + ' ', l1[3]]
        self.assertEqual(b.simple_line_justifying(l1, 19), l2)

    # - justify - #
    def test_justify_empty_no_width(self):
        res = list(b.justify([[]], 0))
        self.assertEqual(res, [[]])

    def test_justify_empty(self):
        res = list(b.justify([[]], 100))
        self.assertEqual(res, [[]])

    def test_justify_two_empty_lines(self):
        res = list(b.justify([[], []], 100))
        self.assertEqual(res, [[], []])

    def test_justify_one_word_per_line(self):
        res = list(b.justify([['foo'], ['bar']], 8))
        self.assertEqual(res, [['foo'], ['bar']])

    def test_justify(self):
        res = list(b.justify([['foo', 'bar'], ['a', 'b', 'c']], 8))
        self.assertEqual(res, [['foo ', 'bar'], ['a  ', 'b ', 'c']])

    # - linelen - #

    def test_linelen_empty(self):
        self.assertEqual(b.linelen([]), 0)

    def test_linelen_one_word(self):
        w = 'foo'
        self.assertEqual(b.linelen([w]), len(w))

    def test_linelen_two_words(self):
        w1 = 'foo'
        w2 = 'bar'
        l  = len(w1 + ' ' + w2)
        self.assertEqual(b.linelen([w1, w2]), l)

    def test_linelen(self):
        line = 'foo bar zzzzzzzz qq s s rstuv wx'
        words = line.split(' ')
        self.assertEqual(b.linelen(words), len(line))
