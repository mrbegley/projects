# Understanding Hashcat

# Hashcat is pretty complex, but here is a simple example
# If you don't have hashcat...then get it. It's very useful, especially if you forget your password
# I will be using kali linux to demonstrate hash cat

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install hashcat

# Let's start out by creating two users: Loser & Ugly, with passwords of hahloser & uglyloser

adduser Loser && adduser Ugly

# Then change the password by using the passwd command
# Then let's make a simple password list

vi pass.dict

# and add a few passwords there and don't forget the passwords of the new users
# Then let's locate the hashes

tail /etc/shadow

# The hashes should be folling the user
# Let's cp the entire shadow file

cp /etc/shadow hash.hash

# Now we can view which type of encryption we use

more /etc/login.defs

# The default is usually SHA-512 which is 1800 in hashcat
# Now we have the hashes, the password list and the encryption tpye, we can start cracking

hashcat -m 1800 -a 0 -o HACKED.txt hash.hash pass.dict


# the -m 1800 is the SHA-512 encryption method
# The -a is a dictionary attack
# The -o HACKED.TXT is the output for the cracked passwords
# And the hash.hash and pass.dict are the files we made earlier

# After the passwords are cracked, view the output file

cat HACKED.txt

# BOOM
