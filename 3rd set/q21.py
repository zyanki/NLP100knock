#python fileinput.py < filelist.txt
import sys
import re
filelists = sys.stdin.readlines()
for filename in filelists:
	filename = filename.rstrip()
	#print filename
	for line in open(filename, 'r'):
		line = line.rstrip()
		line_break_added = line.replace('.', '.\n')
		show_line = line_break_added.replace('\n ', '\n')
		print show_line
