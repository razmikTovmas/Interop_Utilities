#!/usr/bin/env python3
#=== console.py ===#

from cmd import Cmd
import os
import sys
import subprocess
import time
from datetime import datetime

iuBaseDir = os.environ['IUBASEDIR']

import importlib.util
spec = importlib.util.spec_from_file_location('module.name', iuBaseDir + '/DB/Scripts/lib.py')
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)

def RStrip(string):
	if string.rstrip() == '':
		return 'notSet'
	else:
		return string.rstrip()

##########################################	M A I N 	S C R E E N  ###############################################
class MainScreen(Cmd):

	command = ''

	def do_q(self, args):
		''' Quit the setup. '''
		#=== Log Helper ===#
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'setup')
		#==
		print ('Quitting.')
		exit()

	def do_a(self, args):
		''' Apply detected devices. '''
		lib.ApplyDevices()
		main_screen()

	def do_s(self, args):
		''' Go you to the Settings screen. '''
		self.command = 's'
		return True

	def do_r(self, args):
		''' Refreshe the screen.'''
		main_screen()

	def do_c(self, args):
		''' Change the config name '''
		self.command = 'c'
		return True

	def do_n(self, args):
		''' Create a New Log. '''
		self.command = 'n'
		return True

	def do_clear(self, args):
		''' This command will reset all config values, this required when scripts work not probably '''
		os.system('python3 ' + iuBaseDir + '/DB/Scripts/clear.py all')
		main_screen()

def main_print(devName, devApplied, devDetected):

	devAppLen = str(devApplied) + ' ' * (24 - len(str(devApplied)))
	devDetLen = str(devDetected) + ' ' * (14 - len(str(devDetected)))
	print('|__      ' + devName  + ' '  * (22 - len(str(devName))) + devAppLen + devDetLen + '__|')

def main_settings_print(setName1, setName2):

	setName1 = setName1 + ' ' * (28 - len((setName1)))
	setName2 = setName2 + ' ' * (32 - len((setName2)))
	print('|__      ' + setName1  + setName2 +  '__|')

