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
second_col =[]
dic ={}
for line in lines:
	matched_by_tab = re.match(r"(.*)\t(.*)", line)
	second_col.append(matched_by_tab.group(2))
	dic[matched_by_tab.group(2)]=0
sorted(dic.items()):
    print k
