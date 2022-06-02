# Ilia Morshed
# Description - This project uses brute force attack to crack the passwords in the hashes.txt file. We use 4 module
# haslib, random, string, and time. hashlip is to turn the generated password to hash. random is to create a random password
# string is for the generated password that is made and time is to tell how long it took the system to find the password
# we use a combination of inifinte loop, for loop and branching to excute this program.
import hashlib
import random
import string
import time
from datetime import datetime
from datetime import timedelta
# we want to make a empthy list first
LIST = []
# we want to open and make the program read the file
file = open("hashes.txt", "r")
# using infinite loop, we want the program read every line and remove space  .rstrip()
# while 1 will make the loop keep going
while 1:
        #removed all space
        read = file.readline().rstrip("\n")
        # if the file that is being read has no space then break and Append the list to file
        if read == "":
                break
        LIST.append(read)
file.close()
def main():
        # we will be using a for loop here. What we want a password to be generated based on the length of the hash in the file/LIST we have
        for i in range(1,len(LIST)):
                # start timer
                t0 = time.time()
                # another inifinte loop. Here we will be generating as many random passwords we can until it matches each line
                # we will be using ascii module to create random password
                # k = i will make sure that it keeps generating password for other lines and not not the first line
                # guess is where we turn in the random password to hash
                while 1:
                        characters = ''.join(random.choices(string.ascii_letters + string.digits, k=i ))
                        guess = hashlib.md5(characters.encode('utf-8')).hexdigest()
                        # if the guess password that is hashed matches the file/LIST then timer ends
                        # since this is a while loop inside a for loop, it will keep going until i has no more lines to go through
                        if guess in LIST:
                                t1 = time.time()
                                total = t1-t0
                                convert = time.strftime("%H:%M:%S", time.gmtime(total))
                                print("\nPassword Found: " + characters + " in  - " + convert + " seconds")
                                # makes sure to skip after finds the first password and it does not go on an infinite loop to compare the first random psassword to "z"
                                break
main()



