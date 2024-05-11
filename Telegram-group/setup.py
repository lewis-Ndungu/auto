#!/bin/env python3

'''
Dear programmer:
When I wrote this code, only God and
I knew how it worked.
Now, only God knows it
Therefore, if you are trying to optimize
this routine and it fails (most surely),
please increase this counter as a
warning for the next person:
total hours wasted here = 11
'''

import os, sys
import time


def requirements():
	def csv_lib():
		print('['']'' this may take some time ...')
		os.system("""
			pip install cython numpy pandas
			python -m pip install cython numpy pandas
			""")
	print(' it will take upto 10 min to install csv merge.')
	input_csv = input(' do you want to enable csv merge (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print("[+] Installing requirements ...")
	os.system("""
		pip install telethon requests configparser
		python -m pip install telethon requests configparser
		touch config.data
		""")
	print("[+] requirements Installed.\n")


def config_setup():
	import configparser
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input("[+] enter api ID : ")
	cpass.set('cred', 'id', xid)
	xhash = input("[+] enter hash ID : ")
	cpass.set('cred', 'hash', xhash)
	xphone = input("[+] enter phone number : ")
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print("[+] setup complete !")

def merge_csv():
	import pandas as pd
	import sys
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(' merging '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(' big files can take some time ... ')
	merge = file1.merge(file2, on='First Name')
	merge.to_csv("output.csv", index=False)
	print('['']'' saved file as "output.csv"\n')

def update_tool():
	import requests as r
	source = r.get("../.image/.version")
	if source.text == '3':
		print('['']'' already latest version')
	else:
		print(' removing old files ...')
		os.system('rm *.py');time.sleep(3)
		print(' getting latest files ...')
		os.system();time.sleep(3)
		print('\n update completed.\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(' selected module : '+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(' selected module : '+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(' selected module : '+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		print("""$ python setup.py -m file1.csv file2.csv
			
	( --config  / -c ) setup api configuration
	( --merge   / -m ) merge 2 .csv files in one 
	( --update  / -u ) update tool to latest version
	( --install / -i ) install requirements
	( --help    / -h ) show this msg 
			""")
	else:
		print('\n'+' unknown argument : '+ sys.argv[1])
		print(' for help use : ')
		print('$ python setup.py -h'+'\n')
except IndexError:
	print('\n'+' no argument given : '+ sys.argv[1])
	print(' for help use : ')
	print(' https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use')
	print('$ python setup.py -h'+'\n')
