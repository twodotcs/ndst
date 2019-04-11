# NDST (ndt-stat)  
<img src="https://github.com/twodotcs/ndst/raw/master/ndst.png"></br>  
A metascript to get system info.  
all you need is:  
- python (>=3.5.2, lower might work)
- neofetch (whatever version stdout works in, test being implemented soon)  
- cut, can be run with --no-deps to avoid this. You probably have it.
- curl, for the uploading to dpaste. (optional)    
## Features
- lsusb (usb)
- lscpu (cpu)
- df (all disk usage)  
- uploads to dpaste  
- Sensors and stuff coming soon, when I can figure out how to parse them...  
## Why Python?
I don't know bash. Rewrite it yourself if you want to.
