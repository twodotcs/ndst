import sys
from subprocess import run
import subprocess
distro = run('cat /etc/*release', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[0].split('"')[1]
ram = run('vmstat -s -S M', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
totram = int(ram.split('\n')[0].split('M')[0])
freeram = int(ram.split('\n')[1].split('M')[0])
ram_used = int(totram - freeram)
cpu  = run("lscpu", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
neo = run("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --shell_path on --memory_percent on", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-2]
disk = run('df -hl', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
user = run("whoami", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
uptime = run("uptime -p", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
date = run('date', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
#
usb = run("lsusb", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1].split('\n')
x = 0
no_id = ''
while(x<int(len(usb))-1):
      line = usb[x]
      sep_id = line.split('ID')
      no_id  = sep_id[0] + sep_id[1][11:] + '\n' + no_id
      x = x + 1
usb = no_id[:-1]
#
print(neo)
x = (cpu[2] + '\n' + cpu[15] + '\n' + cpu[16] + '\n' + cpu[17] + '\n' + cpu[19] + '\n' + cpu[20] + '\n' + cpu[21] + '\n' + cpu[22] + '\n' + cpu[23] + '\n')[:-1]
print(x)
print('Date: ' + date[:-1])
print('Disk Usage: \n' + disk[:-1])
print('USB Devices: \n' + usb)
