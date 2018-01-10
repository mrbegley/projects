import threading
try:
    import paramiko
except:
    print "[+] Run 'pip install paramiko'"

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Coming soon. Very lazy
