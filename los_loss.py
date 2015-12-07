#!/usr/bin/python
import math, sys

light_speed = float(299792458)

def loss(wlen, dist):
    k = math.pi * 4
    tmp = k * dist / wlen
    return 20 * math.log10(tmp)

def freq_to_wlen(freq):
    return light_speed / freq

if (len(sys.argv) != 3):
    print "Usage:\n{} <freq_Hz> <distance_meters>".format(sys.argv[0])
else:
    freq = float(sys.argv[1])
    dist = float(sys.argv[2])
    wlen = freq_to_wlen(freq)
    atten = loss(wlen, dist)
    print "atten: -{:f} dB\n".format(atten)
