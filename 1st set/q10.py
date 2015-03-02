#!/usr/bin/env python
# coding: utf-8
# python q9.py ../data\ set/KEN_ALL.txt 
import sys
import re
arg = sys.argv
filepath = arg[1]
try:
	file = open(filepath)
	lines = file.readlines()
finally:
	file.close()
dic ={}
for line in lines:
	matched_by_tab = re.match(r"(.*)\t(.*)", line)
	if dic.has_key(matched_by_tab.group(2)):
		dic[matched_by_tab.group(2)] += 1
	else:
		dic[matched_by_tab.group(2)] = 1
for w, c in sorted(dic.iteritems(), key=lambda x: x[1], reverse=True):
	print w, c