def main_screen():
	
	lib.GetDevices()
	lib.GetDevicesCount()

	os.system('clear')

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

	# DETECTED DRIVE LETTERS
	proc = subprocess.Popen('ls /media/usb', shell=True, stdout=subprocess.PIPE,)
	deviceLetters = proc.communicate()[0]
	deviceLetters = deviceLetters.decode('utf-8').split()
	deviceLetters = '  '.join(deviceLetters)

	with open(iuBaseDir + '/DB/Setup/DriveLetters.txt', 'w') as fDriveLetters:
		fDriveLetters.write(deviceLetters)

	# CONFIG
	try:
		with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as fConfig:
			Config = RStrip(fConfig.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py Con"')
		Config = 'INTEROP'

	# SETTINGS
	try:	
		with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'r') as fLoopTransferEn:
			LoopTransfersEn = RStrip(fLoopTransferEn.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py LooTE"')
		LoopTransfersEn = 'YES'

	try:
		with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'r') as fDeviceCheckEn:
			DeviceCheckEn = RStrip(fDeviceCheckEn.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py DevCE"')
		DeviceCheckEn = 'YES'

	try:
		with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'r') as fLargeFile:
			LargeFile = RStrip(fLargeFile.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py LarF"')
		LargeFile = 'notSet'

	try:
		with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'r') as fSmallFile:
			SmallFile = RStrip(fSmallFile.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py SmaF"')
		SmallFile = 'notSet'

	try:
		with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'r') as fLoggingEn:
			LoggingEn = RStrip(fLoggingEn.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py LogE"')
		LoggingEn = 'YES'

	try:
		with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'r') as fCameraAutoConfig:
			CameraAutoConfig = RStrip(fCameraAutoConfig.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py CamAC"')
		CameraAutoConfig = 'NO'
	
	try:
		with open(iuBaseDir + '/DB/Setup/CurrentLog.txt', 'r') as fCurrentLogName:
			CurrentLogName = RStrip(fCurrentLogName.read())
	except:
		os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/clear.py CurL"')
		CurrentLogName = 'Log.txt'

	TransferMode = 'R/W'

	print(' ______________________________________________________________________\n'
	      '|__                                                                  __|\n'
          '|__   DETECTED DRIVE LETTERS:                                        __|')
	main_print(deviceLetters,'','')
	main_print('','','')
	main_print('DEVICE NUMBERS:', 'APPLIED:', 'DETECTED:')
	main_print('SS+ Devices:', SSP_AppliedDevCount, SSP_DetectedDevCount)
	main_print('SS Devices:', SS_AppliedDevCount, SS_DetectedDevCount)
	main_print('SS+ Hubs:', SSP_AppliedHubCount, SSP_DetectedHubCount)
	main_print('SS Hubs:', SS_AppliedHubCount, SS_DetectedHubCount)
	main_print('HS Hubs:', HS_AppliedHubCount, HS_DetectedHubCount)
	main_print('FS Hubs:', FS_AppliedHubCount, FS_DetectedHubCount)
	main_print('MSC Devices:', MSC_AppliedDevCount, MSC_DetectedDevCount)
	main_print('HID Devices:', HID_AppliedDevCount, HID_DetectedDevCount)
	main_print('WebCams:', WebCam_AppliedDevCount, WebCam_DetectedDevCount)
	main_print('DisplayLink:', DisplayLink_AppliedDevCount, DisplayLink_DetectedDevCount)
	main_print('Total Devices:', Total_AppliedDevCount, Total_DetectedDevCount)
	main_print('','','')
	main_print('Configuration:', Config, '')
	main_print('','','')
	print('|__      Current Log Name:     ' + CurrentLogName + ' ' * (38 - len(CurrentLogName)) + '__|')
	main_print('','','')
	main_print('SETTINGS:', '', '')
	main_settings_print('Loop Transfers:  ' + str(LoopTransfersEn), 'Device Check:  ' + str(DeviceCheckEn))
	main_settings_print('Large File:  ' + str(LargeFile) + 'MB', 'Small File:  ' + str(SmallFile)+ 'MB')
	main_settings_print('Logging:  ' + str(LoggingEn), 'Cam Auto Config:  ' +  str(CameraAutoConfig))
	main_settings_print('Transfer Mode:  ' + TransferMode, '')
	print('|__                                                                  __|\n'		  
	      '|__  OPTIONS:                                                        __|\n'
	      '|__  a - Apply Detected   c - Config        r - Refresh Display      __|\n'
	      '|__  s - Settings         n - New Log       q - Quit                 __|\n'
          '|__  --------------------------------------------------------------  __|\n'
          '|__               clear - will reset all config values               __|\n'
	      ' |____________________________________________________________________|\n\n')

#************************************************************************************************************************
#************************************************************************************************************************

##########################################	S E T T I N S 	S C R E E N  ###############################################

class SettingsScreen(Cmd):

	command = ''

	def do_b(self, args):
		''' Go back to the Main Screen. '''
		self.command = 'b'
		return True

	def do_r(self, args):
		''' Refreshe the screen.'''
		settings_screen()

	def do_w(self, args):
		''' Webcam setup '''
		self.command = 'w'
		return True

	def do_x(self, args):
		''' Toggle LoopTransfersEn. '''
		with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'r') as fLoopTransfersEnR:
			isLoopTransfer = RStrip(fLoopTransfersEnR.read())

		with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'w') as fLoopTransfersEnW:
			if isLoopTransfer == 'YES':
				fLoopTransfersEnW.write('NO')
			elif isLoopTransfer == 'NO':
				fLoopTransfersEnW.write('YES')
			elif isDeviceCheck == 'notSet':
				fLoopTransfersEnW.write('YES')

		settings_screen()

	def do_d(self, args):
		''' Toggle DeviceChekEn. '''
		with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'r') as fDeviceCheckEnR:
			isDeviceCheck = RStrip(fDeviceCheckEnR.read())
		
		with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'w') as fDeviceCheckEnW:
			if isDeviceCheck == 'YES':
				fDeviceCheckEnW.write('NO')
			elif isDeviceCheck == 'NO':
				fDeviceCheckEnW.write('YES')
			elif isDeviceCheck == 'notSet':
				fDeviceCheckEnW.write('YES')

		settings_screen()	

	def do_l(self, args):
		''' Toggle LoggingEn. '''
		with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'r') as fLoggingEnR:
			isLogging = RStrip(fLoggingEnR.read())

		with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'w') as fLoggingEnW:
			if isLogging == 'YES':
				fLoggingEnW.write('NO')
			elif isLogging == 'NO':
				fLoggingEnW.write('YES')
			elif isDeviceCheck == 'notSet':
				fLoggingEnW.write('YES')

		settings_screen()	

	def do_s(self, args):
		''' Choose SmallFile size. '''
		newSmallFile = input('\nPlease enter a new Small File size in MB\n')
		if newSmallFile.isdigit() and newSmallFile[0] != '0':
			with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'w') as fSmallFile:
				fSmallFile.write(newSmallFile)

			fileList = subprocess.run(['ls', iuBaseDir + '/DB/Files/'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()
			fileName = newSmallFile + 'MB.zip'
			if not fileName in fileList:
				os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/build_file.py ' + newSmallFile + '"')
		
		settings_screen()
   
	def do_f(self, args):
		''' Choose LargeFile size. '''
		newLargeFile = input('\nPlease enter a new Large File size in MB\n')
		if newLargeFile.isdigit() and newLargeFile[0] != '0':
			with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'w') as fLargeFile:
				fLargeFile.write(newLargeFile)

			fileList = subprocess.run(['ls', iuBaseDir + '/DB/Files/'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()
			fileName = newLargeFile + 'MB.zip'
			if not fileName in fileList:
				os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/build_file.py ' + newLargeFile + '"')
		
		settings_screen()

	def do_z(self, args):
		''' Cleanup Zip Files. '''
		os.system('rm -rf ' + iuBaseDir + '/DB/Files/*.zip')
		with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'w') as fLargeFile:
				fLargeFile.write('notSet')
		with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'w') as fSmallFile:
				fSmallFile.write('notSet')
		settings_screen()

def settings_print(setName1, setName2):

	setName1 = setName1 + ' ' * (28 - len((setName1)))
	setName2 = setName2 + ' ' * (32 - len((setName2)))
	print('***      ' + setName1  + setName2 +  '***')

def settings_screen():
	os.system('clear')

	with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'r') as fLoopTransferEn:
		LoopTransfersEn = RStrip(fLoopTransferEn.read())

	with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'r') as fDeviceCheckEn:
		DeviceCheckEn = RStrip(fDeviceCheckEn.read())

	with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'r') as fLoggingEn:
		LoggingEn = RStrip(fLoggingEn.read())

	LoopTransfersEn = 'X' if LoopTransfersEn == 'YES' else ' '
	DeviceCheckEn = 'X' if DeviceCheckEn == 'YES' else ' '
	LoggingEn = 'X' if LoggingEn == 'YES' else ' '

	with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'r') as fLargeFile:
		LargeFile = RStrip(fLargeFile.read())

	with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'r') as fSmallFile:
		SmallFile = RStrip(fSmallFile.read())

	print(' ____________________________________________________ \n'
	      '|__                   SETTINGS                     __|\n'
	      '|                                                    |\n'
	      '|__  Options:                                      __|\n'
	      '|__  w - Webcam Setup                              __|\n' #22
	      '|__  x - LoopTransfersEn   [' + LoopTransfersEn + ']                     __|\n'
	      '|__  d - Device Check   [' + DeviceCheckEn + ']                        __|\n'
	      '|__  l - Log Interop Activity   [' + LoggingEn + ']                __|\n'
	      '|__  f - Large File Size:    ' + LargeFile + 'MB' + ' ' * (18 - len(str(LargeFile))) + '  __|\n'
	      '|__  s - Small File Size:    ' + SmallFile + 'MB' + ' ' * (18 - len(str(SmallFile))) + '  __|\n'
	      '|__  z - Cleanup Zip Files 			  __|\n'
	      '|__  b - Back                                      __|\n'
	      ' |__________________________________________________| \n')

