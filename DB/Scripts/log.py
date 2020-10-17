#!/usr/bin/env python3
#=== log.py ===$

import os
import sys
import subprocess
from datetime import datetime


iuBaseDir = os.environ['IUBASEDIR']

def switchEnable(option):
    if option == 'YES':
        return 'ENABLE'
    else:
        return 'DISABLE'

def RStrip(string):
    if string.rstrip() == '':
        return 'notSet'
    else:
        return string.rstrip()


if __name__ == '__main__':
    timeStamp = str(datetime.now()).split()[1][0:-4]

    with open(iuBaseDir + '/DB/Setup/CurrentLog.txt', 'r') as fCurrentLogName:
        currentLogName = RStrip(fCurrentLogName.read())

    fCurrentLog = open(iuBaseDir + '/' + currentLogName, 'a')

    if (sys.argv[1] == 'startnormal'):
        with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as fConfig:
            config = fConfig.read().split()[0]
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=           Starting Test          =\n')
        if (config == 'INTEROP'):
            fCurrentLog.write('=         Config: INTEROP          =\n')
        elif (config == 'BACKWARDS'):
            fCurrentLog.write('=         Config: BACKWARDS        =\n')
        else:
            fCurrentLog.write('=         Config:  N/A             =\n')

        fCurrentLog.write('==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'sleep'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=        Entering Sleep  (S3)      =\n'
                          '==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'hibernate'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=      Entering Hibernate (S4)     =\n'
                          '==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'warmboot'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=        Entering Warm Boot        =\n'
                          '==                                ==\n'
                          '====================================\n\n')


    elif (sys.argv[1] == 'coldboot'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=        Entering Cold Boot        =\n'
                          '==                                ==\n'
                          '====================================\n\n')


    elif (sys.argv[1] == 'stop'):
        messType = 0
        if (sys.argv[2] == 'stopping'):
            fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                              '==                                ==\n'
                              '=               Test               =\n'
                              '=             STOPPING             =\n'
                              '==                                ==\n'
                              '====================================\n\n')

        elif (sys.argv[2] == 'stopped'):
            fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                              '==                                ==\n'
                              '=               Test               =\n'
                              '=             STOPPED              =\n'
                              '==                                ==\n'
                              '====================================\n\n')

        elif (sys.argv[2] == 'killed'):
            fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                              '==                                ==\n'
                              '=               Test               =\n'
                              '=              KILLED              =\n'
                              '==                                ==\n'
                              '====================================\n\n')

    elif (sys.argv[1] == 'transfer'):
        if (sys.argv[2] == 'stop'):
            if (sys.argv[3] == 'stopping'):
                fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                                  '==                                ==\n'
                                  '=         File  Transfers          =\n'
                                  '=             STOPPING             =\n'
                                  '==                                ==\n'
                                  '====================================\n\n')
            elif (sys.argv[3] == 'stopped'):
                fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                                  '==                                ==\n'
                                  '=         File  Transfers          =\n'
                                  '=             STOPPED              =\n'
                                  '==                                ==\n'
                                  '====================================\n\n')
            elif (sys.argv[3] == 'killed'):
                fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                                  '==                                ==\n'
                                  '=         File  Transfers          =\n'
                                  '=              KILLED              =\n'
                                  '==                                ==\n'
                                  '====================================\n\n')
        else:
            if (sys.argv[2] == 'pass'):
                message = 'Copy Completed Succesfully: '
            elif (sys.argv[2] == 'fail'):
                if (sys.argv[8] == 'setup'):
                    message = 'Copy Failed during Setup Stage: '
                elif (sys.argv[8] == 'transfer'):
                    message = 'Copy Failed During Transfer Stage: '
                elif (sys.argv[8] == 'dataint'):
                    if (sys.argv[9] == '0'):
                        message = 'Couldn\'t Check Data Integrity: '
                    elif (sys.argv[9] == '1'):
                        message = 'Failed Data Integrity Check: '

            transferInfo = 'from ' + sys.argv[3] + ' to ' + sys.argv[4] + ' File Size: ' + sys.argv[5] + ' Loop Count: ' + sys.argv[6] + ' Failed: ' + sys.argv[7] + ' ---\n'
            fCurrentLog.write('---   Timestamp: ' + timeStamp + ' ' +  message + transferInfo + '\n')

    elif (sys.argv[1] == 'cameras'):

        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=        Operating Cameras         =\n')
        if (sys.argv[2] == 'auto'):
            fCurrentLog.write('=        Configuration: AUTO       =\n' )
        elif (sys.argv[2] == 'manual'):
            fCurrentLog.write('=        Configuration: MANUAL     =\n' )
        else:
            fCurrentLog.write('=        Configuration:  N/A       =\n')

        fCurrentLog.write('==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'devicecheck'):
        if (sys.argv[2] == 'pass'):
            fCurrentLog.write('---   Timestamp: ' + timeStamp + ' Device Check: PASS\n\n')
        elif (sys.argv[2] == 'fail'):
            fCurrentLog.write('---   Timestamp: ' + timeStamp + ' Device Check: FAIL\n\n')

    elif (sys.argv[1] == 'video'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=            Playing VIDEO         =\n'
                          '==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'music'):
        fCurrentLog.write('====== Timestamp: ' + timeStamp + ' ======\n'
                          '==                                ==\n'
                          '=            Playing MUSIC         =\n'
                          '==                                ==\n'
                          '====================================\n\n')

    elif (sys.argv[1] == 'setup'):
        with open(iuBaseDir + '/DB/Setup/AppliedDevicesCount.txt', 'r') as fAppliedCount:
            SSP_AppliedDevCount         = RStrip(fAppliedCount.readline())
            SS_AppliedDevCount          = RStrip(fAppliedCount.readline())
            SSP_AppliedHubCount         = RStrip(fAppliedCount.readline())
            SS_AppliedHubCount          = RStrip(fAppliedCount.readline())
            HS_AppliedHubCount         = RStrip(fAppliedCount.readline())
            FS_AppliedHubCount         = RStrip(fAppliedCount.readline())
            MSC_AppliedDevCount        = RStrip(fAppliedCount.readline())
            HID_AppliedDevCount         = RStrip(fAppliedCount.readline())
            WebCam_AppliedDevCount         = RStrip(fAppliedCount.readline())
            DisplayLink_AppliedDevCount = RStrip(fAppliedCount.readline())
            Total_AppliedDevCount         = RStrip(fAppliedCount.readline())

        with open(iuBaseDir + '/DB/Setup/DriveLetters.txt', 'r') as fDriveLetters:
            driveLetters = RStrip(fDriveLetters.read())

        with open(iuBaseDir + '/DB/Setup/Config.txt', 'r') as fConfig:
            Config = RStrip(fConfig.read())

        with open(iuBaseDir + '/DB/Setup/LoopTransfersEn.txt', 'r') as fLoopTransferEn:
            LoopTransfersEn = switchEnable(RStrip(fLoopTransferEn.read()))

        with open(iuBaseDir + '/DB/Setup/DeviceCheckEn.txt', 'r') as fDeviceCheckEn:
            DeviceCheckEn = switchEnable(RStrip(fDeviceCheckEn.read()))


        with open(iuBaseDir + '/DB/Setup/LargeFile.txt', 'r') as fLargeFile:
            LargeFile = RStrip(fLargeFile.read())

        with open(iuBaseDir + '/DB/Setup/SmallFile.txt', 'r') as fSmallFile:
            SmallFile = RStrip(fSmallFile.read())

        with open(iuBaseDir + '/DB/Setup/LoggingEn.txt', 'r') as fLoggingEn:
            LoggingEn = switchEnable(RStrip(fLoggingEn.read()))

        with open(iuBaseDir + '/DB/Setup/CameraAutoConfig.txt', 'r') as fCameraAutoConfig:
            CameraAutoConfig = switchEnable(RStrip(fCameraAutoConfig.read()))

        TransferMode = 'R/W'

        fCurrentLog.write('========================================================\n'
                          '     ------------------TEST SETUP------------------     \n'
                          '           ---   Timestamp: ' + timeStamp + '   ---\n\n'
                          '     Loop Transfers:            ' + LoopTransfersEn + '\n'
                          '     Device Check:              ' + DeviceCheckEn + '\n'
                          '     Large File Size:           ' + LargeFile + 'MB\n'
                          '     Small File Size:           ' + SmallFile + 'MB\n'
                          '     Logging:                   ' + LoggingEn + '\n'
                          '     File Transfer Mode:        ' + TransferMode + '\n'
                          '     Camera Auto Config:        ' + CameraAutoConfig + '\n\n'
                          '     Drive Letters:             ' + driveLetters + '\n\n'
                          '     Number of SS+ Devices:     ' + SSP_AppliedDevCount + '\n'
                          '     Number of SS Devices:      ' + SS_AppliedDevCount + '\n'
                          '     Number of SS+ Hubs:        ' + SSP_AppliedHubCount + '\n'
                          '     Number of SS Hubs:         ' + SS_AppliedHubCount + '\n'
                          '     Number of HS Hubs:         ' + HS_AppliedHubCount + '\n'
                          '     Number of FS Hubs:         ' + FS_AppliedHubCount + '\n'
                          '     Number of MSC Devices:     ' + MSC_AppliedDevCount + '\n'
                          '     Number of HID Devices:     ' + HID_AppliedDevCount + '\n'
                          '     Number of Webcams:         ' + WebCam_AppliedDevCount + '\n'
                          '     Number of DisplayLink:     ' + DisplayLink_AppliedDevCount + '\n'
                          '     Total Number Devices:      ' + Total_AppliedDevCount + '\n\n'
                          '     Configuration:             ' + Config + '\n\n'
                          '========================================================\n\n')

    fCurrentLog.close()
