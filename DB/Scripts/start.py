#!/usr/bin/env python3
#=== start.py ===#

import os
import sys
from cmd import Cmd

iuBaseDir = os.environ['IUBASEDIR']

#=== Set title of terminal
print('\33]0;Start\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=18, cols=33))
#===

def launch_controls():
    prompt = ControlsScreen()
    prompt.prompt = '>> '
    prompt.cmdloop(controls_screen())

    if prompt.command == 'o':
        launch_other()

def launch_other():
    prompt = OtherScreen()
    prompt.prompt = '>> '
    prompt.cmdloop(other_screen())

    if prompt.command == 'b':
        launch_controls()

class ControlsScreen(Cmd):
    def do_1(self, args):
        ''' Start Normal '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/StartNormal.py"')
        controls_screen()

    def do_2(self, args):
        ''' Sleep '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/Sleep.py"')
        controls_screen()

    def do_3(self, args):
        ''' Hibernate '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/Hibernate.py"')
        controls_screen()

    def do_4(self, args):
        ''' Warm Boot '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/BootWarm.py"')
        controls_screen()

    def do_5(self, args):
        ''' Cold Boot '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/BootCold.py"')
        controls_screen()

    def do_6(self, args):
        ''' Stop '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/Stop.py"')
        controls_screen()

    def do_o(self, args):
        ''' Other Tools Screen '''
        self.command = 'o'
        return True

    def do_q(self, args):
        ''' Exit '''
        exit()
    def do_r(self, args):
        ''' Refresh '''
        controls_screen()

class OtherScreen(Cmd):
    def do_1(self, args):
        ''' File Transfers '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/FileTransfers.py"')
        other_screen()

    def do_2(self, args):
        ''' Stop File Transfers '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/StopFileTransfers.py"')
        other_screen()

    def do_3(self, args):
        ''' Operate Cameras '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Cameras.py"')
        other_screen()

    def do_4(self, args):
        ''' Device Check '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/DeviceCheck.py"')
        other_screen()

    def do_5(self, args):
        ''' Video '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Video.py"')
        other_screen()

    def do_6(self, args):
        ''' Music '''
        os.system('gnome-terminal -e "python3 ' + iuBaseDir + '/Controls/OtherTools/Music.py"')
        other_screen()

    def do_b(self, args):
        ''' Controls Screen '''
        self.command = 'b'
        return True

    def do_q(self, args):
        ''' Exit '''
        exit()

    def do_r(self, args):
        ''' Refresh '''
        other_screen()


def controls_screen():
    os.system('clear')
    print(' _______________________________\n'
          '|______                   ______|\n'
          '|____       Controls        ____|\n'
          '|__                           __|\n'
          '|__     1 - Start Normal      __|\n'
          '|__     2 - Sleep             __|\n'
          '|__     3 - Hibernate         __|\n'
          '|__     4 - Warm Boot         __|\n'
          '|__     5 - Cold Boot         __|\n'
          '|__     6 - Stop              __|\n'
          '|__                           __|\n'
          '|____   o - Other Tools     ____|\n'
          '|____  r - Refresh Screen   ____|\n'
          '|______    q - Quit       ______|\n'
          '  |___________________________|\n\n')

def other_screen():
    os.system('clear')
    print(' _______________________________\n'
          '|______                   ______|\n'
          '|____      Other Tools      ____|\n'
          '|__                           __|\n'
          '|__  1 - File Transfers       __|\n'
          '|__  2 - Stop File Transfers  __|\n'
          '|__  3 - Cameras              __|\n'
          '|__  4 - Device Check         __|\n'
          '|__  5 - Video                __|\n'
          '|__  6 - Music                __|\n'
          '|__                           __|\n'
          '|__  b - Back To Main Screen  __|\n'
          '|____   r - Refresh Screen  ____|\n'
          '|______     q - Quit      ______|\n'
          '  |___________________________|\n\n')

if __name__ == '__main__':

    launch_controls()

    print("Thanks for using our console application")
