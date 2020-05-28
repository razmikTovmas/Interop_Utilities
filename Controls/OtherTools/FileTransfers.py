#!/usr/bin/env python3
#=== FileTransfers.py ===#

import os
import sys
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;File Transfers\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=   Starting File Transfers   =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)

with open(iuBaseDir + '/DB/TerminalID/FileTransfer.txt', 'w') as idFile:
	idFile.write('')

os.system('rm -rf ../../DB/Transfers/*') # check this one

with open(iuBaseDir + '/DB/Setup/DriveLetters.txt', 'r') as rFile:
	driveLetters = rFile.read().rstrip()

## SS -> FS
## HS -> SS

i = 1

fileSize = ' '

if 'SS' in driveLetters and 'HS' in driveLetters:
	# Start transfer. pv HS/LargeFile > SS/LargeFile
	with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'r') as file:
		fileSize = file.read().rstrip()
	cmd = 'HS SS ' + fileSize + 'MB.zip' + ' Transfer' + str(i) + '.txt'
	os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/file_transfer.py ' + cmd + '"')
	time.sleep(1)
	i += 1

if 'SS' in driveLetters and 'FS' in driveLetters:
	# Start transfer. pv SS/SmallFile > FS/SmallFile
	with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'r') as file:
		fileSize = file.read().rstrip()
	cmd = 'SS FS ' + fileSize + 'MB.zip' + ' Transfer' + str(i) + '.txt'
	os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/file_transfer.py ' + cmd + '"')
	i += 1

