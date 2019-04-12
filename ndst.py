import sys
import io
from contextlib import redirect_stdout
import subprocess
def shexec(x):
      return subprocess.check_output(x, shell=True, stderr=True).decode('utf-8')
def usb_nocut():
      usb = shexec("lsusb")[:-1].split('\n')
      x = 0
      no_id = ''
      while(x<int(len(usb))-1):
            line = usb[x]
            sep_id = line.split('ID')
            no_id  = sep_id[0] + sep_id[1][11:] + '\n' + no_id
            x = x + 1
      usb = no_id[:-1]
      return usb

def usb_cut():
       usb = shexec("lsusb | cut -d ' '  -f 1-4,7-")
       return usb
 
def neo_nocut():
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
            
def neo_cut():
      neolist1 = shexec("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --memory_percent on | cut -d ':' -f 1").split('\n')
      width = 20
      iterator = 2
      neolist2 = shexec("neofetch --gtk2 off --gtk3 off --refresh_rate on --disable wm de --cpu_cores physical --stdout --memory_percent on | cut -d ':' -f 2").split('\n')
      print(neolist1[0]  + '\n' +  neolist1[1]) ##first 2 lines
      while(iterator<len(neolist2)-2):
            line = neolist1[iterator] + ':'.ljust(width - len(neolist1[iterator])) + neolist2[iterator]
            print(line)
            iterator+=1
            
cpu  = shexec("lscpu").split('\n')
cpu = (cpu[2] + '\n' + cpu[15] + '\n' + cpu[16] + '\n' + cpu[17] + '\n' + cpu[19] + '\n')
disk = shexec('df -hl')
date = shexec('date')
try:
      if sys.argv[1] == '--no-cut':
            print('--nocut mode active')
            f = io.StringIO()
            with redirect_stdout(f):
                  neo_nocut()
            x = f.getvalue()
            payload = x + cpu + 'Date: ' + date + 'Disk Usage: \n' + disk + 'USB Devices: \n' + usb_nocut()
            print(payload)
            term = input('log to dpaste? (requires cURL)')
            if term == 'yes':
                  x = shexec("curl -s -F \"content=" + payload + '\" http://dpaste.com/api/v2/')
                  print("URL: " + x)
      if sys.argv[1] == '--no-neo':
            payload = str(cpu) + '\nDate: ' + date + 'Disk Usage:\n' + disk + str(usb_cut())
            print(payload)
      if sys.argv[1] == '--no-deps':
            payload_nocut = cpu + 'Date: ' + date + 'Disk Usage: \n' + disk + 'USB Devices: \n' + usb_nocut()
            print(payload_nocut)
      elif sys.argv[1] == '--help':
            print('ndst - a tool to get system info. run with --no-deps for usage without neofetch or cut, or --no-cut for if you just dont have cut for some reason')
      else:
            print('invalid args')
except IndexError:
     f = io.StringIO()
     with redirect_stdout(f):
           neo_nocut()
           x = f.getvalue()
     payload = str(x) + str(cpu) + 'Date: ' + date + 'Disk Usage:\n' + disk + str(usb_cut())
     print(payload)
     term = input('log to dpaste? (requires cURL)')
     if term == 'yes':
            x = shexec("curl -s -F \"content=" + payload + '\" http://dpaste.com/api/v2/')
            print("URL: " + x)
