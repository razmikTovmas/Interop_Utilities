#!/usr/bin/env python3
#=== build_file.py ===#

import os
import sys
import time

iuBaseDir = os.environ['IUBASEDIR']

fileSizeName = sys.argv[1] # Name and MB

#=== Set title of terminal
print('\33]0;Build Zip\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=5, cols=50))
#===

os.system('clear')
print('\033[1;40;33mBuilding .zip file. fileName: ' + fileSizeName + 'MB.zip')
print('...')

#		MB		 1MB = xb
#dd bs=1024 count=1048576 </dev/urandom >myfile 
os.system('dd bs=' + fileSizeName + ' count=1048576 </dev/urandom >DB/Files/' + fileSizeName + 'MB.zip')
