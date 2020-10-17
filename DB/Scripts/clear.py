#!/usr/bin/env python3
#=== clear.py ===#

import os
import sys

iuBaseDir = os.environ['IUBASEDIR']

if len(sys.argv) == 1:
    x = 'all'
else:
    x = sys.argv[1]

if x == 'all' or x == 'AppD': # AppD
    with open(iuBaseDir + '/DB/Setup/AppliedDevices.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'AppDC': # AppDC
    with open(iuBaseDir + '/DB/Setup/AppliedDevicesCount.txt', 'w') as f:
        f.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0')

if x == 'all' or x == 'Cam': # Cam
    with open(iuBaseDir + '/DB/Setup/Camera.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'CamAC': # CamAC
    with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'w') as f:
        f.write('NO')

if x == 'all' or x == 'Con': # Con
    with open(iuBaseDir + '/DB/Setup/Config.txt', 'w') as f:
        f.write('INTEROP')

if x == 'all' or x == 'CurL': # CurL
    with open(iuBaseDir + '/DB/Setup/CurrentLog.txt', 'w') as f:
        f.write('Log.txt')

if x == 'all' or x == 'DetD': # DetD
    with open(iuBaseDir + '/DB/Setup/DetectedDevices.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'DetDC': # DetDC
    with open(iuBaseDir + '/DB/Setup/DetectedDevicesCount.txt', 'w') as f:
        f.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0')

if x == 'all' or x == 'DevCA': # DevCA
    with open(iuBaseDir + '/DB/Setup/DevCheckApplied.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'DevCD': # DevCD
    with open(iuBaseDir + '/DB/Setup/DevCheckDetected.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'DevCE': # DevCE
    with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'w') as f:
        f.write('YES')

if x == 'all' or x == 'DriL': # DriL
    with open(iuBaseDir + '/DB/Setup/DriveLetters.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'LarF': # LarF
    with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'w') as f:
        f.write('notSet')

if x == 'all' or x == 'LogE': # LogE
    with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'w') as f:
        f.write('YES')

if x == 'all' or x == 'LooTE': # LooTE
    with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'w') as f:
        f.write('YES')

if x == 'all' or x == 'SmaF': # SmaF
    with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'w') as f:
        f.write('notSet')

if x == 'all' or x == 'sto': # sto
    with open(iuBaseDir + '/DB/Setup/stop.txt', 'w') as f:
        f.write('NO')

if x == 'all' or x == 'Sto': # Sto
    with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'w') as f:
        f.write('NO')

if x == 'all' or x == 'MAudFN': # MAudFN
    with open(iuBaseDir + '/DB/Media/AudioFileName.txt', 'w') as f:
        f.write('SleepAway.mp3')

if x == 'all' or x == 'MVidFN': # MVidFN
    with open(iuBaseDir + '/DB/Media/VideoFileName.txt', 'w') as f:
        f.write('HD_Canada.m2ts')

if x == 'all' or x == 'TDevC': # TDevC
    with open(iuBaseDir + '/DB/TerminalID/DeviceCheck.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'TFilT': # TFilT
    with open(iuBaseDir + '/DB/TerminalID/FileTransfer.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'TSto': # TSto
    with open(iuBaseDir + '/DB/TerminalID/Stop.txt', 'w') as f:
        f.write('')

if x == 'all' or x == 'TStoFT': # TStoFT
    with open(iuBaseDir + '/DB/TerminalID/StopFT.txt', 'w') as f:
        f.write('')
