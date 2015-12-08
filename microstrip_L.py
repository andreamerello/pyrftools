#!/usr/bin/python
from math import log
from measure import parse_length

width_str = "2.5mm"
length_str = "71.5mm"
distance_str = "10mm"

def calc_L(width_in, distance_in, length_in):
    w = width_in
    b = length_in
    h = distance_in
    # formula from ARRL handbook. NB log is ln
    return 0.00508 * b * (log(2 * b / (w + h)) + 0.5 + 0.2235 * (w + h) / b)

width_in, width_m = parse_length(width_str, 'width')
length_in, length_m = parse_length(length_str, 'length')
distance_in, distance_m = parse_length(distance_str, 'distance')

print "Width: {:f} m, ({:f} in)".format(width_m, width_in)
print "Length: {:f} m, ({:f} in)".format(length_m, length_in)
print "Distance: {:f} m, ({:f} in)".format(distance_m, length_in)

LuH = calc_L(width_in, distance_in, length_in)

if (LuH < 1):
    LnH = LuH * 1000.0;
    print "Inductance {:f} nH".format(LnH)
else:
    print "Inductance {:f} uH".format(LuH)
