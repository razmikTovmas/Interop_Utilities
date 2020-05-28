#!/usr/bin/env python3
#=== BootCold.py ===#

import os
import time
import sys

iuBaseDir = os.environ['IUBASEDIR']

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'coldboot')
#==

#=== Set title of terminal
print('\33]0;Warm Boot\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=    Entering to Cold Boot    =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)

os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/Stop.py"')

while True:
	with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'r') as file:
		if 'YES' in file.read():
			break

time.sleep(2)

os.system('poweroff')

