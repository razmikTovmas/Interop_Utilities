# Interop Utilities

Tool on Linux Ubuntu OS to assist in USB Interoperability and Backwards Compatibility testing.  
[Specification](https://www.usb.org/sites/default/files/3.1%20Interoperability%20Testing%20v0.95%20w%20USB%20Type-C.pdf)

## Plugins and additional software
**Please install the following packages before running the scripts**  
Make sure you have Python3 installed

```
sudo apt-get install gstreamer1.0-plugins_ugly
sudo apt-get install gstreamer1.0-plugins_bad
sudo apt-get install gstreamer1.0-libav
sudo apt-get install xdotool
sudo apt-get install v4l-utils
```

## For DisplayLink

First install the DKMS package
```
sudo apt-get install dkms
```

Then download the ubuntu driver, extract, and run the .run script to get the DisplayLink driver work.  
The Displaylink driver path is [here](http://www.displaylink.com/downloads/ubuntu).

## interop Utilities BaseDir

Add the following command in your .bashrc
```
export IUBASEDIR=<path to Interop_Utilities folder>
```
For example: 'export IUBASEDIR=~/Desktop/Interop_Utilities'

## Running the scripts

The scripts can be run in 2 ways - 'python3 <script_name>.py' or  './<script_name>.py'  

To use the scripts you will need to use only Start.py and Setup.py scripts which are located in the base directory.  

To setup the configuration details run the Setup.py script. It will open an interactive console application.For each screen some commands will be available to be chosen. If a command is unknown you can type 'help <command_name>' in the console. It will print short information about the command.

**NOTE:**
Check microphone inputs by searching 'sound' in the Ubuntu search bar, then open the Sound app. Click on the 'input' tab and pick a microphone.  

## Start.py

After completing the setup, you will need to run the Start.py script and choose an option. The Start.py console has 2 screens - the 'Controls Screen' and the 'Other screen'.  
Here is the 'Constrols Screen'.
```
 _______________________________
|______                   ______|
|____       Controls        ____|
|__                           __|
|__     1 - Start Normal      __|
|__     2 - Sleep             __|
|__     3 - Hibernate         __|
|__     4 - Warm Boot         __|
|__     5 - Cold Boot         __|
|__     6 - Stop              __|
|__                           __|
|____   o - Other Tools     ____|
|____  r - Refresh Screen   ____|
|______    q - Quit       ______|
  |___________________________|
```

Type the number which corresponds to the action you want to start, then press Enter. Type 'o' to view the 'Other Screen'.  
Here is the 'Other Screen'.
```
 _______________________________
|______                   ______|
|____      Other Tools      ____|
|__                           __|
|__  1 - File Transfers       __|
|__  2 - Stop File Transfers  __|
|__  3 - Cameras              __|
|__  4 - Device Check         __|
|__  5 - Video                __|
|__  6 - Music                __|
|__                           __|
|__  b - Back To Main Screen  __|
|____   r - Refresh Screen  ____|
|______     q - Quit      ______|
  |___________________________|
```

Type 'b' to go back to the Controls Screen, and 'q' to quit the script.

## Setup.py

Navigate through Setup.py script in the same way as shown above.

## Scripts Topology
```
./                                          # IUBASEDIR
├── Controls                                # Includes main scripts, can be run from Start.py, or in the terminal using the command 'python3 <script_name>' or './<script_name>'
│   ├── BootCold.py                         # Shuts down the system
│   ├── BootWarm.py                         # Restarts the system
│   ├── Hibernate.py                        # Stops all file transfers, then initiates hibernate
│   ├── Sleep.py                            # Stops all file transfers, then initiates sleep
│   ├── OtherTools                          # Main scripts used for Start Normal
│   │   ├── Cameras.py
│   │   ├── DeviceCheck.py
│   │   ├── FileTransfers.py
│   │   ├── Music.py
│   │   ├── StopFileTransfers.py
│   │   └── Video.py
│   ├── StartNormal.py                      # The main script to operate the interop tree
│   └── Stop.py                             # The script to stop all media/file transfers
├── DB
│   ├── Files
|   |   ├── <File Size>MB.zip               # Name of the file to be transfered
|   |   ├── ...                             # Can be several files like the previous one
│   ├── Media
│   │   ├── AudioFileName.txt               # Includes the name of the music file to be played, can be changed
|   |   ├── <Video File>                    # Video file to be played, (new video file must be added to this directory)
|   |   ├── <Music File>                    # Music file to be played, (new music file must be added to this directory)
│   │   └── VideoFileName.txt               # Includes the name of the video file to be played, can be changed s
│   ├── Scripts                             # Secondary scripts used by main scripts
│   │   ├── build_file.py
│   │   ├── camera.py
│   │   ├── clear.py
│   │   ├── console.py
│   │   ├── file_transfer.py
│   │   ├── lib.py
│   │   ├── log.py
│   │   ├── music.py
│   │   ├── setup.py
│   │   ├── start.py
│   │   └── video.py
│   ├── Setup                               # Setup files, contain information about applied and detected configurations' details
│   │   ├── AppliedDevicesCount.txt
│   │   ├── AppliedDevices.txt
│   │   ├── CameraAutoConfig.txt
│   │   ├── Camera.txt
│   │   ├── Config.txt
│   │   ├── CurrentLog.txt
│   │   ├── DetectedDevicesCount.txt
│   │   ├── DetectedDevices.txt
│   │   ├── DevCheckApplied.txt
│   │   ├── DevCheckDetected.txt
│   │   ├── DeviceCheckEn.txt
│   │   ├── DriveLetters.txt
│   │   ├── LargeFile.txt
│   │   ├── LoggingEn.txt
│   │   ├── LoopTransfersEn.txt
│   │   ├── SmallFile.txt
│   │   ├── Stopped.txt
│   │   └── stop.txt
│   ├── TerminalID
│   │   ├── DeviceCheck.txt
│   │   ├── FileTransfer.txt
│   │   ├── StopFT.txt
│   │   └── Stop.txt
│   └── Transfers
│       ├── Transfer<i>.txt                  # Contains information about the transfer status
│       └── ...                              # Can be several files like the previous one
├── <config_name>_<date>.txt                 # Log name, can be unlimited log files
├── README.txt                               # This file
├── Setup.py                                 # Setup script
└── Start.py                                 # Start script
```
