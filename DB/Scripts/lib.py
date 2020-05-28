#!/usr/bin/env python3
#=== lib.py ===#

import subprocess
import os
import re

iuBaseDir = os.environ['IUBASEDIR']

def Speed(arg):

	if arg == '1.5':
		return 'ls'
	elif arg == '12':
		return 'fs'
	elif arg == '480':
		return 'hs'
	elif arg == '5000':
		return 'ss'
	elif arg == '10000':
		return 'ssp'
	return ''

def BCDusb(m, devList):
	for line in devList:
		if m in line:
			return line.split()[-1]
	return ''

def GetDevices():
	busName = ''
	devName = ''
	devSpeed = ''
	busDeviceSpeedList = ['']
	res = ''

	outCMD = subprocess.run(['lsusb', '-v'], stdout=subprocess.PIPE)

	devListForDevCheck = subprocess.run(['lsusb'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')

	out = outCMD.stdout.decode('utf-8').split('\n')

	lsUSBm = subprocess.run(['lsusb', '-t'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
	
	for line in lsUSBm:

		match = re.search('.*Bus\s(\d+).*', line)
		if str(match) != 'None':
			busName = 'Bus ' + '0' * (3 - len(match.group(1))) + match.group(1)

		match = re.search('.*Dev\s(\d+).*', line)
		if str(match) != 'None':
			devName = 'Device ' + '0' * (3 - len(match.group(1))) + match.group(1)

		match1 = re.search('.*(,\s\d+)M$', line)
		match2 = re.search('.*(,\s\d+\.\d+)M$', line)
		
		if str(match1) != 'None':
			devSpeed = Speed(match1.group(1)[2:])
		if str(match2) != 'None':
			devSpeed = Speed(match2.group(1)[2:])

		busDeviceSpeedList.append(busName + ' ' + devName + ' ' + devSpeed)

	found = False
	result = ''
	devList = ['']

	for line in out:
		if 'Bus' in line and 'Device' in line:
			found = True
			idVendorProduct = line.split()[5]
			devSpeed = BCDusb(line[0:18], busDeviceSpeedList)
		if found:
			if 'iProduct' in line:
				iProduct = ' '.join(line.split()[2:])
			if 'bInterfaceClass' in line:
				bInterfaceClass = ' '.join(line.split()[2:])
			if 'bInterfaceSubClass' in line:
				bInterfaceSubClass = ' '.join(line.split()[2:])
			if 'bInterfaceProtocol' in line:
				bInterfaceProtocol = ' '.join(line.split()[2:])
				result = idVendorProduct + '<=>' + iProduct + '<=>' + devSpeed + '<=>' + bInterfaceClass + '<=>' + bInterfaceSubClass + '<=>' + bInterfaceProtocol + '\n'
				devList.append(result)
				found = False

	devList.sort()

	with open(iuBaseDir +'/DB/Setup/DetectedDevices.txt', 'w') as file:
		for element in devList:
			file.write(element)
	devListForDevCheck.sort()
	with open(iuBaseDir +'/DB/Setup/DevCheckDetected.txt', 'w') as file:
		for element in devListForDevCheck:
			file.write(element[0:7] + element[22:] + '\n')

def DetectDevices():
	GetDevices()
	GetDevicesCount()

def ApplyDevices():
	os.system('cp ' + iuBaseDir + '/DB/Setup/DetectedDevices.txt ' + iuBaseDir + '/DB/Setup/AppliedDevices.txt')
	os.system('cp ' + iuBaseDir + '/DB/Setup/DetectedDevicesCount.txt ' + iuBaseDir + '/DB/Setup/AppliedDevicesCount.txt')
	os.system('cp ' + iuBaseDir + '/DB/Setup/DevCheckDetected.txt ' + iuBaseDir + '/DB/Setup/DevCheckApplied.txt')
	os.system('cp ' + iuBaseDir + '/DB/Setup/DetectedConfig.txt ' + iuBaseDir + '/DB/Setup/AppliedConfig.txt')

def GetDevicesForDeviceCheck():
	devListForDevCheck = subprocess.run(['lsusb'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
	devListForDevCheck.sort()
	with open(iuBaseDir + '/DB/Setup/DevCheckDetected.txt', 'w') as file:
		for element in devListForDevCheck:
			file.write(element[0:7] + element[22:] + '\n')

def DeviceCheck():
	a = ''
	b = ''

	with open(iuBaseDir + '/DB/Setup/DevCheckDetected.txt', 'r') as f:
		a += f.read()
	with open(iuBaseDir + '/DB/Setup/DevCheckApplied.txt', 'r') as f:
		b += f.read()
	if a == b:
		return True
	return False

import copy
def EMDevice():
	with open(iuBaseDir + '/DB/Setup/DetectedDevices.txt', 'r') as file1:
		list1 = file1.read().split('\n')

	with open(iuBaseDir + '/DB/Setup/AppliedDevices.txt', 'r') as file2:
		list2 = file2.read().split('\n')

	checkList = copy.deepcopy(list1)

	for line in checkList:
		if line in list2:
			del list1[list1.index(line)]
			del list2[list2.index(line)]

	if not len(list1) == 0:
		index = 1
		print('Extra Devices:')
		for line in list1:
			l = line.split('<=>')
			print('\t', str(index), ':::', l[-3], l[-4])
			index += 1
	if not len(list2) == 0:
		index = 1
		print('Missing Devices:')
		for line in list2:
			l = line.split('<=>')
			print('\t', str(index), ':::', l[-3], ' - ', l[-4])
			index += 1

def GetDevicesCount():
	dev_qnt = { 'ssp Hub': 0,
		    'ss Hub': 0,
		    'hs Hub': 0,
		    'fs Hub': 0,
		    'Video': 0,
		    'Mass Storage': 0,
		    'Human Interface Device': 0,
		    'DisplayLink': 0, # 17e9
		    'Headset': 0,
		    'ssp Device': 0,
		    'ss Device': 0, }

	total = 0

	with open(iuBaseDir +'/DB/Setup/DetectedDevices.txt', 'r') as file:
		for line in file:
			total += 1

			spd = line.split('<=>')[2]

			if 'Video' in line:
				dev_qnt['Video'] += 1
			if 'Mass Storage' in line:
				dev_qnt['Mass Storage'] += 1
			if 'Human Interface Device' in line:
				dev_qnt['Human Interface Device'] += 1
			if '17e9' in line:
				dev_qnt['DisplayLink'] += 1
			if 'Headset' in line:
				dev_qnt['Headset'] += 1

			if 'Hub' in line or 'hub' in line:
				if  spd == 'ssp':
					dev_qnt['ssp Hub'] += 1
				if  spd == 'ss':
					dev_qnt['ss Hub'] += 1
				if  spd == 'hs':
					dev_qnt['hs Hub'] += 1
				if  spd == 'fs':
					dev_qnt['fs Hub'] += 1
			else:
				if  spd == 'ssp':
					dev_qnt['ssp Device'] += 1
				if  spd == 'ss':
					dev_qnt['ss Device'] += 1

	with open(iuBaseDir + '/DB/Setup/DetectedDevicesCount.txt', 'w') as file:
		file.write(str(dev_qnt['ssp Device']) + '\n')	
		file.write(str(dev_qnt['ss Device']) + '\n')
		file.write(str(dev_qnt['ssp Hub']) + '\n')
		file.write(str(dev_qnt['ss Hub']) + '\n')
		file.write(str(dev_qnt['hs Hub']) + '\n')
		file.write(str(dev_qnt['fs Hub']) + '\n')
		file.write(str(dev_qnt['Mass Storage']) + '\n')
		file.write(str(dev_qnt['Human Interface Device']) + '\n')
		file.write(str(dev_qnt['Video']) + '\n')
		file.write(str(dev_qnt['DisplayLink']) + '\n')
		file.write(str(total))
		file.close()
