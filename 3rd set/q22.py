##! /usr/bin/env python
# -*- python -*-
# -*- encoding: utf-8 -*-
import nltk
import sys
import re

filelists = sys.stdin.readlines()
for filename in filelists:
	filename = filename.rstrip()
	for line in open(filename, 'r'):
		line = line.rstrip()
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		print('\n-----\n'.join(sent_detector.tokenize(line)))
