
# Python script to fetch system information
# Author -  ThePythonDjango.Com
# Tested with Python3 on Ubuntu 16.04
# 

import platform
import psutil
import os
import subprocess
import collections
import shutil




# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

#cpu usage
print('cpu usage')
mem=str(os.popen('free -t -m').read())
print(mem)

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)

# Load
with open("/proc/loadavg", "r") as f:
print("Average Load: " + f.read().strip())

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# uptime
uptime = None
with open("/proc/uptime", "r") as f:
uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")
#memory usage
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
print('memory use:', memoryUse)
#disk Usage
# Path 
path = "/home/"

# Get the disk usage statistics 
# about thinke given path 
stat = shutil.disk_usage(path) 

# Print disk usage statistics 
print("Disk usage statistics:") 
print(stat) 

#Network latency
import os, sys, pexpect, time, datetime

# # SET YOUR PING INTERVAL HERE, IN SECONDS
interval = 5

# # LOG TO WRITE TO WHEN PINGS TAKE LONGER THAN THE THRESHOLD SET ABOVE
i = datetime.datetime.now()
log_file = 'logs/latency-tester.' + i.strftime('%Y.%m.%d.%H.%M.%S') + '.log'

# SET YOUR PING RESPONSE TIME THRESHOLD HERE, IN MILLISECONDS
threshold = 250

# # WHO SHOULD WE RUN THE PING TEST AGAINST
ping_destination = 'www.facebook.com'

def write_to_file(file_to_write, message):
os.makedirs(os.path.dirname(file_to_write), exist_ok=True)
fh = open(file_to_write, 'a')
fh.write(message)
fh.close()     
count = 0
line = 'Ping Interval: ' + str(interval) + ', Destination: ' + ping_destination + ', Threshold to Log (msec): ' + str(threshold) + '\n'

write_to_file(log_file, line)
ping_command = 'ping -i ' + str(interval) + ' ' + ping_destination
print(line)

child = pexpect.spawn(ping_command)
child.timeout=1200

while 1:
line = child.readline()
if not line:
    break

if line.startswith(b'ping: unknown host'):
    print('Unknown host: ' + ping_destination)
    write_to_file(log_file, 'Unknown host: ' + ping_destination)
    break

if count > 0:
    ping_time = float(line[line.find(b'time=') + 5:line.find(b' ms')])
    line = time.strftime("%m/%d/%Y %H:%M:%S") + ": " + str(ping_time)
    print(str(count) + ": " + line)

    if ping_time > threshold:
        write_to_file(log_file, line + '\n')

count += 1	