#************************************************************************************************************************
#************************************************************************************************************************

##########################################	W E B C A M 	S C R E E N  ###############################################

class WebcamScreen(Cmd):

	command = ''
	def do_b(self, args):
		''' Go back to the settings screen '''
		self.command = 'b'
		return True

	def do_a(self,args):
		with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'r') as fWebcamAutoConfigR:
			isAutoConfig = RStrip(fWebcamAutoConfigR.read())

		with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'w') as fWebcamAutoConfigW:
			if isAutoConfig == 'YES':
				fWebcamAutoConfigW.write('NO')
			elif isAutoConfig == 'NO':
				fWebcamAutoConfigW.write('YES')
			elif isAutoConfig == 'notSet':
				fWebcamAutoConfigW.write('YES')

		webcam_screen()

	def do_m(self, args):
		''' Manually setup detected cameras '''
		cmd = 'ls /dev/video*'	

		proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,)
		output = proc.communicate()[0]
		output = output.decode("utf-8").split()

		with open(iuBaseDir + '/DB/Setup/Camera.txt', 'w') as fCameraN:
			fCameraN.write('')

		for camLoc in output:
			os.system('gnome-terminal -e "mplayer tv:// -tv driver=v4l2:device=' + camLoc + '"')
# razmikt
			time.sleep(1)
			#=== Select terminal ===#
			terminalID = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()[0]
			os.system('xdotool windowactivate ' + terminalID) # razmikt test this :)
