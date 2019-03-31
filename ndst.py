import sys
from subprocess import run
import subprocess
def whitegen(n):
      x = ''
      while(len(x)<n):
            x = x + ' '
      return x

cpu  = run("lscpu", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
cpu = (cpu[2] + '\n' + cpu[15] + '\n' + cpu[16] + '\n' + cpu[17] + '\n' + cpu[19] + '\n' + cpu[20] + '\n' + cpu[21] + '\n' + cpu[22] + '\n' + cpu[23] + '\n')[:-1]
#NEOBEGIN
neo = run("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --memory_percent on", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2].split('\n')
print(neo[0]  + '\n' +  neo[1])
itr = 2
lst = []
while(itr<len(neo)):
      line = neo[itr]
      linelist = line.split(':')
      itt = 0
      while(itt<len(linelist)):
            lst.append(linelist[itt])
            itt = itt + 1
      itr = itr + 1
itr = 0
while(itr<len(lst)):  
      n = 21
      line = lst[itr] + ':' + lst[itr+1][1]
      x = 0 
      if len(line) != n:
            x = n - len(line)
            col = ':' + whitegen(x)
            line = lst[itr] + col + lst[itr+1]
            if(itr % 2 == 0):
                  print(line)
      itr = itr + 2
#NEOEND          
disk = run('df -hl', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
date = run('date', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
#USBBEGIN
usb = run("lsusb", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1].split('\n')
x = 0
no_id = ''
while(x<int(len(usb))-1):
      line = usb[x]
      sep_id = line.split('ID')
      no_id  = sep_id[0] + sep_id[1][11:] + '\n' + no_id
      x = x + 1
usb = no_id[:-1]
####USBEND
print(cpu)
print('Date: ' + date[:-1])
print('Disk Usage: \n' + disk[:-1])
print('USB Devices: \n' + usb)
