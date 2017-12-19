#!/usr/bin/python

# an IP/Hostname locating script

import os
import sys
try:
    import geocoder
except:
    print 'Geocoder is required ... pip install geocoder'


the_IP = raw_input("[+] IP address/Hostname: ")
loc = geocoder.freegeoip(the_IP)
print "-" * 30
print "\n[+] Locating %s \n" % the_IP
print "-" * 30
print "[+]", loc.json
print "-" * 30
print "[+] Complete\n"
