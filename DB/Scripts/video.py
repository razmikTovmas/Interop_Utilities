#!/usr/bin/env python3
#=== video.py ===#

import os
import subprocess
import sys
import time

print('\33]0;Video\a', end='', flush=True)  # Title of terminal

iuBaseDir = os.environ['IUBASEDIR']

def RStrip(string):
	if string.rstrip() == '':
		return 'notSet'
	else:
		return string.rstrip()

#=== Set title of terminal
print('\33]0;Video\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=20, cols=20))

time.sleep(0.5)
#=== Minimize terminal ===#
terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
os.system('xdotool windowminimize ' + terminalID)
#===

with open(iuBaseDir + '/DB/Media/VideoFileName.txt') as file:
	fileName = RStrip(file.read())

os.system('mplayer -loop 0 ' + iuBaseDir + '/DB/Media/' + fileName)
