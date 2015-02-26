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
	dic[matched_by_tab.group(2)]=matched_by_tab.group(1)
for k, v in sorted(dic.items(),  key=lambda x:(x[0],x[1]),reverse=True):
    print v,k
