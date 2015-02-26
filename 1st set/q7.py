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
pattern_for_first_col = re.compile(r'.*\t')
for line in lines:
	line_matched_by_tab = pattern_for_first_col.finditer(line)
	for get_first_col in line_matched_by_tab:
		first_col.append(get_first_col.group(0))
first_col_set = set(first_col)
print len(first_col_set)