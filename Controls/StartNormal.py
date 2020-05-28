#/usr/bin/env python3
#=== StartNormal.py ===#

import os
import sys
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;' + 'Start Normal\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=        Starting Test        =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)

with open(iuBaseDir + '/DB/Setup/stop.txt', 'w') as file:
	file.write('NO')

with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'w') as file:
		file.write('NO')

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'startnormal')
#==

with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'r') as file:
	devChekEn = file.read().rstrip()

if devChekEn == 'YES':
	#	Start DeviceCheck
	os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/DeviceCheck.py' + '"')

#	Start FileTransfers
os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/FileTransfers.py' + '"')

# 	Start Cameras
os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Cameras.py' + '"')

with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as file:
	topology = file.read().split()[0]

if topology == 'INTEROP':
	#	Start Video
	os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Video.py' + '"')
elif topology == 'BACKWARDS':
	#	Start Audio
	os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Music.py' + '"')

time.sleep(2)

