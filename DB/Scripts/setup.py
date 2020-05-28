#!/usr/bin/env python3
#=== setup.py ===#

import console
import os
import sys
from cmd import Cmd

#=== Set title of terminal
print('\33]0;Setup\a', end='', flush=True)
#=== Change size of terminal
sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=37, cols=72))
#===

def launch_main():
	prompt = console.MainScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.main_screen()) 	#'Starting prompt...')


	if (prompt.command == 'alt'):
		launch_alt()
	elif (prompt.command == 's'):
		launch_settings()
	elif (prompt.command == 'n'):
		launch_newlog()
	elif (prompt.command == 'c'):
		launch_config()
			

def launch_alt():
	prompt = console.AltScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.alt_screen()) 	#'Starting prompt...')

	if(prompt.command == 'b'):
		launch_main()


def launch_settings():
	prompt = console.SettingsScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.settings_screen()) 	#'Starting prompt...')

	if(prompt.command == 'b'):
		launch_main()
	if(prompt.command == 'w'):
		launch_webcam()

def launch_webcam():
	prompt = console.WebcamScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.webcam_screen())

	if(prompt.command == 'b'):
		launch_settings()

def launch_newlog():
	prompt = console.NewLogScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.newlog_screen())

	if(prompt.command == 'b'):
		launch_main()

def launch_config():
	prompt = console.ConfigScreen()
	prompt.prompt = '>> '
	prompt.cmdloop(console.config_screen())

	if(prompt.command == 'b'):
		launch_main()

if __name__ == '__main__':
	launch_main()
	
	print("Thanks for using our console application")
