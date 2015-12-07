#!/usr/bin/python
from math import log

width_mm = 2.5
length_mm = 71.5
distance_mm = 10

def mm_to_inches(mm):
    return mm * 0.0393701

def calc_L(width_in, distance_in, length_in):
    w = width_in
    b = length_in
    h = distance_in
    # formula from ARRL handbook. NB log is ln
    return 0.00508 * b * (log(2 * b / (w + h)) + 0.5 + 0.2235 * (w + h) / b)


print "Width {:f} mm".format(width_mm)
print "Length {:f} mm".format(length_mm)
print "Distance {:f} mm".format(distance_mm)

width_in = mm_to_inches(width_mm)
distance_in = mm_to_inches(distance_mm)
length_in = mm_to_inches(length_mm)
LuH = calc_L(width_in, distance_in, length_in)
if (LuH < 1):
    LnH = LuH * 1000.0;
    print "Inductance {:f} nH".format(LnH)
else:
    print "Inductance {:f} uH".format(LuH)
