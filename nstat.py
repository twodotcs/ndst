import sys
from subprocess import run
import subprocess
distro = run('cat /etc/*release', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[0].split('"')[1]
ram = run('vmstat -s -S M', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
totram = int(ram.split('\n')[0].split('M')[0])
freeram = int(ram.split('\n')[1].split('M')[0])
ram_used = int(totram - freeram)
neo = run("neofetch --stdout", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
disk = run('df', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
user = run("whoami", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
uptime = run("uptime -p", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
date =run('date', shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
print(uptime)
print(distro)
print(user)
print(totram)
print(freeram)
print(neo)
print(disk)
print(date)
