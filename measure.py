from pint import UnitRegistry

ureg = UnitRegistry()

#the "spectroscopy" ("sp") context enables pinto
#to convert frequency to wavelength and vice-versa
ureg.enable_contexts('sp')

def parse_length(length_str, name = "length"):
    length_in = length_m = None
    try:
        length = ureg.parse_expression(length_str)
        length_in = length.to(ureg.inch).magnitude
        length_m = length.to(ureg.meter).magnitude
    except AttributeError:
        print "Please speficy {:s} measure unit (m, cm, in, ..)".format(name)
        exit(-1)
    return length_in, length_m

def parse_freq(freq_str, name = "frequency"):
    freq_hz = wlen_in = wlen_m = None
    try:
        freq = ureg.parse_expression(freq_str)
        freq_hz = freq.to(ureg.hertz).magnitude
        wlen_in = freq.to(ureg.inch).magnitude
        wlen_m = freq.to(ureg.meter).magnitude
    except AttributeError:
        print "Please specify {:s} measuere unit (Hz, MHz, ..)".format(name)
        exit(-1)
    return freq_hz, wlen_in, wlen_m
