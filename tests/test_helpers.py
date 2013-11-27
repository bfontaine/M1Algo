# -*- coding: UTF-8 -*-

import unittest
import sys
from mock import FakePrinter
import helpers as h

class TestHelpers(unittest.TestCase):

    def setUp(self):
        def f():
            "doc"
            pass

        def g(): pass
        self.f = f
        self.g = g
        self.base = 'Available algorithms:\n'
        self.fp = FakePrinter()
        self.fp.enable()
        self.algs1 = {
            'foo': [self.f, 'oof']
        }

    def tearDown(self):
        self.fp.disable()

    # - print_algo_info - #

    def test_print_algo_info(self):
        h.print_algo_info('f', self.f, 'foo')
        s = self.fp.getvalue()
        self.assertEqual(s, 'F: foo\ndoc\n')

    def test_print_algo_info_nodoc(self):
        h.print_algo_info('g', self.g, 'foo')
        s = self.fp.getvalue()
        self.assertEqual(s, 'G: foo\n')

    def test_print_algo_underscores(self):
        h.print_algo_info('a_b_c', self.f, 'foo')
        s = self.fp.getvalue()
        self.assertEqual(s, 'A B C: foo\ndoc\n')

    def test_print_algo_titleize(self):
        h.print_algo_info('abc_def', self.f, 'foo')
        s = self.fp.getvalue()
        self.assertEqual(s, 'Abc Def: foo\ndoc\n')

    # - str2algo - #

    def test_str2algo_empty(self):
        self.assertEqual(h.str2algo(''), '')

    def test_str2algo_one_word(self):
        w = 'foobarlongword'
        self.assertEqual(h.str2algo(w), w)

    def test_str2algo_hyphens(self):
        w1 = 'a-b-c'
        w2 = 'a_b_c'
        self.assertEqual(h.str2algo(w1), w2)

    def test_str2algo_spaces(self):
        w1 = 'a b c'
        w2 = 'a_b_c'
        self.assertEqual(h.str2algo(w1), w2)

    def test_str2algo_spaces_and_hyphens(self):
        w1 = 'a b-c d'
        w2 = 'a_b_c_d'
        self.assertEqual(h.str2algo(w1), w2)

    # - algo2str - #

    def test_algo2str_empty(self):
        self.assertEqual(h.algo2str(''), '')

    def test_algo2str_one_word(self):
        w = 'foobarlongword'
        self.assertEqual(h.algo2str(w), w)

    def test_algo2str_only_one_underscore(self):
        self.assertEqual(h.algo2str('_'), '-')

    def test_algo2str_underscores(self):
        w1 = 'a_b_c'
        w2 = 'a-b-c'
        self.assertEqual(h.algo2str(w1), w2)

    def test_algo2str_two_underscores(self):
        w1 = 'a__c'
        w2 = 'a--c'
        self.assertEqual(h.algo2str(w1), w2)

    # - get_algos_str - #

    def test_algos_str_empty(self):
        self.assertEqual(h.get_algos_str({}), self.base)

    def test_algos_str_one(self):
        s = h.get_algos_str(self.algs1)
        self.assertEqual(s, self.base + 'foo -- oof')

    def test_algos_str(self):
        algs = {
            'foo': [self.f, 'oof'],
            'z': [self.f, 'zz'],
            'longname': [self.f, 'a']
        }
        s = h.get_algos_str(algs)
        expected = self.base + '\n'.join([
            'foo      -- oof',
            'longname -- a',
            'z        -- zz'
        ])
        self.assertEqual(s, expected)

    # - print_algos - #
    def test_print_algos(self):
        h.print_algos(self.algs1, file=sys.stdout)
        self.assertEqual(self.fp.getvalue(), self.base + 'foo -- oof\n')

