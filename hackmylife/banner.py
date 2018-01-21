
#!/usr/bin/python

import os
import sys
import textwrap
import socket
try:
	import geocoder
except:
	print 'Geocoder is required ... See help page for installing'
from datetime import datetime

# FrankenLine Banner

print "-" * 50
print "-" * 50
banner = "\n\n 	 FrankenLine\n\n "
print banner.upper()
print "-" * 50
print "-" * 50

the_IP = raw_input('\nWhat is the IP/Hostname?' + ' ' + '[+]' + ' ') # the originating IP

print "\n[+] %s \n" % the_IP
print "-" * 50

print "[+] Scan"
print "[+] DNS Check" 						# The continuing options
print "[+] Locate"
print "[+] More Options..."
print "[+] Help"
print '-' * 50

next_step = raw_input('[+] ')  			

def help():
	print '-' * 50
	print """\n 
	
Welcome to FrankenLine! 
	

A pentesting framework built for surveillance and locating.
The first option are Scan, Check DNS and Locate.
To use the tools, just type out scan, dns or locate and the process will begin.
HOWEVER, you will need to download geocoder, by running the script below

sudo pip install geocoder

Remember, this is a beginner's pentesting framework. You will make a lot of noise, so be careful....

Happy Hacking
\n"""

	print "-" * 50

def dns():				# Checking DNS
	fqdn = socket.gethostbyaddr(the_IP)
	hostname1 = socket.gethostbyname(the_IP)
	name_ex = socket.gethostbyname_ex(the_IP)

	print "-" * 50
	print "\n[+] Checking DNS of %s...\n" % the_IP
	print "-" * 50

	print "[+]", fqdn
	print "[+]", hostname1
	print "[+]", name_ex
	print "-" * 50
	print "\n[+] Complete"


def locate():			# Locating
	
	loc = geocoder.freegeoip(the_IP)
	print "-" * 50
	print "\n[+] Locating %s ... \n" % the_IP
	print "-" * 50
	print "[+]", loc.json
	print "-" * 50
	print "[+] Complete\n"


def pscan():
	socket_IP = socket.gethostbyname(the_IP)

	print "-" * 50
	print "\n[+] Scanning %s ... \n" % the_IP 
	print "-" * 50
	
	t1 = datetime.now()
	try:
		for port in range(22):
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = sock.connect_ex((socket_IP,port))
			if result == 0:
				print "Port{}: \t Open".format(port)
			sock.close()
	except KeyboardInterrupt:
		print "\n[+] Canceling...\n"
		sys.exit()
	except socket.error:
		print "Couldn't connect to server..."
		sys.exit()
	t2 = datetime.now()
	total = t2 - t1

	print "Scan Completed in: ", total

def more_options():
	print "-" * 50
	print "[+] Payload Creator"
	print "[+] Backdoor"
	print "[+] Packet Sniffer"
	print "-" * 50
	more_options_next_step = raw_input("[+] ")
	if more_options_next_step == "Payload" or more_options_next_step == "payload" or more_options_next_step == 1:
		print "-" * 50
		print "Welcome to Payload Creator!\n"
		print "Coming Soon...."
	if more_options_next_step == "Backdoor" or more_options_next_step == "backdoor" or more_options_next_step == 2:
		print "-" * 50
		print "Welcome to the Backdoor Creator\n"
		print "Coming Soon...."
	if more_options_next_step == "Packet Sniffer" or more_options_next_step == "packet" or more_options_next_step == "sniffer" or more_options_next_step == 3:
		print "-" * 50
		print "Welcome to the Packet Sniffer\n"
		print "Coming Soon...."

if next_step == "help" or next_step == "Help":
	help()
if next_step == "Scan" or next_step == "scan" or next_step == 1:
	pscan()
if next_step == "Check DNS" or next_step == "check dns" or next_step == "dns" or next_step == "DNS" or next_step == 2:
	dns()
if next_step == "Locate" or next_step == "locate" or next_step == 3:
	locate()
if next_step == "More Options" or next_step == "more options" or next_step == "more":
	more_options()
if next_step == "Cancel" or next_step == "cancel" or next_step == "exit":
	print "\n[+]Bye for now...\n"
	sys.exit()
