#!/usr/bin/env python
# coding: utf-8

import sys
import re
buffer = sys.stdin.read().splitlines()
f_of_col1 = open('col1.txt', 'w')
f_of_col2 = open('col2.txt', 'w')
for index,line in enumerate(buffer):
	line_split_by_tab =  line.split('\t')
	f_of_col1.write(line_split_by_tab[0]+"\n")
	f_of_col2.write(line_split_by_tab[1]+"\n")
f_of_col1.close()
f_of_col2.close()