#!/usr/bin/env python3
#=== Start.py ===#

import os

iuBaseDir = os.environ['IUBASEDIR']

os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/DB/Scripts/start.py"')

