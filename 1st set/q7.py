#!/usr/bin/env python
# coding: utf-8
# python q7.py ../data\ set/KEN_ALL.txt 
import sys
import re
arg = sys.argv
filepath = arg[1]
try:
	file = open(filepath)
	lines = file.readlines()
finally:
	file.close()
first_col =[]
for line in lines:
	matched_by_tab = re.match(r"(.*)\t(.*)", line)
	first_col.append(matched_by_tab.group(1))
first_col_set = set(first_col)
print len(first_col_set)