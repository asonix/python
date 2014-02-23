#!/usr/bin/python
import math
u = 0.125
for i in xrange(0, 25):
	u = math.sin(math.pi*u)
	print "iteration: {:n} - value: {:n}".format((i+1),u)

p = 0.125
for i in xrange(0, 25):
	p = math.sin(math.pi*p)
	if i == 3:
		p *= 100000
		print p
		p = math.floor(p)
		print p
		p /= 100000
	print "iteration: {:n} - value: {:n}".format((i+1),p)
print "Final unaltered value: {:n}".format(u)
print "Final altered value: {:n}".format(p)

