#!/usr/bin/env python
# coding: utf-8

import sys
import re
col1=[]
for item_of_col1 in open('col1.txt', 'r'):
    item_of_col1 = item_of_col1.rstrip()
    col1.append(item_of_col1)
line_number_of_col1 = 0
for item_of_col2 in open('col2.txt', 'r'):
	print col1[line_number_of_col1] +"\t"+item_of_col2,
	line_number_of_col1 += 1