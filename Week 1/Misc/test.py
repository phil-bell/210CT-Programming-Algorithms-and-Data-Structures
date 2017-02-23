import collections
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

print d

for a,b in d.items():
	print a,b

print "-------------------------------------------------"

e = {}

e['a'] = 'A'
e['b'] = 'B'
e['c'] = 'C'
e['d'] = 'D'
e['e'] = 'E'

print e

for a,b in e.items():
	print a,b