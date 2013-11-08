# -*- coding: UTF-8 -*-

from sys import argv, exit, stdin, stderr

def read_args():
    """
    Read command-line arguments and return the output width (default: 79),
    the name of the algorithm (default: None), and a possibly empty dict
    representing the additional flags from the command-line. For example,
    if '--foo' is passed as an argument, flags['foo'] will be True.
    """
    algo  = None
    width = 79
    wflag = False
    args  = argv[1:]
    flags = {}
    for a in argv[1:]:
        if wflag:
            width = int(a)
            wflag = False
        elif a == '-w':
            wflag = True
        elif a.startswith('--algo='):
            algo = a[7:]
        elif a.startswith('--'):
            flags[a[2:]] = True

    return (width, algo, flags)

def debug(s):
    """
    Print a debugging message
    """
    print("[DEBUG] %s" % s, file=stderr)

def print_usage():
    """
    Print the executable usage
    """
    print("""Usage:\n\t%s --algo=<algo> [-w <width>]
  The input is read on STDIN and the output is written on STDOUT.""" % argv[0])

def print_algos(algs):
    """
    Print a dict of algorithms
    """
    ls = [ [k, v[1]] for k,v in algs.items() ]
    ls.sort(key=lambda x: x[0])

    max_width = max([len(x[0]) for x in ls])
    fmt = "%-" + str(max_width) + "s -- %s"

    for algo,shortdoc in ls:
        print(fmt % (algo, shortdoc))
