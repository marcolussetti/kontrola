<<<<<<< HEAD
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
#remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServer    = 'lnxvmpccryerd01'
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
port_list = [22, 80, 443, 8443, 646]

#for port_number in port_list:
#    print port_number

# We also put in some error handling for catching errors

try:
    #for port in range(1,1025):
    #for port in range(port_list):
    for port_number in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port_number))
        if result == 0:
            print "Port {}: 	 Open".format(port_number)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
||||||| merged common ancestors
=======
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
#remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServer    = '127.0.0.1'
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
port_list = [22, 80, 443, 8443, 646]

#for port_number in port_list:
#    print port_number

# We also put in some error handling for catching errors

try:
    #for port in range(1,1025):
    #for port in range(port_list):
    for port_number in port_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port_number))
        if result == 0:
            print "Port {}: 	 Open".format(port_number)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
>>>>>>> d13cbc05b61bb4ec7d60f1bc017c6891c9fa5bbd
