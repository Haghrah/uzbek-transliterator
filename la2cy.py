# -*- coding: utf-8 -*-
import transliterate as tl
import sys

for arg in sys.argv[1:]:
	argfile = open(arg, "r")
	outfile = open(arg[:-arg[::-1].find(".")-1] + "_cy" + arg[-arg[::-1].find(".")-1:], "w")
	for line in argfile:
		outfile.write(tl.transliterate(line, "cyrillic"))
	outfile.close()
	argfile.close()


