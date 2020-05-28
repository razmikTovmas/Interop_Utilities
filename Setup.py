#!/usr/bin/env python3
#=== Setup.py ===#

import os

iuBaseDir = os.environ['IUBASEDIR']

os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/setup.py"')

