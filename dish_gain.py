#!/usr/bin/python
import math, sys
from measure import parse_length, parse_freq

#for 50% efficency
k = 0.5

def dish_gain(wlen, diam):
    tmp = math.pi * diam / wlen
    return 10 * math.log10(tmp * tmp * k)

if (len(sys.argv) != 3):
    print "Usage:\n{} <freq> <diam>".format(sys.argv[0])
else:
    freq, wlen_in, wlen_m = parse_freq(sys.argv[1], 'frequency')
    diam_in, diam_m = parse_length(sys.argv[2], 'diameter')

    gain = dish_gain(wlen_m, diam_m)
    print "gain: {:f} dB (assuming 50% efficency)\n".format(gain)
