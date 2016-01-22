#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hw2

def main(args):
	try:
		number = int(args[1])
		if number < 1:
			raise
	except:
		print "Your input is wrong"
		return
	for i in range(1, number+1):
		if i % 6 == 0:
			print 'fizzbuzz'
		elif i % 2 == 0:
			print 'fizz'
		elif i % 3 == 0:
			print 'buzz'
		else:
			print i

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
