# A part of pdfrw (pdfrw.googlecode.com)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

# Deal with Python2/3 differences

try:
    import zlib
except ImportError:
    zlib = None

try:
    unicode = unicode
except NameError:

    def convert_load(s):
        return s.decode('Latin-1')

    def convert_store(s):
        return s.encode('Latin-1')

    def from_array(a):
        return a.tobytes()

else:

    def convert_load(s):
        return s

    def convert_store(s):
        return s

    def from_array(a):
        return a.tostring()

nextattr, = (x for x in dir(iter([])) if 'next' in x)

try:
    iteritems = dict.iteritems
except AttributeError:
    iteritems = dict.items

try:
    xrange = xrange
except NameError:
    xrange = range
