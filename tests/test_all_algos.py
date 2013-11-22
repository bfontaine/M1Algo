# -*- coding: UTF-8 -*-

import types
import unittest
import algos

class TestAllAlgos(unittest.TestCase):
    def setUp(self):
        self.word = 'foo'
        def empty_gen(): yield from ()
        def one_gen(): yield self.word
        self.empty = empty_gen()
        self.one   = one_gen()
    pass

def generate_tests(algo_name, func):
    """
    Add tests for the specified algorithm implementation
    """
    def test_empty(self):
        res = func(self.empty, 42)
        self.assertEqual(list(res), [[]])

    def test_one_word(self):
        res = func(self.one, 42)
        self.assertEqual(list(res), [[self.word]])

    for attr, val in locals().items():
        if isinstance(val, types.FunctionType):
            name = attr + '_with_' + algo_name
            setattr(TestAllAlgos, name, val)

# Add all tests for each algorithm implementation
for (name, (func, _)) in algos.get_algos().items():
    generate_tests(name, func)
