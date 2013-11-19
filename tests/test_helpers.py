# -*- coding: UTF-8 -*-

import unittest
import helpers as h

class TestHelpers(unittest.TestCase):

    def setUp(self):
        def f():
            pass
        self.base = 'Available algorithms:\n'
        self.f = f


    def test_algos_str_empty(self):
        self.assertEqual(h.get_algos_str({}), self.base)

    def test_algos_str_one(self):
        algs = {
            'foo': [self.f, 'oof']
        }
        s = h.get_algos_str(algs)
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
