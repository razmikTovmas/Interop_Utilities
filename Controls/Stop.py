#!/usr/bin/env python3
#=== Stop.py ===#

import os
import subprocess
import sys
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;Stop\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=8, cols=31))
#===

print('===============================\n'
      '=====                     =====\n'
      '==       Stopping Test       ==\n'
      '=  Waiting for file transfers =\n'
      '==       to be finished      ==\n'
      '=====                     =====\n'
      '===============================')

time.sleep(1)

def KillAllTasks():
    #=== Kill File Transfer(s)
    with open(iuBaseDir + '/DB/TerminalID/FileTransfer.txt', 'r') as file:
        for line in file:
            os.system('xdotool windowclose ' + line.split()[0])
    #=== Kill Camera(s), Video and Audio
    os.system('pkill mplayer')
    #=== Kill Device Check
    with open(iuBaseDir + '/DB/TerminalID/DeviceCheck.txt', 'r') as file:
        os.system('xdotool windowclose ' + file.read().rstrip())

    with open(iuBaseDir + '/DB/Setup/stop.txt', 'w') as file:
            file.write('NO')

    os.system('rm -rf ' + iuBaseDir + '/DB/Transfers/*.txt')

    with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'w') as file:
        file.write('YES')

    #=== Kill File Transfer(s)
    with open(iuBaseDir + '/DB/TerminalID/Stop.txt', 'r') as file:
        for line in file:
            os.system('xdotool windowclose ' + line.rstrip())

#=== __main__ ===#

res = ''

with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'w') as file:
        file.write('NO')

with open(iuBaseDir + '/DB/Setup/stop.txt', 'r') as file:
    if file.read().rstrip() == 'YES':
        #=== Log Helper ===#
        os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'stop killed')
        #==

        time.sleep(2)
        KillAllTasks()
        exit()

# Start saving ID of terminal ======================
terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]

with open(iuBaseDir + '/DB/TerminalID/Stop.txt', 'w') as idFile:
    idFile.write(terminalID + '\n')
# End saving ID of terminal ========================

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'stop stopping')
#==

with open(iuBaseDir + '/DB/Setup/stop.txt', 'w') as file:
    file.write('YES')

status = True

fileList = subprocess.run(['ls', iuBaseDir + '/DB/Transfers/'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()

while status:
    strCheck = ''
    for fileName in fileList:
        with open(iuBaseDir + '/DB/Transfers/' + fileName, 'r') as file:
            strCheck += file.read()

    if 'RUNNING' in strCheck:
        status = True
    else:
        status = False
        break

#=== Log Helper ===#
os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'stop stopped')
#==

time.sleep(2)

KillAllTasks()
