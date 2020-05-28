#!/usr/bin/env python3
#=== file_transfer.py ===#

import os
import sys
import subprocess
import time

iuBaseDir = os.environ['IUBASEDIR']

def RStrip(string):
	if string.rstrip() == '':
		return 'notSet'
	else:
		return string.rstrip()

statusFileName = iuBaseDir + '/DB/Transfers/' + sys.argv[4]

# Write status
with open(statusFileName, 'w') as file:
	file.write('RUNNING')

loopTransfer = ''
stop = ''

with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'r') as fLoopTransferEn:
	loopTransfer =  RStrip(fLoopTransferEn.read())

fileName = sys.argv[3]
devFrom = sys.argv[1]
devTo = sys.argv[2]
fileFrom = '/media/usb/' + devFrom + '/' + fileName
fileTo = '/media/usb/' + devTo + '/' + fileName

#=== Set title of terminal
print('\33]0;' + 'File Transfer: ' + devFrom + ' => ' + devTo + '\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=10, cols=55))
#===

# Start saving ID of terminal ======================
idFile = open(iuBaseDir + '/DB/TerminalID/FileTransfer.txt', 'a')

terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]

idFile.write(terminalID + '\n')

idFile.close()
# End saving ID of terminal ========================

# Start setting file to transfer ===================
print('\033[1;40;33mSetting up file to transfer.\tPC => ' + devFrom) 
try:
	os.system('pv -pa ' + iuBaseDir + '/DB/Files/' + fileName + ' > ' + fileFrom)
except:
	print('Error with setting up') # for logHelper
	#=== Log Helper ===#
	os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'transfer fail ' + devFrom + ' ' + devTo + ' ' + fileName + 'X X setup X')
	#==
	exit()
os.system('clear')
# End setting file to transfer======================

print('\033[1;40;32m')

# Start file transfer 
i = 0
iP = 0
iF = 0

while True:
	os.system('clear')
	print(fileFrom, ' => ', fileTo)
	print('Iteration: %d  Pass: %d  Fail: %d' %(i, iP, iF))

	try:
		os.system('pv -pa ' + fileFrom + ' > ' + fileTo)
	except:
		print('Error with file transfer') # for logHelper
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'transfer fail ' + devFrom + ' ' + devTo + ' ' + fileName + ' ' + str(i) + ' ' + str(iF) + ' transfer X')
		#==
		exit()

	time.sleep(1)

	try:
		res1 = subprocess.run(['md5sum', fileFrom], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
		res2 = subprocess.run(['md5sum', fileTo], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
	except:
		print('Error with data integrity') # for logHelper
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'transfer fail ' + devFrom + ' ' + devTo + ' ' + fileName + ' ' + str(i) + ' ' + str(iF) + ' dataint 0')
		#==
		exit()
				
	if res1 == res2:
		print('Data Integrity Pass')
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'transfer pass ' + devFrom + ' ' + devTo + ' ' + fileName + ' ' + str(i) + ' ' + str(iF) + ' X X')
		#==
		iP += 1
	else:
		print('\033[1;37;41mData integrity Fail')
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'transfer fail ' + devFrom + ' ' + devTo + ' ' + fileName + ' ' + str(i) + ' ' + str(iF) + ' dataint 1')
		#==
		iF += 1
	
	with open(iuBaseDir + '/DB/Setup/stop.txt', 'r') as file:
		stop = RStrip(file.read())

	if stop == 'YES' or stop == 'notSet':
		break
	if loopTransfer == 'NO':
		break

	time.sleep(1)

	i += 1
# End file transfer

# Print results
os.system('clear')
print('Stopped\n')
print('Iterations:', i)
print('Data Integrity Pass:', iP)
print('Data Integrity Fail:', iF)

# Write status
with open(statusFileName, 'w') as sFile:
	sFile.write('DONE')

# Wait for some action
input('Press [Enter] to continue:')