# razmikt : end
			camRes = input('Please choose a resolution for this camera from the list above\n')
			if(camRes == '1'):
				camWidth = 160
				camLength = 120
			elif(camRes == '2'):
				camWidth = 320
				camLength = 240
			elif(camRes == '3'):
				camWidth = 640
				camLength = 480
			elif(camRes == '4'):
				camWidth = 800
				camLength = 600
			elif(camRes == '5'):
				camWidth = 1280
				camLength = 720
			else:
				print('Invalid input: Setting by default config 320x240')
				camWidth = 320
				camLength = 240


			with open(iuBaseDir + '/DB/Setup/Camera.txt', 'a') as fCameraN:
				fCameraN.write(str(camLoc) + ' ' + str(camWidth) + ' ' + str(camLength) + '\n')
			os.system('pkill mplayer')

		webcam_screen()

def webcam_screen():
	os.system('clear')

	fWebcamAutoConfigR = open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'r')

	isAutoConfig = fWebcamAutoConfigR.read().split()[0]

	if isAutoConfig == 'YES':
		isAutoConfig = 'X'
	else:
		isAutoConfig = ' '
	print(' ___________________________________________________________ \n'
	      '|__                  WEBCAM SETUP SCREEN                  __|\n'
	      '|                                                           |\n'
	      '|     Camera Auto Config    [' + isAutoConfig + ']                             |\n'
	      '|                                                           |\n'
	      '|     Options                                               |\n'
	      '|__   a - Toggle Automatic Camera Configuration           __|\n'
	      '|__   m - Setup Cameras Manually                          __|\n'
	      '|__       (Will turn on cameras one by one)               __|\n'
	      '|__       Choose the resolution for the active camera     __|\n'
	      '|__       1 - 160x120                                     __|\n'
	      '|__       2 - 320x240   Recommended for FS camera         __|\n'
	      '|__       3 - 640x480                                     __|\n'
	      '|__       4 - 800x600                                     __|\n'
	      '|__       5 - 1280x720                                    __|\n'
	      '|__                                                       __|\n'
	      '|__   b - Back to Settings Screen                         __|\n'
	      ' |_________________________________________________________|\n')

##########################################	N E W L O G 	S C R E E N  ###############################################

class NewLogScreen(Cmd):

	command = ''
	def do_y(self, args):
		''' Creating a New Log. '''
		timeNow = '_'.join(str(datetime.now()).split('.')[0].split())

		with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as fConfig:
			config =  RStrip(fConfig.read())

		newLogName = config + '_' + timeNow + '.txt'
		with open(iuBaseDir + '/DB/Setup/CurrentLog.txt', 'w') as fCurrentLog:
			fCurrentLog.write(newLogName)

		print('- New log name is: ' + newLogName)
	
		with open(iuBaseDir + '/' + newLogName, 'w') as fCurrentLog:
			fCurrentLog.write('')
			newlog_screen()

		# takes to main screen
		self.command = 'b'
		return True
		
	def do_n(self,args):
		''' Not Creating a New Log. Takes You to the Main Screen '''
		# takes to main screen
		self.command = 'b'
		return True

def newlog_screen():
	os.system('clear')

	print(' ___________________________________________________ \n'
	      '|____             CREATE NEW LOG                ____|\n'
	      '|                                                   |\n'
	      '|__     Do You want to create a New Log? (y/n)    __|\n'
	      ' |_________________________________________________|\n\n')


#************************************************************************************************************************
#************************************************************************************************************************

##########################################	C O N F I G 	S C R E E N  ###############################################

class ConfigScreen(Cmd):

	command = ''

	def do_b(self, args):
		''' Back to the Main Screen. '''
		self.command = 'b'
		return True

	def do_r(self, args):
		''' Refreshes the screen.'''
		config_screen()

	def do_1(self, args):
		''' Changes the config to INTEROP '''
		with open(iuBaseDir + '/DB/Setup/Config.txt', 'w') as fConfig:
			fConfig.write('INTEROP')
		# takes to main screen
		self.command = 'b'
		return True

	def do_2(self, args):
		''' Changes the config to BACKWARDS '''
		with open(iuBaseDir + '/DB/Setup/Config.txt', 'w') as fConfig:
			fConfig.write('BACKWARDS')
		# takes to main screen
		self.command = 'b'
		return True

def config_screen():
	os.system('clear')
	with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as fConfig:
		config =  RStrip(fConfig.read())
	
	print(' __________________________________________________________ \n'
          '|_____               CHANGE CONFIG NAME              ______|\n'
	      '|                                                          |\n'
	      '|_  The current config is ' + config + ' ' * (32 - len(str(config))) + '_|\n'
	      '|_                                                        _|\n'
	      '|_   You can overwrite the config                         _|\n'
	      '|_  with the following options                            _|\n'
	      '|_                                                        _|\n'
	      '|_  1 - INTEROP       2 - BACKWARDS                       _|\n'
	      '|_                                                        _|\n'
	      '|_  b - Back to the Main Screen                           _|\n'
	      ' |________________________________________________________|\n\n')
