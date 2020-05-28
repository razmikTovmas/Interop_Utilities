#!/usr/bin/env python3
#=== Hibernate.py ===#

import os
import time
import sys

iuBaseDir = os.environ['IUBASEDIR']

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'hibernate')
#==

#=== Set title of terminal
print('\33]0;Hibernate\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=    Entering to Hibernate    =\n'
      '==                           ==\n'
      '===============================')

time.sleep(0.5)

try:
	os.system('pkill pv')
except:
	print('PKILL')

time.sleep(1)

with open(iuBaseDir + '/DB/TerminalID/DeviceCheck.txt', 'r') as file: # kill device check
		os.system('xdotool windowclose ' + file.read().rstrip())
os.system('clear')

print('===============================\n'
      '==                           ==\n'
      '=    Entering to Hibernate    =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)

os.system('systemctl hibernate')

time.sleep(20) # Device Check Poll Time

os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/DeviceCheck.py"')
