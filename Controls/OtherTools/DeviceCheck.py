#!/usr/bin/env python3
#=== DeviceCheck.py ===#

import os
import sys
import subprocess
import time

def RStrip(string):
	if string.rstrip() == '':
		return 'notSet'
	else:
		return string.rstrip()	

def MainPrint(devName, devApplied, devDetected):

	devAppLen = str(devApplied) + ' ' * (10 - len(str(devApplied)))
	devDetLen = str(devDetected) + ' ' * (10 - len(str(devDetected)))
	print('|__ ' + devName  + ' '  * (20 - len(str(devName))) + devAppLen + devDetLen + ' __|')

def PrintDevices():
	lib.GetDevices()
	lib.GetDevicesCount()

	with open(iuBaseDir + '/DB/Setup/AppliedDevicesCount.txt', 'r') as fAppliedCount:
		SSP_AppliedDevCount = RStrip(fAppliedCount.readline())
		SS_AppliedDevCount = RStrip(fAppliedCount.readline())
		SSP_AppliedHubCount = RStrip(fAppliedCount.readline())
		SS_AppliedHubCount = RStrip(fAppliedCount.readline())
		HS_AppliedHubCount = RStrip(fAppliedCount.readline())
		FS_AppliedHubCount = RStrip(fAppliedCount.readline())
		MSC_AppliedDevCount = RStrip(fAppliedCount.readline())
		HID_AppliedDevCount = RStrip(fAppliedCount.readline())
		WebCam_AppliedDevCount = RStrip(fAppliedCount.readline())
		DisplayLink_AppliedDevCount = RStrip(fAppliedCount.readline())
		Total_AppliedDevCount = RStrip(fAppliedCount.readline())

	with open(iuBaseDir + '/DB/Setup/DetectedDevicesCount.txt', 'r') as fDetectedCount:
		SSP_DetectedDevCount = RStrip(fDetectedCount.readline())
		SS_DetectedDevCount = RStrip(fDetectedCount.readline())
		SSP_DetectedHubCount = RStrip(fDetectedCount.readline())
		SS_DetectedHubCount = RStrip(fDetectedCount.readline())
		HS_DetectedHubCount = RStrip(fDetectedCount.readline())
		FS_DetectedHubCount = RStrip(fDetectedCount.readline())
		MSC_DetectedDevCount = RStrip(fDetectedCount.readline())
		HID_DetectedDevCount = RStrip(fDetectedCount.readline())
		WebCam_DetectedDevCount = RStrip(fDetectedCount.readline())
		DisplayLink_DetectedDevCount = RStrip(fDetectedCount.readline())
		Total_DetectedDevCount = RStrip(fDetectedCount.readline())

	print(' ______________________________________________\n'
	      '|__                                          __|')
	MainPrint('DEVICE NUMBERS:', 'APPLIED:', 'DETECTED:')
	MainPrint('SS+ Devices:', SSP_AppliedDevCount, SSP_DetectedDevCount)
	MainPrint('SS Devices:', SS_AppliedDevCount, SS_DetectedDevCount)
	MainPrint('SS+ Hubs:', SSP_AppliedHubCount, SSP_DetectedHubCount)
	MainPrint('SS Hubs:', SS_AppliedHubCount, SS_DetectedHubCount)
	MainPrint('HS Hubs:', HS_AppliedHubCount, HS_DetectedHubCount)
	MainPrint('FS Hubs:', FS_AppliedHubCount, FS_DetectedHubCount)
	MainPrint('MSC Devices:', MSC_AppliedDevCount, MSC_DetectedDevCount)
	MainPrint('HID Devices:', HID_AppliedDevCount, HID_DetectedDevCount)
	MainPrint('WebCams:', WebCam_AppliedDevCount, WebCam_DetectedDevCount)
	MainPrint('DisplayLink:', DisplayLink_AppliedDevCount, DisplayLink_DetectedDevCount)
	MainPrint('Total Devices:', Total_AppliedDevCount, Total_DetectedDevCount)
	print(' |____________________________________________|\n\n')

print('\33]0;Device Check\a', end='', flush=True)  # Title of terminal

iuBaseDir = os.environ['IUBASEDIR']

import importlib.util
spec = importlib.util.spec_from_file_location('module.name', iuBaseDir + '/DB/Scripts/lib.py')
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)

import time

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=3, cols=30))
print('\033[1;40;32m ****  Device Check Pass  ****')

# Start saving ID of terminal ======================
terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]

with open(iuBaseDir + '/DB/TerminalID/DeviceCheck.txt', 'w') as file:
	file.write(terminalID + '\n')
#===

with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'w') as file:
	file.write('NO')

while True:
	lib.GetDevicesForDeviceCheck()

	with open(iuBaseDir + '/DB/Setup/Stopped.txt', 'r') as file:
		if file.read().rstrip() == 'YES':
			break

	devCheck = lib.DeviceCheck()

	if not devCheck:
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'devicecheck fail')
		#==
		break

	#=== Log Helper ===#
	os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'devicecheck pass')
	#==

	time.sleep(3)

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=18, cols=48))

if devCheck:
	print('\033[1;40;32m*** Device Check Pass ***')
else:
	print('\033[1;37;41m*** Device Check Fail ***')

PrintDevices()

x = input('Press [enter] to continue...')

