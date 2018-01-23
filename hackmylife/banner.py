#!/usr/bin/python

import os
import sys
import textwrap
import socket
try:
	import geocoder
except:
	print '\nGeocoder is required ... See help page for installing\n'
from datetime import datetime

# FrankenLine Banner

print "-" * 50
print "-" * 50
banner = "\n\n 	 FrankenLine\n\n "
print banner.upper()
print "-" * 50
print "-" * 50
def start_ip():
	the_IP = raw_input('\nWhat is the IP/Hostname?' + ' ' + '[+]' + ' ') # the originating IP
	return the_IP

def menu(ip_var):
	print "-" * 50
	print "\n[+] " + ip_var

	print "\n[+] Scan"
	print "[+] DNS Check" 						# The continuing options
	print "[+] Locate"
	print "[+] Change IP/Hostname"
	print "[+] More Options..."
	print "[+] Help"
	print '-' * 50

	next_step = raw_input('[+] ')  			

	def help():
		print '-' * 50
		print """\n 

	Welcome to FrankenLine!

	Geocoder, pip install geocoder


		\n"""

		print "-" * 50

	def dns():				# Checking DNS
		fqdn = socket.gethostbyaddr(ip_var)
		hostname1 = socket.gethostbyname(ip_var)
		name_ex = socket.gethostbyname_ex(ip_var)

		print "-" * 50
		print "\n[+] Checking DNS of %s...\n" % ip_var
		print "-" * 50

		print "[+]", fqdn
		print "[+]", hostname1
		print "[+]", name_ex
		print "-" * 50
		print "\n[+] Complete"


	def locate():			# Locating
		
		loc = geocoder.freegeoip(ip_var)
		print "-" * 50
		print "\n[+] Locating %s ... \n" % ip_var
		print "-" * 50
		print "[+]", loc.json
		print "-" * 50
		print "[+] Complete\n"


	def pscan():
		socket_IP = socket.gethostbyname(ip_var)

		print "-" * 50
		print "\n[+] Scanning %s ... \n" % ip_var 
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

	def change_IP():
		restart = raw_input("Change the IP? (y/n) ")
		if restart.lower() == 'y' or restart.lower() == 'yes':
			this_ip = start_ip() 
		else:
			sys.close()

	if next_step.lower() == "help" or next_step == '6':
		help()
	if next_step.lower() == "scan" or next_step == '1':
		pscan()
	if next_step.lower() == "check dns" or next_step.lower() == "dns" or next_step == '2':
		dns()
	if next_step.lower() =="locate" or next_step == '3':
		locate()
	if next_step.lower() == "more options" or next_step == "more" or next_step.lower() == '5':
		more_options()
	if next_step.lower() == "cancel" or next_step == "exit":
		print "\n[+]Bye for now...\n"
		sys.exit()
	if next_step.lower() == "change ip" or next_step.lower() == 'change':
		change_IP() 

def r_u_done(ip):
	finished = raw_input("Do you wish to continue? (y/n)")
	if finished.lower() == 'y' or finished.lower() == 'yes':
		menu(ip)
	else:
		print "[+] Exiting\n"
		sys.close()

my_ip = start_ip()
menu(my_ip)
r_u_done(my_ip)