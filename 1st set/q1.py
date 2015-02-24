#!/usr/bin/env python
# coding: utf-8

import sys

buffer = sys.stdin.read().splitlines()
length = len(str(len(buffer)))
format_template = '%%0%sd: %%s' % length

for index, line in enumerate(buffer, start = 1):
  print format_template % (index, line)
