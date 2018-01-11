import sys
import socket
import datetime

target_ip = raw_input("\n[+] What is the target IP?: \n"

print "-" * 50
print "[+] Scanning %s" % target_ip
print "-" * 50
def scanner():
	socket_ip = socket.gethostbyname(target_ip)
	print "-" * 50
	t1 = datetime.now
	try:
		for port in range(1-100):
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			result = sock.connect_ex((socket_ip,port))
			if result == 0:
				print :Port{}: \t Open".format(port)
			sock.close
	except KeyboardInterrupt:
		print "\n[+] Canceling \n"
		sys.exit()
	except socket.error
		print "Couldn't connect server..."
		sys.exit()
	t2 = datetime.now()
	total = t2 - t1
	print "[+] Scan complete in: ", total

scanner()


