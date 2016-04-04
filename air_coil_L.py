#!/usr/bin/python
import sys
from math import log
from measure import parse_length

def calc_L(diam_in, len_in, turns):
    d = diam_in
    n = turns
    l = len_in
    return (d*d * n*n) / (18 * d + 40 * l)

if (len(sys.argv) != 4):
    print "Usage:\n{} <diam> <len> <turns>".format(sys.argv[0])
else:

    diam_in, diam_m = parse_length(sys.argv[1], 'diam')
    len_in, len_m = parse_length(sys.argv[2], 'len')
    turns = int(sys.argv[3])

    print "Diam: {:f} m, ({:f} in)".format(diam_m, diam_in)
    print "Length: {:f} m, ({:f} in)".format(len_m, len_in)
    print "Turns: {:d}".format(turns)

    LuH = calc_L(diam_in, len_in, turns)

    if (LuH < 1):
        LnH = LuH * 1000.0;
        print "Inductance {:f} nH".format(LnH)
    else:
        print "Inductance {:f} uH".format(LuH)
