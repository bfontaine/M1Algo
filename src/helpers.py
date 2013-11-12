# -*- coding: UTF-8 -*-

import argparse as ap
from argparse import RawTextHelpFormatter
from sys import exit, stdin, stdout, stderr

def printerr(*args, **kwargs):
    """
    Print on stderr
    """
    kwargs['file'] = stderr
    print(*args, **kwargs)

def read_args(algs):
    """
    Read command-line arguments and return the output width (default: 79),
    the name of the algorithm, and a possibly empty namespace representing
    the additional flags from the command-line. For example, if '--foo' is
    a valid argument and is given on the command-line, flags.foo will be
    True.
    """
    ep  = '----\nOne line of input is read on stdin and the output is '
    ep += 'written on stdout.\n\n' + get_algos_str(algs)
    parser = ap.ArgumentParser(
            #description='A text wrapper',
            epilog=ep,
            formatter_class=RawTextHelpFormatter)
    parser.add_argument('--algo', help='The algorithm to use')
    parser.add_argument('-w', '--width',
            default=79, help='Set the output line width', type=int)
    parser.add_argument('--info', metavar='ALGO',
            help='Get some info about an algorithm')
    args = parser.parse_args()

    if not args.algo and not args.info:
        printerr('You must give an algorithm on the command-line!')
        parser.print_help(file=stderr)
        exit(1)

    if args.algo:
        args.algo = args.algo.lower()

    return (args.width, args.algo, args)

def get_algos_str(algs):
    """
    Return a string describing the algorithms dict passed as an argument
    """
    ls = [ [k, v[1]] for k,v in algs.items() ]
    ls.sort(key=lambda x: x[0])

    max_width = max([len(x[0]) for x in ls])
    fmt = "%-" + str(max_width) + "s -- %s"

    s = "Available algorithms:\n"
    return s + "\n".join([fmt % tuple(a) for a in ls])

def print_algos(algs, file=stdout):
    """
    Print a dict of algorithms
    """
    print(get_algos_str(algs), file=file)

def unknown_algo_error(alg, algs):
    """
    Print an error message for an unknown algorithm, show the list of
    available algorithms and exit.
    """
    printerr("Unknown algorithm '%s'." % alg)
    print_algos(algs, file=stderr)
