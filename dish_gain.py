#!/usr/bin/python
import math, sys

light_speed = float(299792458)
#for 50% efficency
k = 0.5

def dish_gain(wlen, diam):
    tmp = math.pi * diam / wlen
    return 10 * math.log10(tmp * tmp * k)

def freq_to_wlen(freq):
    return light_speed / freq / 1000.0

if (len(sys.argv) != 3):
    print "Usage:\n{} <freq_Hz> <diam_meters>".format(sys.argv[0])
else:
    freq = float(sys.argv[1])
    diam = float(sys.argv[2])
    wlen = freq_to_wlen(freq)

    gain = dish_gain(wlen, diam)
    print "gain: {:f} dB (assuming 50% efficency)\n".format(gain)
