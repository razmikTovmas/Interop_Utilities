#!/usr/bin/env python3
#=== Cameras.py ===#

import re
import os
import sys
import subprocess
import time

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;Cameras\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=6, cols=31))
#===

print('===============================\n'
      '==                           ==\n'
      '=      Operating Cameras      =\n'
      '==                           ==\n'
      '===============================')

time.sleep(1)


def DetectCameraSpeed(idVenPro, camName):
    with open(iuBaseDir + '/DB/Setup/AppliedDevices.txt', 'r') as f:
        for line in f:
            line = line.split('<=>')
            if idVenPro == line[0] or camName == line[1]:
                return line[2]

def OperateCamera(camLoc, camSpeed):
    full_width  = '320'
    full_height = '240'

    high_width  = '640'
    high_height = '480'

    ss_width    = '1280'
    ss_height   = '720'

    def_width   = full_width
    def_height  = full_height

    if camSpeed == 'fs':
        def_width  = full_width
        def_height = full_height
    elif camSpeed == 'hs':
        def_width  = high_width
        def_width  = high_height
    elif camSpeed == 'ss' or camSpeed == 'ssp':
        def_width  = ss_width
        def_height = ss_height

    os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/camera.py ' + camLoc + " " + def_width + " " + def_height + '"')

def OperateWithAutoConfig():
    proc = subprocess.Popen('v4l2-ctl --list-devices', shell=True, stdout=subprocess.PIPE,)
    output = proc.communicate()[0]
    output = output.decode("utf-8").split('\n\n')

    i     = 0
    cam_arr  = []
    camInfo  = []

    for i in range (len( output[:-1])):
        cam_arr.append(output[i].split())

        cam_match = re.search('^\((\w{4}:\w{4})\)$', cam_arr[i][-3])

        if str(cam_match) != 'None':
            camInfo.append([cam_match.group(1), ' '.join(cam_arr[i][0:-3]), cam_arr[i][-1], ''])
        else:
            camInfo.append(['None',' '.join(cam_arr[i][0:-2]), cam_arr[i][-1], ''])

    for j in range(len(camInfo)):
        camInfo[j][3] = DetectCameraSpeed(camInfo[j][0], camInfo[j][1])

        OperateCamera(camInfo[j][2], camInfo[j][3])
        time.sleep(1)

def OperateWithManualConfig():
    with open(iuBaseDir + '/DB/Setup/Camera.txt', 'r') as file:
        for line in file:
            os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/camera.py ' + line + '"')

#=== __main__ ===#

with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'r') as file:
    cameraAutoConfig = file.read().split()[0]

if 'YES' == cameraAutoConfig:
    #=== Log Helper ===#
    os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'cameras auto')
    #==
    OperateWithAutoConfig()
elif 'NO' == cameraAutoConfig:
    #=== Log Helper ===#
    os.system('python3 ' + iuBaseDir + '/DB/Scripts/log.py ' + 'cameras manual')
    #==
    OperateWithManualConfig()

