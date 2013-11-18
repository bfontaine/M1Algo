# -*- coding: UTF-8 -*-

import unittest
import algos.base as b

class TestAlgosBase(unittest.TestCase):

    def setUp(self):
        b.ALGOS = {}
        def f():
            pass
        self.fun = f

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

    def test_get_algo(self):
        doc = 'foo'
        b.register(self.fun, doc)
        self.assertEqual(b.get_algos()['f'][1], doc)

