import sys
from subprocess import run
import subprocess
cpu  = run("lscpu", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
cpu = (cpu[2] + '\n' + cpu[15] + '\n' + cpu[16] + '\n' + cpu[17] + '\n' + cpu[19] + '\n' + cpu[20] + '\n' + cpu[21] + '\n' + cpu[22] + '\n' + cpu[23] + '\n')[:-1]

#NEOBEGIN
neo = run("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --memory_percent on", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2].split('\n')
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
