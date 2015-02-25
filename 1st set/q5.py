#!/usr/bin/env python
# coding: utf-8

import sys
buffer = sys.stdin.read().splitlines()
head_number = sys.argv[1]
current_line_number  = 0
for index, line in enumerate(buffer):
	current_line_number += 1
	print line
	if current_line_number == int(head_number):
		break
