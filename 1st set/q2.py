#!/usr/bin/env python
# coding: utf-8

import sys
buffer = sys.stdin.read().splitlines()
for index,line in enumerate(buffer):
    print (line.expandtabs(1))