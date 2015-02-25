#!/usr/bin/env python
# coding: utf-8
#python q6.py /Users/a18818/NLP100knock/data\ set/KEN_ALL.txt 2

import sys

arg = sys.argv
filepath = arg[1]
readnumber = int(arg[2])

try:
	file = open(filepath)
	lines = file.readlines()
	length = len(lines)
finally:
	file.close()
for i in range(length - readnumber, length):
	print lines[i],
