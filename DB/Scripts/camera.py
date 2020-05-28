#!/usr/bin/env python3
#=== camera.py ===#

import os
import sys
import subprocess
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;Camera\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=20, cols=20))

time.sleep(0.5)
#=== Minimize terminal ===#
terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
os.system('xdotool windowminimize ' + terminalID)
#===

camLoc = sys.argv[1]
def_width = sys.argv[2]
def_height = sys.argv[3]

os.system('mplayer tv:// -tv driver=v4l2:width=' + def_width + ':height=' + def_height + ':device=' + camLoc)
