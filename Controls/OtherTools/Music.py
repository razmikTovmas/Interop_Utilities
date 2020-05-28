#!/usr/bin/env python3
#=== Music.py ===#

import os
import sys
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'music')
#==

#=== Set title of terminal
print('\33]0;Music\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=       Operating Music       =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)

os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/music.py' + '"')

