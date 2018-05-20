#!/usr/bin/python

# a simple dns check

import os
import sys
import socket

the_IP = raw_input("\n[+]IP Address/Hostname: ")

fqdn = socket.gethostbyaddr(the_IP)
hostname1 = socket.gethostbyname(the_IP)
name_ex = socket.gethostbyname_ex(the_IP)

print "-" * 30
print "\n[+] Checking DNS of %s...\n" % the_IP
print "-" * 30

print "[+]", fqdn
print "[+]", hostname1
print "[+]", name_ex
print "-" * 30
print "\n[+] Complete"
