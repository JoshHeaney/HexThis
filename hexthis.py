#!/usr/bin/python
#Josh Heaney
#May 17 2016
#Convert argv values to hex

import sys
import binascii
from optparse import OptionParser

#Optional arguments
parser = OptionParser("python hexthis.py [option(s)] [string(s)]\n Display the input strings converted to hex in the specified format.\n Output is little endian by default.")
parser.add_option("-b", "--bigendian", action="store_true", dest="big", default=False, help="display hex result in big endian order.")
parser.add_option("-s", "--string", action="store_true", dest="string", default=False, help="display hex result as a formated string.")
parser.add_option("-n", "--number", action="store_true", dest="number", default=False, help="treat the input as a hex number and stringify it.")
(options, args) = parser.parse_args()



if len(args) >= 1:
	for val in args:
		result = ''
		sys.stdout.write(val + ":   ")
		if options.number: #Reformat an input hex number
			if val[0]=='0' and val[1]=='x':
				val=val[2:]
			if len(val)%2: #Make sure it has an even length
				val = '0' + val
			for i in range(0, len(val)-1, 2):
				if options.big: #For big endian output
					result += '\\x' + val[i:i+2]
				else:
					result = '\\x' + val[i:i+2] + result
			result = "\"" + result + "\""
		else:
			for c in val:
				if options.big:
					if options.string: #String version add 
						result += '\\x'
					result += binascii.hexlify(c)
				else:
					result = binascii.hexlify(c) + result
					if options.string: #String version add 
						result = '\\x' + result
			if options.string:
				result = "\"" + result + "\""
			else:
				result = '0x' + result
		sys.stdout.write(result + "\n")
else:
	print("No args")
	sys.exit()

