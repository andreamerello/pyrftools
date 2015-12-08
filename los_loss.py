#!/usr/bin/python
import math, sys
from measure import parse_length, parse_freq

def loss(wlen, dist):
    k = math.pi * 4
    tmp = k * dist / wlen
    return 20 * math.log10(tmp)

def freq_to_wlen(freq):
    return light_speed / freq

if (len(sys.argv) != 3):
    print "Usage:\n{} <freq> <distance>".format(sys.argv[0])
else:

    dist_in, dist_m = parse_length(sys.argv[2])
    freq_hz, wlen_in, wlen_m = parse_freq(sys.argv[1])
    atten = loss(wlen_m, dist_m)
    print "atten: {:f} dB\n".format(atten)
