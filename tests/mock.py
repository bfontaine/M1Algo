# -*- coding: UTF-8 -*-

import sys
from io import StringIO

class FakePrinter():
    """
    This class is intended to use to mock Python3's 'print'. Typical workflow:
        fp = FakePrinter()
        fp.enable()
        print("foo")
        s = fp.getvalue() # "foo"
        fp.disable()
    """

    def enable(self):
        """
        Enable the mock, printed output will be available through .getvalue
        """
        self.out = StringIO()
        self._stdout = sys.stdout
        sys.stdout = self.out

    def getvalue(self):
        """
        Return the printed output so far
        """
        return self.out.getvalue()

    def disable(self):
        """
        Disable the mock. If .getvalue is called after this function,
        it'll raise an error.
        """
        self.out.close()
        sys.stdout = self._stdout

    def __del__(self):
        self.disable()
