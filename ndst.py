import sys
from subprocess import run
import subprocess
def shexec(x):
      return run(x, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')

cpu  = shexec("lscpu").split('\n')
cpu = (cpu[2] + '\n' + cpu[15] + '\n' + cpu[16] + '\n' + cpu[17] + '\n' + cpu[19] + '\n' + cpu[20] + '\n' + cpu[21] + '\n' + cpu[22] + '\n' + cpu[23] + '\n')[:-1]
#NEOBEGIN
neo = shexec("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --memory_percent on")[:-2].split('\n')
print(neo[0]  + '\n' +  neo[1])
neolist = []
for iterator in range(0,len(neo)):
      line = neo[iterator]
      linelist = line.split(':')
      list_iter = 0
      if(iterator >= 2):
            while(list_iter<len(linelist)):
                  neolist.append(linelist[list_iter])
                  list_iter+=1      
iterator = 0
for iterator in range(0,len(neolist),2):
      width = 22
      line = neolist[iterator] + ':' + neolist[iterator+1][1]
      div = ':'.ljust(width - len(line))
      print(neolist[iterator] + div + neolist[iterator+1])
#NEOEND
disk = shexec('df -hl')
date = shexec('date')
#USBBEGIN
usb = shexec("lsusb")[:-1].split('\n')
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
